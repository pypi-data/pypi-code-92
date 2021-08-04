# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# This file is auto-generated by substrates/meta/rewrite.py
# It will be surfaced by the build system as a symlink at:
#   `tensorflow_probability/substrates/numpy/distributions/markov_chain.py`
# For more info, see substrate_runfiles_symlinks in build_defs.bzl
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# (This notice adds 10 to line numbering.)


# Copyright 2021 The TensorFlow Probability Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""MarkovChain distribution."""

import functools

from tensorflow_probability.python.internal.backend.numpy.compat import v2 as tf
from tensorflow_probability.substrates.numpy import math as tfp_math
from tensorflow_probability.substrates.numpy.bijectors import bijector
from tensorflow_probability.substrates.numpy.distributions import distribution
from tensorflow_probability.substrates.numpy.distributions import log_prob_ratio
from tensorflow_probability.substrates.numpy.internal import assert_util
from tensorflow_probability.substrates.numpy.internal import distribution_util
from tensorflow_probability.substrates.numpy.internal import parameter_properties
from tensorflow_probability.substrates.numpy.internal import prefer_static as ps
from tensorflow_probability.substrates.numpy.internal import samplers
from tensorflow_probability.substrates.numpy.internal import tensor_util
from tensorflow_probability.substrates.numpy.internal import tensorshape_util

__all__ = [
    'MarkovChain',
]


class MarkovChain(distribution.Distribution):
  """Distribution of a sequence generated by a memoryless process.

  A discrete-time [Markov chain](https://en.wikipedia.org/wiki/Markov_chain)
  is a sequence of random variables in which the variable(s) at each step is
  independent of all previous variables, *conditioned on* the variable(s) at the
  immediate predecessor step. That is, there can be no (direct) long-term
  dependencies. This 'Markov property' is a simplifying assumption; for example,
  it enables efficient sampling. Many time-series models can be formulated as
  Markov chains.

  Instances of `tfd.MarkovChain` represent fully-observed, discrete-time Markov
  chains, with one or more random variables at each step. These variables may
  take continuous or discrete values. Sampling is done sequentially, requiring
  time that scales with the length of the sequence; `log_prob` evaluation is
  vectorized over timesteps, and so requires only constant time given sufficient
  parallelism.

  #### Related distributions

  The discrete-valued Markov chains modeled by `tfd.HiddenMarkovModel` (using
  a trivial observation distribution) are a special case of those supported by
  this distribution, which enable exact inference over the values in an
  unobserved chain. Continuous-valued chains with linear Gaussian transitions
  are supported by `tfd.LinearGaussianStateSpaceModel`, which can similarly
  exploit the linear Gaussian structure for exact inference of hidden states.
  These distributions are limited to chains that have the respective (discrete
  or linear Gaussian) structure.

  Autoregressive models that do *not* necessarily respect the Markov property
  are supported by `tfd.Autoregressive`, which is, in that sense, more general
  than this distribution. These models require a more involved specification,
  and sampling in general requires quadratic (rather than linear) time in the
  length of the sequence.

  Exact inference for unobserved Markov chains is not possible in
  general; however, particle filtering exploits the Markov property
  to perform approximate inference, and is often a well-suited method for
  sequential inference tasks. Particle filtering is available in TFP using
  `tfp.experimental.mcmc.particle_filter`, and related methods.

  #### Example: Gaussian random walk

  One of the simplest continuous-valued Markov chains is a
  [Gaussian random walk](
  https://en.wikipedia.org/wiki/Random_walk#Gaussian_random_walk).
  This may also be viewed as a discretized [Brownian motion](
  https://en.wikipedia.org/wiki/Brownian_motion).

  ```python
  tfd = tfp.distributions

  gaussian_walk = tfd.MarkovChain(
    initial_state_prior=tfd.Normal(loc=0., scale=1.),
    transition_fn=lambda _, x: tfd.Normal(loc=x, scale=1.),
    num_steps=100)
  # ==> `gaussian_walk.event_shape == [100]`
  # ==> `gaussian_walk.batch_shape == []`

  x = gaussian_walk.sample(5)  # Samples a matrix of 5 independent walks.
  lp = gaussian_walk.log_prob(x)  # ==> `lp.shape == [5]`.
  ```

  #### Example: batch of random walks

  To spice things up, we'll now define a *batch* of random walks, each following
  a different distribution (in this case, different starting locations).
  We'll also demonstrate scales that differ across timesteps.

  ```python
  scales = tf.convert_to_tensor([0.5, 0.3, 0.2, 0.2, 0.3, 0.2, 0.7])
  batch_gaussian_walk = tfd.MarkovChain(
    # The prior distribution determines the batch shape for the chain.
    # Transitions must respect this batch shape.
    initial_state_prior=tfd.Normal(loc=[-10., 0., 10.],
                                   scale=[1., 1., 1.]),
    transition_fn=lambda t, x: tfd.Normal(
      loc=x,
      # The `num_steps` dimension will always be leftmost in `x`, so we
      # pad the scale to the same rank as `x` to make their shapes line up.
      tf.reshape(tf.gather(scales, t),
                 tf.concat([[-1],
                            tf.ones(tf.rank(x) - 1, dtype=tf.int32)], axis=0))),
    # Limit to eight steps since we only specified scales for seven transitions.
    num_steps=8)
  # ==> `batch_gaussian_walk.event_shape == [8]`
  # ==> `batch_gaussian_walk.batch_shape == [3]`

  x = batch_gaussian_walk.sample(5)  # ==> `x.shape == [5, 3, 8]`.
  lp = batch_gaussian_walk.log_prob(x)  # ==> `lp.shape == [5, 3]`.
  ```

  #### Example: multivariate chain with longer-term dependence

  We can also define multivariate Markov chains. In addition to the obvious
  use of modeling the joint evolution of multiple variables, multivariate
  chains can also help us work around the Markov limitation by
  the trick of folding state history into the current state as an auxiliary
  variable(s). The next example, a second-order [autoregressive process](
  https://en.wikipedia.org/wiki/Autoregressive_model) with dynamic coefficients
  and scale, contains multiple time-dependent variables and also uses an
  auxiliary `previous_level` variable to enable the transition function
  to access the previous *two* steps of history:

  ```python

  def transition_fn(_, previous_state):
    return tfd.JointDistributionNamedAutoBatched(
        # The transition distribution must match the batch shape of the chain.
        # Since `log_scale` is a scalar quantity, its shape is the batch shape.
        batch_ndims=tf.rank(previous_state['log_scale']),
        model={
            # The autoregressive coefficients and the `log_scale` each follow
            # an independent slow-moving random walk.
            'coefs': tfd.Normal(loc=previous_state['coefs'], scale=0.01),
            'log_scale': tfd.Normal(loc=previous_state['log_scale'],
                                    scale=0.01),
            # The level is a linear combination of the previous *two* levels,
            # with additional noise of scale `exp(log_scale)`.
            'level': lambda coefs, log_scale: tfd.Normal(  # pylint: disable=g-long-lambda
                loc=(coefs[..., 0] * previous_state['level'] +
                     coefs[..., 1] * previous_state['previous_level']),
                scale=tf.exp(log_scale)),
            # Store the previous level to access at the next step.
            'previous_level': tfd.Deterministic(previous_state['level'])})
  ```

  Note: when using an autobatched joint distribution as a transition model,
  as we did here, it is necessary to explicitly set its `batch_ndims` to the
  batch rank of the passed-in state. This will be at least the batch rank of the
  initial state prior, but may be greater, e.g., when evaluating multiple iid
  samples. In general, the correct batch rank is that of the previous state
  `Tensor`s.

  ```python
  process = tfd.MarkovChain(
      # For simplicity, define the prior as a 'transition' from fixed values.
      initial_state_prior=transition_fn(
          0, previous_state={
              'coefs': [0.7, -0.2],
              'log_scale': -1.,
              'level': 0.,
              'previous_level': 0.}),
      transition_fn=transition_fn,
      num_steps=100)
  # ==> `process.event_shape == {'coefs': [100, 2], 'log_scale': [100],
  #                              'level': [100], 'previous_level': [100]}`
  # ==> `process.batch_shape == []`

  x = process.sample(5)
  # ==> `x['coefs'].shape == [5, 100, 2]`
  # ==> `x['log_scale'].shape == [5, 100]`
  # ==> `x['level'].shape == [5, 100]`
  # ==> `x['previous_level'].shape == [5, 100]`
  lp = process.log_prob(x)  # ==> `lp.shape == [5]`.
  ```

  """

  def __init__(self,
               initial_state_prior,
               transition_fn,
               num_steps,
               experimental_use_kahan_sum=False,
               validate_args=False,
               name='MarkovChain'):
    """Initializes the Markov chain.

    Note that the `initial_state_prior` and `transition_fn` used to specify a
    Markov chain are the same parameters required for particle filtering
    inference with `tfp.experimental.mcmc.particle_filter`.

    Args:
      initial_state_prior: `tfd.Distribution` instance describing a prior
        distribution on the state at step 0. This may be a joint distribution.
      transition_fn: Python `callable` with signature
        `current_state_dist = transition_fn(previous_step, previous_state)`.
        The arguments are an integer `previous_step`, and `previous_state`,
        a (structure of) Tensor(s) like a sample from the
        `initial_state_prior`. The returned `current_state_dist` must have the
        same `dtype`, `batch_shape`, and `event_shape` as `initial_state_prior`.
      num_steps: Integer `Tensor` scalar number of steps in the chain.
      experimental_use_kahan_sum: If `True`, use
        [Kahan summation](
        https://en.wikipedia.org/wiki/Kahan_summation_algorithm) to mitigate
        accumulation of floating-point error in log_prob calculation.
      validate_args: Python `bool`, default `False`. Whether to validate input
        with asserts. If `validate_args` is `False`, and the inputs are
        invalid, correct behavior is not guaranteed.
      name: The name to give ops created by this distribution.
    """
    parameters = dict(locals())
    with tf.name_scope(name) as name:
      self._initial_state_prior = initial_state_prior
      self._transition_fn = transition_fn
      self._num_steps = tensor_util.convert_nonref_to_tensor(
          num_steps, dtype_hint=tf.int32, name='num_steps',
          as_shape_tensor=True)
      self._experimental_use_kahan_sum = experimental_use_kahan_sum
      super(MarkovChain, self).__init__(
          parameters=parameters,
          validate_args=validate_args,
          reparameterization_type=initial_state_prior.reparameterization_type,
          dtype=initial_state_prior.dtype,
          allow_nan_stats=initial_state_prior.allow_nan_stats,
          name=name)

  @property
  def initial_state_prior(self):
    return self._initial_state_prior

  @property
  def num_steps(self):
    return self._num_steps

  @property
  def transition_fn(self):
    return self._transition_fn

  @property
  def _sum_fn(self):
    if self._experimental_use_kahan_sum:
      return lambda x, axis: tfp_math.reduce_kahan_sum(x, axis=axis).value
    return tf.reduce_sum

  @classmethod
  def _parameter_properties(cls, dtype, num_classes=None):
    return dict(
        initial_state_prior=parameter_properties.BatchedComponentProperties(),
        num_steps=parameter_properties.ShapeParameterProperties())

  def _event_shape(self):
    def _prefix_with_num_steps(event_shape):
      if tensorshape_util.rank(event_shape) is None:
        return tf.TensorShape(None)
      return tensorshape_util.concatenate([tf.get_static_value(self.num_steps)],
                                          event_shape)
    return tf.nest.map_structure(_prefix_with_num_steps,
                                 self.initial_state_prior.event_shape)

  def _event_shape_tensor(self):
    return tf.nest.map_structure(
        lambda event_shape: ps.concat([[self.num_steps], event_shape], axis=0),
        self.initial_state_prior.event_shape_tensor())

  def _batch_shape(self):
    # This matches the automatically-inferred batch shape, but we implement it
    # anyway in order to support the structured batch shapes of
    # non-autobatched JDs.
    return self.initial_state_prior.batch_shape

  def _batch_shape_tensor(self):
    # This matches the automatically-inferred batch shape, but we implement it
    # anyway in order to support the structured batch shapes of
    # non-autobatched JDs.
    return self.initial_state_prior.batch_shape_tensor()

  def _step_axes(self):
    """Index of the `num_steps` axis in each event part, as negative int(s)."""
    return tf.nest.map_structure(
        lambda nd: -(1 + nd),
        tf.nest.map_structure(ps.rank_from_shape,
                              self.initial_state_prior.event_shape_tensor()))

  def _sample_and_log_prob_helper(self,
                                  sample_shape,
                                  seed=None,
                                  compute_log_prob=False):
    """Draws samples from the chain and optionally accumulates the log_prob."""
    prior_seed, loop_seed = samplers.split_seed(
        n=2, seed=seed, salt='markov_chain_sample')

    if compute_log_prob:
      sample_attr = 'experimental_sample_and_log_prob'
      extract_sample_fn = lambda x_and_lp: x_and_lp[0]
      extract_lp_fn = lambda x_and_lp: self._sum_fn(x_and_lp[1], axis=0)
    else:
      sample_attr = 'sample'
      extract_sample_fn = lambda x: x
      extract_lp_fn = lambda x: 0.

    prior_result = getattr(self.initial_state_prior, sample_attr)(
        sample_shape, seed=prior_seed)

    loop_body = _make_sample_loop_body(
        self.transition_fn,
        sample_attr=sample_attr,
        extract_sample_fn=extract_sample_fn)
    _, results = tf.scan(loop_body,
                         elems=tf.range(1, self.num_steps),
                         initializer=(loop_seed, prior_result))

    # Concatenate prior sample (and lp) with remaining samples (and lps).
    results = tf.nest.map_structure(concat_initial, prior_result, results)
    samples, lp = extract_sample_fn(results), extract_lp_fn(results)

    # Move leftmost `num_steps` dimension into the event shape.
    samples = move_dimensions(samples, 0, self._step_axes())
    return samples, lp

  def _sample_n(self, sample_shape, seed=None):
    samples, _ = self._sample_and_log_prob_helper(
        sample_shape, seed=seed, compute_log_prob=False)
    return samples

  # We need to bypass base Distribution reshaping logic, so we
  # tactically implement the `_call_sample_n` redirector.
  def _call_sample_n(self, sample_shape, seed, **kwargs):
    return self._sample_n(sample_shape,
                          seed=seed() if callable(seed) else seed,
                          **kwargs)

  def _sample_and_log_prob(self, sample_shape, seed=None):
    return self._sample_and_log_prob_helper(
        sample_shape, seed=seed, compute_log_prob=True)

  def _log_prob_parts(self, x):
    """Returns the prior log-prob and elementwise transition log-probs."""
    # Move step dimension to the leftmost location, so that it appears to the
    # transition model as the leftmost sample dimension rather than as the
    # rightmost batch dimension (which could otherwise conflict with existing
    # batch dimensions).
    x = move_dimensions(x, self._step_axes(), 0)
    prior_lp = self.initial_state_prior.log_prob(
        tf.nest.map_structure(lambda state_part: state_part[0], x))
    num_steps = ps.shape(tf.nest.flatten(x)[0])[0]

    return prior_lp, self.transition_fn(
        tf.range(num_steps - 1),
        tf.nest.map_structure(
            lambda state_part: state_part[:num_steps - 1], x)
        ).log_prob(tf.nest.map_structure(
            lambda state_part: state_part[1 : num_steps], x))

  def _log_prob(self, x):
    prior_lp, transition_lps = self._log_prob_parts(x)
    transition_lp = self._sum_fn(transition_lps, axis=0)

    with tf.control_dependencies(
        _assert_same_shape(
            prior_lp, transition_lp, validate_args=self.validate_args,
            message='The shape of the `log_prob` returned by the transition '
            'distribution does not match the `log_prob` from the '
            'initial state prior. This indicates that the transition '
            'distribution\'s batch shape is incorrect. Please ensure that '
            '`initial_state_prior.batch_shape == transition_fn(0, '
            'initial_state_prior.sample()).batch_shape`.')):
      return prior_lp + transition_lp

  def _default_event_space_bijector(self):
    transition_dist = self.transition_fn(
        0, self.initial_state_prior.sample(seed=samplers.zeros_seed()))
    transition_bijector = (
        transition_dist.experimental_default_event_space_bijector())
    # We can share a single bijector across the whole chain if:
    # 1. The prior and transition distributions use the same bijector, and
    # 2. This bijector has no batch shape (which could conflict with
    #    the `num_steps` axis of the chain).
    if (transition_bijector ==
        self.initial_state_prior.experimental_default_event_space_bijector()
        and tensorshape_util.rank(
            transition_bijector.experimental_batch_shape()) == 0):
      return transition_bijector

    return _MarkovChainBijector(
        self,
        transition_bijector=transition_bijector,
        bijector_fn=lambda d: d.experimental_default_event_space_bijector())

  def _parameter_control_dependencies(self, is_init):
    if not self.validate_args:
      return []
    assertions = []
    if is_init != tensor_util.is_ref(self._num_steps):
      assertions.append(assert_util.assert_greater_equal(
          self._num_steps, 1,
          message='Argument `num_steps` must be at least 1.'))
    return assertions

  def _sample_control_dependencies(self, x):
    if not self.validate_args:
      return []
    parts_num_steps = tf.nest.flatten(tf.nest.map_structure(
        lambda x, k: ps.shape(x)[k], x, self._step_axes()))
    return [
        assert_util.assert_equal(  # pylint: disable=g-complex-comprehension
            num_steps, self.num_steps,
            message='Input shape does not match the expected num_steps.')
        for num_steps in parts_num_steps]


def _make_sample_loop_body(transition_fn,
                           sample_attr='sample',
                           extract_sample_fn=lambda x: x):
  """Builds the scan loop body to sample from a Markov chain."""

  def loop_body(seed_and_state, step):
    seed, previous_result = seed_and_state
    state = extract_sample_fn(previous_result)  # Maybe strip log_prob.
    current_step_seed, seed = samplers.split_seed(seed, n=2)
    new_result = getattr(transition_fn(step - 1, state), sample_attr)(
        seed=current_step_seed)
    return seed, new_result

  return loop_body


def _assert_same_shape(x, y,
                       message='Shapes do not match.',
                       validate_args=False):
  """Asserts (statically if possible) that two Tensor have the same shape."""
  if not tensorshape_util.is_compatible_with(x.shape, y.shape):
    raise ValueError(message +
                     ' Saw shapes: {} vs {}.'.format(x.shape, y.shape))

  assertions = []
  if validate_args and not (tensorshape_util.is_fully_defined(x.shape) and
                            tensorshape_util.is_fully_defined(y.shape)):
    assertions.append(
        assert_util.assert_equal(
            tf.shape(x), tf.shape(y), message=message))
  return assertions


# pylint: disable=protected-access
@log_prob_ratio.RegisterLogProbRatio(MarkovChain)
def _markov_chain_log_prob_ratio(p, x, q, y, name=None):
  """Implements `log_prob_ratio` for tfd.MarkovChain."""
  with tf.name_scope(name or 'markov_chain_log_prob_ratio'):
    # TODO(davmre): In the case where `p` and `q` have components of the same
    # families (in addition to just both being MarkovChains), we might prefer to
    # recursively call `log_prob_ratio` instead of just subtracting log probs.
    p_prior_lp, p_transition_lps = p._log_prob_parts(x)
    q_prior_lp, q_transition_lps = q._log_prob_parts(y)
    prior_lp_ratio = p_prior_lp - q_prior_lp
    transition_lp_ratios = p_transition_lps - q_transition_lps
    if (p._experimental_use_kahan_sum or
        q._experimental_use_kahan_sum):
      transition_lp_ratio = tfp_math.reduce_kahan_sum(
          transition_lp_ratios, axis=0).value
    else:
      transition_lp_ratio = tf.reduce_sum(transition_lp_ratios, axis=0)
    return prior_lp_ratio + transition_lp_ratio
# pylint: enable=protected-access


class _MarkovChainBijector(bijector.Bijector):
  """Applies distinct bijectors to initial + transition states of a chain."""

  def __init__(self,
               chain,
               bijector_fn,
               transition_bijector,
               name='markov_chain_bijector'):
    """Initializes the MarkovChain bijector.

    This bijector maps into the support of the corresponding MarkovChain
    distribution, using separate bijectors for the head (initial state)
    and tail (transition states) of the chain. Its input is a pair of
    unconstrained structures each matching `chain.dtype`, and the output is a
    constrained structure matching `chain.dtype`. Note that the inputs
    to the two bijectors may have different shapes, corresponding to the
    inverse images of the two bijectors, but the outputs must have the same
    shape in order to support concatenation along the `num_steps` axis.

    Conceptually, the Markov chain bijector performs the same transformation as
    the `joint_distribution._DefaultJointBijector` for a hypothetical joint
    distribution that samples from the chain one step at a time:

    ```python
    @tfd.JointDistributionCoroutineAutoBatched
    def markov_chain_equivalent():
      x = yield initial_state_prior
      for i in range(1, num_steps):
        x = yield transition_fn(i, x)
    markov_chain_equivalent_joint_bijector = (
      markov_chain_equivalent.experimental_default_event_space_bijector())
    ```

    However, just as `MarkovChain` uses low-level looping and batch operations
    for better performance than the corresponding joint
    distribution, the `MarkovChainBijector` is more efficient than the
    corresponding joint bijector.

    Args:
      chain: Instance of `tfd.MarkovChain`.
      bijector_fn: Callable with signature `bij = bijector_fn(dist)`, where
        `dist` is a `tfd.Distribution` instance. This is applied to the
        `chain.initial_state_prior` and to distributions returned by
        `chain.transition_fn(...)`.
      transition_bijector: Bijector instance for a single step of the
        transition model. This is typically equal to
        `bijector_fn(markov_chain.transition_fn(0,
        markov_chain.initial_state_prior.sample()))`; passing it explicitly
        avoids the need to recreate it whenever the chain bijector is
        copied or otherwise re-initialized.
      name: The name to give ops created by this bijector.

    #### Example

    For example, consider the following chain, which has dtype
    `{'probs': tf.float32}`, and describes a process in which a 2D vector
    is sampled from the probability simplex and then gradually corrupted by
    Gaussian noise (which will in general push it out of the simplex):

    ```python
    chain = tfd.MarkovChain(
      initial_state_prior=tfd.JointDistributionNamedAutoBatched(
          {'probs': tfd.Dirichlet([1., 1.])}),
      transition_fn=lambda _, x: tfd.JointDistributionNamedAutoBatched(
          {'probs': tfd.MultivariateNormalDiag(loc=x['probs'],
                                               scale_diag=[0.1, 0.1])},
        batch_ndims=ps.rank(x['probs'])),
      num_steps=10)
    ```

    Transformations of this distribution apply separate bijectors
    for the `Dirichlet` initial state and `MultivariateNormalDiag` transitions:

    ```python
    bij = chain.experimental_default_event_space_bijector()
    y = chain.sample(5)  # Shape: {'probs': [5, 10, 2]}
    x = chain.inverse(y)  # Shape: [{'probs': [5, 1]}, {'probs': [5, 9, 2]}]
    ```

    Note that the pulled-back `x` is a pair of structures, of shapes
    `{'probs': [5, 1]}` and  `{'probs': [5, 9, 2]}` respectively. The first is
    the result of pulling the initial state vectors back through the Dirichlet
    event space bijector, which inverts shape-`[2]` vectors on the simplex to
    shape-`[1]` unconstrained vectors.  The second comes from pulling the
    shape-`[2]` chain state at each of the remaining `9` timesteps back through
    the `MultivariateNormalDiag` event space bijector, which is just
    the identity bijector, resulting in vectors of shape `[2]`.

    """
    parameters = dict(locals())
    with tf.name_scope(name):
      self._chain = chain
      self._bijector_fn = bijector_fn
      self._initial_bijector = bijector_fn(chain.initial_state_prior)
      self._transition_bijector = transition_bijector

      inverse_min_event_ndims = tf.nest.map_structure(
          ps.rank_from_shape, chain.event_shape_tensor())
      super(_MarkovChainBijector, self).__init__(
          forward_min_event_ndims=(
              self._initial_bijector.inverse_event_ndims(
                  tf.nest.map_structure(lambda nd: nd - 1,
                                        inverse_min_event_ndims)),
              self._transition_bijector.inverse_event_ndims(
                  inverse_min_event_ndims)),
          inverse_min_event_ndims=inverse_min_event_ndims,
          is_constant_jacobian=(
              self.initial_bijector.is_constant_jacobian and
              self.transition_bijector.is_constant_jacobian),
          validate_args=chain.validate_args,
          parameters=parameters,
          name=name)

  @property
  def bijector_fn(self):
    return self._bijector_fn

  @property
  def chain(self):
    return self._chain

  @property
  def initial_bijector(self):
    return self._initial_bijector

  @property
  def transition_bijector(self):
    return self._transition_bijector

  @classmethod
  def _parameter_properties(cls, dtype):
    return dict(
        chain=parameter_properties.BatchedComponentProperties(),
        transition_bijector=parameter_properties.BatchedComponentProperties(
            # The transition bijector contributes no batch shape
            # beyond that from the chain itself.
            event_ndims=None))

  def _apply_forward_scan(self, fn, x0, xs):
    """Runs the chain forward, accumulating `fn(b, x, y)` vals at every step.

    Args:
      fn: Callable with signature `result = fn(b, x, y)`.
      x0: Structure of initial state `Tensors`, each of shape
          `concat([[batch_shape], unconstrained_prior_event_shape])`.
      xs: Structure of `Tensors`, each of shape
          `concat([[batch_shape], [num_steps - 1],
          unconstrained_transition_event_shape])`.
    Returns:
      fs: Result `Tensor` of shape
        `concat([[num_steps], batch_shape, result_shape])`, where `result_shape`
        is the shape of the result from an unbatched call to `fn`.
    """
    xs_step_axes = tf.nest.map_structure(
        lambda nd: -nd,
        self.transition_bijector.inverse_event_ndims(
            # Outputs `y` have the num_steps axis at `-inverse_min_event_ndims`.
            self.inverse_min_event_ndims))
    xs = move_dimensions(xs, source=xs_step_axes, dest=0)

    # Evaluate the initial state.
    y0 = self.initial_bijector.forward(x0)
    f0 = fn(self.initial_bijector, x0, y0)

    # Evaluate the rest of the chain.
    def loop_body(previous_y_and_result, idx):
      previous_y, _ = previous_y_and_result
      bij = self.bijector_fn(self.chain.transition_fn(idx, previous_y))
      x_i = tf.nest.map_structure(lambda x: x[idx - 1], xs)
      y_i = bij.forward(x_i)
      f_i = fn(bij, x_i, y_i)
      return (y_i,
              tf.nest.map_structure(lambda a, b: tf.cast(a, b.dtype), f_i, f0))
    _, fs = tf.scan(loop_body,
                    elems=tf.range(1, self.chain.num_steps),
                    initializer=(y0, f0))
    return concat_initial(f0, fs)

  def _apply_batch(self, fn, y):
    """Applies `fn(b, y)` at each step of the chain.

    Args:
      fn: Callable with signature `result = fn(b, y)`.
      y: Structure of `Tensor`s, of shape
         `batch_shape + self.chain.event_shape`.
    Returns:
      f0: `Tensor` of shape `batch_shape + result_shape`.
      fs: `Tensor` of shape `[num_steps - 1] + batch_shape + result_shape`.
    """
    y = move_dimensions(y, source=self.chain._step_axes(), dest=0)  # pylint: disable=protected-access
    f0 = fn(self.initial_bijector, tf.nest.map_structure(lambda y: y[0], y))
    transition_dist = self.chain.transition_fn(
        tf.range(self.chain.num_steps - 1),
        tf.nest.map_structure(lambda y: y[:-1], y))
    return (f0,
            fn(self.bijector_fn(transition_dist),
               tf.nest.map_structure(lambda y: y[1:], y)))

  def _forward(self, x):
    x0, xs = x
    y = self._apply_forward_scan(fn=lambda b, x, y: y, x0=x0, xs=xs)
    return move_dimensions(y, source=0, dest=self.chain._step_axes())  # pylint: disable=protected-access

  def _inverse(self, y):
    xs_step_axes = tf.nest.map_structure(
        lambda nd: -nd,
        self.transition_bijector.inverse_event_ndims(
            # Outputs `y` have the num_steps axis at `-inverse_min_event_ndims`.
            self.inverse_min_event_ndims))
    x0, xs = self._apply_batch(fn=lambda b, y: b.inverse(y), y=y)
    return (x0, move_dimensions(xs, source=0, dest=xs_step_axes))

  def _forward_log_det_jacobian(self, x):
    inverse_ndims_for_one_step = tf.nest.map_structure(
        lambda nd: nd - 1, self.inverse_min_event_ndims)
    x0, xs = x
    fldjs = self._apply_forward_scan(
        fn=lambda b, x, y: compute_and_maybe_broadcast_ldj(  # pylint: disable=g-long-lambda
            b, x,
            event_ndims=b.inverse_event_ndims(inverse_ndims_for_one_step),
            ldj_fn=lambda b: b.forward_log_det_jacobian),
        x0=x0, xs=xs)
    return tf.reduce_sum(fldjs, axis=0)

  def _inverse_log_det_jacobian(self, y):
    inverse_ndims_for_one_step = tf.nest.map_structure(
        lambda nd: nd - 1, self.inverse_min_event_ndims)
    initial_ildj, ildjs = self._apply_batch(
        fn=lambda b, x: compute_and_maybe_broadcast_ldj(  # pylint: disable=g-long-lambda
            b, x,
            event_ndims=inverse_ndims_for_one_step,
            ldj_fn=lambda b: b.inverse_log_det_jacobian),
        y=y)
    return initial_ildj + tf.reduce_sum(ildjs, axis=0)

  def _forward_event_shape(self, event_shape):
    _, tail_shape = event_shape
    return tf.nest.map_structure(
        lambda s: tensorshape_util.concatenate([1 + s[0]], s[1:]),
        self.transition_bijector.forward_event_shape(tail_shape))

  def _forward_event_shape_tensor(self, event_shape):
    _, tail_shape = event_shape
    return tf.nest.map_structure(
        lambda s: ps.concat([[1 + s[0]], s[1:]], axis=0),
        self.transition_bijector.forward_event_shape_tensor(tail_shape))

  def _inverse_event_shape(self, event_shape):
    num_steps = tf.nest.flatten(event_shape)[0][0]
    head_shape = tf.nest.map_structure(lambda s: s[1:], event_shape)
    tail_shape = tf.nest.map_structure(
        lambda s: tensorshape_util.concatenate([num_steps - 1], s[1:]),
        event_shape)
    return (self.initial_bijector.inverse_event_shape(head_shape),
            self.transition_bijector.inverse_event_shape(tail_shape))

  def _inverse_event_shape_tensor(self, event_shape):
    num_steps = tf.nest.flatten(event_shape)[0][0]
    head_shape = tf.nest.map_structure(lambda s: s[1:], event_shape)
    tail_shape = tf.nest.map_structure(
        lambda s: ps.concat([[num_steps - 1], s[1:]], axis=0),
        event_shape)
    return (self.initial_bijector.inverse_event_shape_tensor(head_shape),
            self.transition_bijector.inverse_event_shape_tensor(tail_shape))

  def _inverse_dtype(self, dtype):
    return (self.initial_bijector.inverse_dtype(dtype),
            self.transition_bijector.inverse_dtype(dtype))

  def _forward_dtype(self, dtype):
    head_dtype, _ = dtype
    return self.initial_bijector.forward_dtype(head_dtype)


def move_dimensions(xs, source, dest):
  if tf.nest.is_nested(xs):
    if not tf.nest.is_nested(source):
      source = tf.nest.map_structure(lambda _: source, xs)
    if not tf.nest.is_nested(dest):
      dest = tf.nest.map_structure(lambda _: dest, xs)
  return tf.nest.map_structure(
      distribution_util.move_dimension, xs, source, dest)


def compute_and_maybe_broadcast_ldj(
    b, x, event_ndims, ldj_fn=lambda b: b.forward_log_det_jacobian):
  """Broadcasts the forward/inverse log det jacobian to full batch shape."""
  ldj = ldj_fn(b)(x, event_ndims=event_ndims)
  x_batch_shape_parts = [
      ps.shape(t)[:ps.rank(t) - nd]
      for (t, nd) in zip(tf.nest.flatten(x), tf.nest.flatten(event_ndims))]
  return tf.broadcast_to(ldj, functools.reduce(ps.broadcast_shape,
                                               x_batch_shape_parts,
                                               ps.shape(ldj)))


def concat_initial(x0, xs):
  return tf.nest.map_structure(
      lambda x0, xs: tf.concat([x0[tf.newaxis, ...], xs], axis=0),
      x0, xs)

