# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pulpcore.client.pulp_ansible
from pulpcore.client.pulp_ansible.models.paginated_collection_version_response_list import PaginatedCollectionVersionResponseList  # noqa: E501
from pulpcore.client.pulp_ansible.rest import ApiException

class TestPaginatedCollectionVersionResponseList(unittest.TestCase):
    """PaginatedCollectionVersionResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedCollectionVersionResponseList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_ansible.models.paginated_collection_version_response_list.PaginatedCollectionVersionResponseList()  # noqa: E501
        if include_optional :
            return PaginatedCollectionVersionResponseList(
                meta = pulpcore.client.pulp_ansible.models.paginated_collection_response_list_meta.PaginatedCollectionResponseList_meta(
                    count = 123, ), 
                links = pulpcore.client.pulp_ansible.models.paginated_collection_response_list_links.PaginatedCollectionResponseList_links(
                    first = '0', 
                    previous = '0', 
                    next = '0', 
                    last = '0', ), 
                data = [
                    pulpcore.client.pulp_ansible.models.collection_version_response.CollectionVersionResponse(
                        version = '0', 
                        href = '0', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        requires_ansible = '0', 
                        artifact = null, 
                        collection = null, 
                        download_url = '0', 
                        name = '0', 
                        namespace = null, 
                        metadata = null, 
                        manifest = pulpcore.client.pulp_ansible.models.manifest.manifest(), 
                        files = pulpcore.client.pulp_ansible.models.files.files(), )
                    ]
            )
        else :
            return PaginatedCollectionVersionResponseList(
        )

    def testPaginatedCollectionVersionResponseList(self):
        """Test PaginatedCollectionVersionResponseList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
