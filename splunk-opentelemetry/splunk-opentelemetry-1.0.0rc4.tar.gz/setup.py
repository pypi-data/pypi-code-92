# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['splunk_otel', 'splunk_otel.cmd']

package_data = \
{'': ['*']}

install_requires = \
['opentelemetry-api==1.4.1',
 'opentelemetry-instrumentation==0.23b2',
 'opentelemetry-sdk==1.4.1']

extras_require = \
{'all': ['opentelemetry-propagator-b3==1.4.1',
         'opentelemetry-exporter-jaeger-thrift==1.4.1',
         'opentelemetry-exporter-otlp-proto-grpc==1.4.1'],
 'b3': ['opentelemetry-propagator-b3==1.4.1'],
 'jaeger': ['opentelemetry-exporter-jaeger-thrift==1.4.1'],
 'otlp': ['opentelemetry-exporter-otlp-proto-grpc==1.4.1']}

entry_points = \
{'console_scripts': ['splk-py-trace = splunk_otel.cmd.trace:run_deprecated',
                     'splk-py-trace-bootstrap = '
                     'splunk_otel.cmd.bootstrap:run_deprecated',
                     'splunk-py-trace = splunk_otel.cmd.trace:run',
                     'splunk-py-trace-bootstrap = '
                     'splunk_otel.cmd.bootstrap:run'],
 'opentelemetry_distro': ['splunk_distro = splunk_otel.distro:SplunkDistro']}

setup_kwargs = {
    'name': 'splunk-opentelemetry',
    'version': '1.0.0rc4',
    'description': 'The Splunk distribution of OpenTelemetry Python Instrumentation provides a Python agent that automatically instruments your Python application to capture and report distributed traces to SignalFx APM.',
    'long_description': '---\n\n<p align="center">\n  <strong>\n    <a href="#getting-started">Getting Started</a>\n    &nbsp;&nbsp;&bull;&nbsp;&nbsp;\n    <a href="CONTRIBUTING.md">Getting Involved</a>\n    &nbsp;&nbsp;&bull;&nbsp;&nbsp;\n    <a href="MIGRATING.md">Migrating from SignalFx Python Tracing</a>\n  </strong>\n</p>\n\n<p align="center">\n  <span class="otel-version-badge"><a href="https://github.com/open-telemetry/opentelemetry-python/releases/tag/v1.4.1"><img alt="OpenTelemetry Python Version" src="https://img.shields.io/badge/otel-1.4.1-blueviolet?style=for-the-badge"/></a></span>\n  <a href="https://github.com/signalfx/splunk-otel-python/releases">\n    <img alt="GitHub release (latest SemVer)" src="https://img.shields.io/github/v/release/signalfx/splunk-otel-python?style=for-the-badge">\n  </a>\n  <a href="https://pypi.org/project/splunk-opentelemetry/">\n    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/splunk-opentelemetry?style=for-the-badge">\n  </a>\n  <a href="https://circleci.com/gh/signalfx/splunk-otel-python">\n    <img alt="CircleCI" src="https://img.shields.io/circleci/build/github/signalfx/splunk-otel-python/main?style=for-the-badge">\n  </a>\n  <a href="https://codecov.io/gh/signalfx/splunk-otel-python">\n    <img alt="Codecov" src="https://img.shields.io/codecov/c/github/signalfx/splunk-otel-python?style=for-the-badge&token=XKXjEQKGaK">\n  </a>\n</p>\n\n<p align="center">\n  <strong>\n    <a href="https://github.com/signalfx/tracing-examples/tree/main/opentelemetry-tracing/opentelemetry-python-tracing">Examples</a>\n    &nbsp;&nbsp;&bull;&nbsp;&nbsp;\n    <a href="SECURITY.md">Security</a>\n    &nbsp;&nbsp;&bull;&nbsp;&nbsp;\n    <a href="https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation">Supported Libraries</a>\n    &nbsp;&nbsp;&bull;&nbsp;&nbsp;\n    <a href="docs/troubleshooting.md">Troubleshooting</a>\n  </strong>\n</p>\n\n---\n<span class="docs-version-header">The documentation below refers to the in development version of this package. Docs for the latest version ([v1.0.0rc4](https://github.com/signalfx/splunk-otel-python/releases/tag/v1.0.0rc4)) can be found [here](https://github.com/signalfx/splunk-otel-python/blob/v1.0.0rc4/README.md).</span>\n---\n\n# Splunk Distribution of OpenTelemetry Python\n\nThe Splunk distribution of [OpenTelemetry\nPython](https://github.com/open-telemetry/opentelemetry-python) provides\nmultiple installable packages that automatically instruments your Python\napplication to capture and report distributed traces to Splunk APM.\nInstrumentation works by patching supported libraries at runtime with an\nOpenTelemetry-compatible tracer to capture and export trace spans.\n\nThis Splunk distribution comes with the following defaults:\n\n- [W3C tracecontext](https://www.w3.org/TR/trace-context/) and [W3C\n  baggage](https://www.w3.org/TR/baggage/) context propagation;\n  [B3](https://github.com/openzipkin/b3-propagation) can also be\n  [configured](docs/advanced-config.md#trace-propagation-configuration).\n- [OTLP gRPC\n  exporter](https://opentelemetry-python.readthedocs.io/en/latest/exporter/otlp/otlp.html)\n  configured to send spans to a locally running [Splunk OpenTelemetry\n  Connector](https://github.com/signalfx/splunk-otel-collector)\n  (`http://localhost:4317`).\n- Unlimited default limits for [configuration options](docs/advanced-config.md#trace-configuration) to\n  support full-fidelity traces.\n\nIf you\'re currently using the SignalFx Tracing Library for Python and want to\nmigrate to the Splunk Distribution of OpenTelemetry Python, see [Migrate from\nthe SignalFx Tracing Library for Python](MIGRATING.md).\n\n> :construction: This project is currently in **BETA**. It is **officially supported** by Splunk. However, breaking changes **MAY** be introduced.\n\n## Requirements\n\nThis Splunk Distribution of OpenTelemetry requires Python 3.6 or later.\nIf you\'re still using Python 2, continue using the SignalFx Tracing Library\nfor Python.\n\n## Getting Started\n\nTo get started, install the `splunk-opentelemetry[all]` package, run the bootstrap\nscript and wrap your run command with `splunk-py-trace`.\n\nFor example, if the runtime parameters were:\n\n```\npython main.py --port=8000\n```\n\nThen the runtime parameters should be updated to:\n\n```\n$ pip install splunk-opentelemetry[all]\n$ splunk-py-trace-bootstrap\n$ OTEL_SERVICE_NAME=my-python-app \\\n    splunk-py-trace python main.py --port=8000\n```\n\nTo see the Python instrumentation in action with sample applications, see our\n[examples](https://github.com/signalfx/tracing-examples/tree/main/opentelemetry-tracing/opentelemetry-python-tracing).\n\n### Basic Configuration\n\nThe service name resource attribute is the only configuration option\nthat needs to be specified. You can set it by adding a `service.name`\nattribute as shown in the [example above](#getting-started).\n\nA few other configuration options that may need to be changed or set are:\n\n- Trace propagation format if not sending to other applications using W3C\n  trace-context. For example, if other applications are instrumented with\n  `signalfx-*-tracing` instrumentation. See the [trace\n  propagation](docs/advanced-config.md#trace-propagation-configuration)\n  configuration documentation for more information.\n- Endpoint if not sending to a locally running Splunk OpenTelemetry Connector\n  with default configuration. For example, if the SignalFx Smart Agent is used.\n  See the [exporters](docs/advanced-config.md#trace-exporters) configuration\n  documentation for more information.\n- Environment resource attribute `deployment.environment` to specify what\n  environment the span originated from. For example:\n  ```\n  OTEL_RESOURCE_ATTRIBUTES=deployment.environment=production\n  ```\n- Service version resource attribute `service.version` to specify the version\n  of your instrumented application. For example:\n  ```\n  OTEL_RESOURCE_ATTRIBUTES=service.version=1.2.3\n  ```\n\nThe `deployment.environment` and `service.version` resource attributes are not\nstrictly required, but recommended to be set if they are\navailable.\n\nThe `OTEL_RESOURCE_ATTRIBUTES` syntax is described in detail in the\n[trace configuration](docs/advanced-config.md#trace-configuration) section.\n\n### Supported Python Versions\n\nThe instrumentation works with Python verion 3.6 and higher. Supported\nlibraries are listed\n[here](https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation).\n\n## Advanced Configuration\n\nFor the majority of users, the [Getting Started](#getting-started) section is\nall you need. Advanced configuration documentation can be found\n[here](docs/advanced-config.md). In addition, special cases for instrumentation\nare documented [here](docs/instrumentation-special-cases.md).\n\n## Manually instrument an application\n\nDocumentation on how to manually instrument a Python application is available\n[here](https://opentelemetry-python.readthedocs.io/en/stable/getting-started.html).\n\nTo extend the instrumentation with the OpenTelemetry Instrumentation for Python,\nyou have to use a compatible API version.\n\nThe Splunk Distribution of OpenTelemetry Python version <span class="splunk-version">1.0.0rc4</span> is compatible\nwith:\n\n* OpenTelemetry API version <span class="otel-api-version">1.4.1</span>\n* OpenTelemetry SDK version <span class="otel-sdk-version">1.4.1</span>\n* OpenTelemetry Instrumentation for Python version <span class="otel-instrumentation-version">0.23b2</span>\n\n## Correlating traces with logs\n\nThe Splunk Distribution of OpenTelemetry Python provides a way\nto correlate traces with logs. It is enabled automatically as part of the\n[logging\ninstrumentation](https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/logging/logging.html).\n\n# License and versioning\n\nThe Splunk distribution of OpenTelemetry Python Instrumentation is a\ndistribution of the [OpenTelemetry Python\nproject](https://github.com/open-telemetry/opentelemetry-python). It is\nreleased under the terms of the Apache Software License version 2.0. See [the\nlicense file](./LICENSE) for more details.\n',
    'author': 'Splunk',
    'author_email': 'splunk-oss@splunk.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
