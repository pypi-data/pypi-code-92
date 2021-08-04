"""
    NLP Sandbox Date Annotator API

    # Overview The OpenAPI specification implemented by NLP Sandbox Annotators.   # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import unittest
from unittest.mock import patch

import nlpsandbox
from nlpsandbox.api.tool_api import ToolApi  # noqa: E501


class TestToolApi(unittest.TestCase):
    """ToolApi unit test stubs"""

    def setUp(self):
        self.api = ToolApi()  # noqa: E501
        self.patcher = patch('nlpsandbox.api_client.ApiClient.call_api')
        self.mock_foo = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_get_tool(self):
        """Test case for get_tool

        Get tool information  # noqa: E501
        """
        self.api.get_tool()

    def test_get_tool_dependencies(self):
        """Test case for get_tool_dependencies

        Get tool dependencies  # noqa: E501
        """
        self.api.get_tool_dependencies()


if __name__ == '__main__':
    unittest.main()
