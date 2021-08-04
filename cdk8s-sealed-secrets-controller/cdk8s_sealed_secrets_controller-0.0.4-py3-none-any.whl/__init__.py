'''
# cdk8s-sealed-secrets-controller

Extends APIObjects for sealed secrets controller.

## Usage:

```
import { Construct } from 'constructs';
import { App, Chart, ChartProps } from 'cdk8s';
import { SealedSecretsTemplate } from '@opencdk8s/cdk8s-sealed-secrets-controller';

export class MyChart extends Chart {
  constructor(scope: Construct, id: string, props: ChartProps = { }) {
    super(scope, id, props);
      new SealedSecretsTemplate(this, 'example', {});
    }
}

const app = new App();
new MyChart(app, 'example');
app.synth();
```
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import constructs


class ControllerStrategy(
    metaclass=jsii.JSIIMeta,
    jsii_type="@opencdk8s/cdk8s-sealed-secrets-controller.ControllerStrategy",
):
    def __init__(self) -> None:
        jsii.create(ControllerStrategy, self, [])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maxSurge")
    def max_surge(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxSurge"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maxUnavailable")
    def max_unavailable(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxUnavailable"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))


class SealedSecretsControllerOptions(
    metaclass=jsii.JSIIMeta,
    jsii_type="@opencdk8s/cdk8s-sealed-secrets-controller.SealedSecretsControllerOptions",
):
    def __init__(self) -> None:
        jsii.create(SealedSecretsControllerOptions, self, [])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="args")
    def args(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "args"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="command")
    def command(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "command"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="env")
    def env(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "env"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="image")
    def image(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "image"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="minReadySeconds")
    def min_ready_seconds(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minReadySeconds"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespace"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="replicas")
    def replicas(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "replicas"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="runAsNonRoot")
    def run_as_non_root(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "runAsNonRoot"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="selector")
    def selector(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "selector"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="strategy")
    def strategy(self) -> typing.Optional[ControllerStrategy]:
        return typing.cast(typing.Optional[ControllerStrategy], jsii.get(self, "strategy"))


class SealedSecretsTemplate(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@opencdk8s/cdk8s-sealed-secrets-controller.SealedSecretsTemplate",
):
    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        options: SealedSecretsControllerOptions,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param options: -
        '''
        jsii.create(SealedSecretsTemplate, self, [scope, id, options])


__all__ = [
    "ControllerStrategy",
    "SealedSecretsControllerOptions",
    "SealedSecretsTemplate",
]

publication.publish()
