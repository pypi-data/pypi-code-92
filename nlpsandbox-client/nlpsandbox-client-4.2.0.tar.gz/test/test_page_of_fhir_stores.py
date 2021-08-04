"""
    NLP Sandbox Data Node API

    # Overview  The NLP Sandbox Data Node is a repository of data used to benchmark NLP Tools like the NLP Sandbox Date Annotator and Person Name Annotator.  The resources that can be stored in this Data Node and the operations supported are listed below:  - Create and manage datasets - Create and manage FHIR stores   - Store and retrieve FHIR patient profiles   - Store and retrieve clinical   notes - Create and manage annotation stores   - Store and retrieve text annotations   # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import nlpsandbox
from nlpsandbox.model.fhir_store import FhirStore
from nlpsandbox.model.page_limit import PageLimit
from nlpsandbox.model.page_offset import PageOffset
from nlpsandbox.model.response_page_metadata import ResponsePageMetadata
from nlpsandbox.model.response_page_metadata_links import ResponsePageMetadataLinks
from nlpsandbox.models import FhirStoreName
globals()['FhirStore'] = FhirStore
globals()['PageLimit'] = PageLimit
globals()['PageOffset'] = PageOffset
globals()['ResponsePageMetadata'] = ResponsePageMetadata
globals()['ResponsePageMetadataLinks'] = ResponsePageMetadataLinks
from nlpsandbox.model.page_of_fhir_stores import PageOfFhirStores


class TestPageOfFhirStores(unittest.TestCase):
    """PageOfFhirStores unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPageOfFhirStores(self):
        """Test PageOfFhirStores"""
        PageOfFhirStores(
            offset=PageOffset(10),
            limit=PageLimit(10),
            links=ResponsePageMetadataLinks(next="next"),
            total_results=30,
            fhir_stores=[FhirStore(name=FhirStoreName("foo"))]
        )


if __name__ == '__main__':
    unittest.main()
