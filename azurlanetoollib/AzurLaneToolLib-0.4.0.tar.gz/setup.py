#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
THIS FILE IS PART OF AZUR LANE TOOL LIB BY MATT BELFAST BROWN
setup.py - The core part of the Azur Lane Tool.

Author: Matt Belfast Brown 
E-mail：thedayofthedo@gmail.com
Creat Date:2021-07-10
Version Date：2021-08-03
Version:0.4.0


THIS PROGRAM IS FREE FOR EVERYONE,IS LICENSED UNDER GPL-3.0
YOU SHOULD HAVE RECEIVED A COPY OF GPL-3.0 LICENSE.

Copyright (C) 2021  Matt Belfast Brown

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from setuptools import setup, find_packages

setup(
    name = "AzurLaneToolLib",
    version = "0.4.0",
    keywords = ("pip","azur_lane", "tool"),
    description = "Tools lib for Azur Lane which game powered by ManJiu Shanghai",
    long_description = "The lib of Azur Lane Tools",
    license = "GPL-3.0 LICENSE",

    url = "http://belfast.xiaopangkj.space/azur_lane/",
    author = "Matt Belfast Brown",
    author_email = "thedayofthedo@gmail.com",

    packages = find_packages(),
    py_modules = ['AzurLaneToolLib.__init__','AzurLaneToolLib.mode.mode_BlP_Cal','AzurLaneToolLib.mode.mode_EXP_Cal','AzurLaneToolLib.mode.mode_JKN_Com'],
    include_package_data = True,
    platforms = "any",
    zip_safe=True,
    install_requires = []
)
