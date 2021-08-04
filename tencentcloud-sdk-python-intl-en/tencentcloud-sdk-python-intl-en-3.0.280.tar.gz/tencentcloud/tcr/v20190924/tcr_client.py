# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.tcr.v20190924 import models


class TcrClient(AbstractClient):
    _apiVersion = '2019-09-24'
    _endpoint = 'tcr.tencentcloudapi.com'
    _service = 'tcr'


    def CheckInstance(self, request):
        """This API is used to verify the information of the Enterprise Edition instance.

        :param request: Request instance for CheckInstance.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CheckInstanceRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CheckInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateImmutableTagRules(self, request):
        """This API is used to create the tag immutability rule.

        :param request: Request instance for CreateImmutableTagRules.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateImmutableTagRulesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateImmutableTagRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateImmutableTagRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateImmutableTagRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateMultipleSecurityPolicy(self, request):
        """This API is used to create multiple public network access allowlist policies of the TCR instance.

        :param request: Request instance for CreateMultipleSecurityPolicy.
        :type request: :class:`tencentcloud.tcr.v20190924.models.CreateMultipleSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.CreateMultipleSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMultipleSecurityPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMultipleSecurityPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteImmutableTagRules(self, request):
        """This API is used to delete the tag immutability rule.

        :param request: Request instance for DeleteImmutableTagRules.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteImmutableTagRulesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteImmutableTagRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteImmutableTagRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteImmutableTagRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteMultipleSecurityPolicy(self, request):
        """This API is used to delete multiple public network access allowlist policies of the instance.

        :param request: Request instance for DeleteMultipleSecurityPolicy.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DeleteMultipleSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DeleteMultipleSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMultipleSecurityPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMultipleSecurityPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImmutableTagRules(self, request):
        """This API is used to list the tag immutability rule.

        :param request: Request instance for DescribeImmutableTagRules.
        :type request: :class:`tencentcloud.tcr.v20190924.models.DescribeImmutableTagRulesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.DescribeImmutableTagRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImmutableTagRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImmutableTagRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyImmutableTagRules(self, request):
        """This API is used to update the tag immutability rule.

        :param request: Request instance for ModifyImmutableTagRules.
        :type request: :class:`tencentcloud.tcr.v20190924.models.ModifyImmutableTagRulesRequest`
        :rtype: :class:`tencentcloud.tcr.v20190924.models.ModifyImmutableTagRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyImmutableTagRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyImmutableTagRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)