# -*- coding: utf-8 -*-

# Copyright 2021 Jean-Baptiste Delisle
#
# This file is part of samsam.
#
# samsam is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# samsam is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with samsam.  If not, see <http://www.gnu.org/licenses/>.

import numpy as np


def acf(x):
  r"""
  Auto-correlation function of the time series x.

  Parameters
  ----------
  x : (n,) or (n, d) ndarray
    Time series values (which can be multi-dimensional).

  Returns
  -------
  R : (n,) or (n, d) ndarray
    Auto-correlation as a function of lag.
  """

  nt = x.shape[0]
  f = np.fft.fft(x - np.mean(x, axis=0), axis=0, n=2 * nt)
  S = abs(f)**2
  R = np.fft.ifft(S, axis=0)[:nt].real
  R /= R[0]
  return (R)


def iat(x=None, R=None, window=50):
  r"""
  Integrated auto-correlation time of the time series x.

  Parameters
  ----------
  x : (n,) or (n, d) ndarray or None
    Time series values (which can be multi-dimensional).
    If R = acf(x) is provided, this is not used.
  R : (n,) or (n, d) ndarray or None
    Auto-correlation as a function of lag.
  window : int
    Window used to smooth the acf.

  Returns
  -------
  IAT : float or (d,) ndarray
    Integrated auto-correlation time (for each dimension).
  """

  if R is None:
    R = acf(x)
  nt = len(R)
  nwindow = nt // window
  nt = nwindow * window
  if R.ndim == 1:
    Ga = np.sum(R[:nt].reshape(nwindow, window), axis=1)
    dGa = Ga[1:] - Ga[:-1]
    kneg = np.where(Ga <= 0)[0][0]
    kincr = np.where(dGa >= 0)[0][0]
    kmax = min(kneg, kincr)
    IAT = 2 * np.sum(Ga[:kmax]) - 1
  else:
    nDim = R.shape[1]
    Ga = np.sum(R[:nt].reshape(nwindow, window, nDim), axis=1)
    dGa = Ga[1:] - Ga[:-1]
    IAT = np.empty(nDim)
    for c in range(nDim):
      kneg = np.where(Ga[:, c] <= 0)[0][0]
      kincr = np.where(dGa[:, c] >= 0)[0][0]
      kmax = min(kneg, kincr)
      IAT[c] = 2 * np.sum(Ga[:kmax, c]) - 1
  return (IAT)
