#
# Copyright (c) 2020-2030 Translational Oncology at the Medical Center of the Johannes Gutenberg-University Mainz gGmbH.
#
# This file is part of Neofox
# (see https://github.com/tron-bioinformatics/neofox).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.#
import os
import unittest
from unittest import TestCase

import neofox
import neofox.tests.unit_tests.tools as test_tools
from neofox.exceptions import NeofoxConfigurationException
from neofox.references.references import ReferenceFolder
from neofox.tests.fake_classes import FakeReferenceFolder


class TestReferenceFolder(TestCase):
    def setUp(self):
        os.environ[neofox.REFERENCE_FOLDER_ENV] = "."
        self.fake_reference_folder = FakeReferenceFolder()

    def test_not_provided_reference(self):
        del os.environ[neofox.REFERENCE_FOLDER_ENV]
        with self.assertRaises(NeofoxConfigurationException):
            ReferenceFolder()

    def test_empty_string_reference(self):
        os.environ[neofox.REFERENCE_FOLDER_ENV] = ""
        with self.assertRaises(NeofoxConfigurationException):
            ReferenceFolder()

    def test_non_existing_reference(self):
        os.environ[neofox.REFERENCE_FOLDER_ENV] = "/non_existing_folder"
        with self.assertRaises(NeofoxConfigurationException):
            ReferenceFolder()

    def test_all_resources_exist(self):
        test_tools.mock_file_existence(
            existing_files=self.fake_reference_folder.resources
        )
        ReferenceFolder()

    def test_one_resource_do_not_exist(self):
        test_tools.mock_file_existence(
            existing_files=self.fake_reference_folder.resources[
                1 : len(self.fake_reference_folder.resources)
            ],
            non_existing_files=[self.fake_reference_folder.resources[0]],
        )
        with self.assertRaises(NeofoxConfigurationException):
            ReferenceFolder()


if __name__ == "__main__":
    unittest.main()
