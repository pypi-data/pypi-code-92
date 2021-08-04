#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Mito.
# Distributed under the terms of the Modified BSD License.

"""
Information about the frontend package of the widgets.
"""

from pathlib import Path
import os
import json
from mitosheet._version import __version__, get_package_json

module_name = get_package_json()['name']
module_version = '^' + __version__
