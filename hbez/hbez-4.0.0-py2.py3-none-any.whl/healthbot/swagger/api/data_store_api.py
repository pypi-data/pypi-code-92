# coding: utf-8

"""
    Paragon Insights APIs

    API interface for PI application  # noqa: E501

    OpenAPI spec version: 4.0.0
    Contact: healthbot-feedback@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from jnpr.healthbot.swagger.api_client import ApiClient


class DataStoreApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_data_store(self, key, data, group_name, **kwargs):  # noqa: E501
        """Create dashboard details.  # noqa: E501

        Store data-store details in database for the requested group name and key.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_data_store(key, data, group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str key: Key of data_store object (required)
        :param DatastoreSchema data: Value of data_store object (required)
        :param str group_name: Group name (required)
        :param str x_iam_token: authentication header object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_data_store_with_http_info(key, data, group_name, **kwargs)  # noqa: E501
        else:
            (data) = self.create_data_store_with_http_info(key, data, group_name, **kwargs)  # noqa: E501
            return data

    def create_data_store_with_http_info(self, key, data, group_name, **kwargs):  # noqa: E501
        """Create dashboard details.  # noqa: E501

        Store data-store details in database for the requested group name and key.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_data_store_with_http_info(key, data, group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str key: Key of data_store object (required)
        :param DatastoreSchema data: Value of data_store object (required)
        :param str group_name: Group name (required)
        :param str x_iam_token: authentication header object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key', 'data', 'group_name', 'x_iam_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_data_store" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key' is set
        if ('key' not in params or
                params['key'] is None):
            raise ValueError("Missing the required parameter `key` when calling `create_data_store`")  # noqa: E501
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `create_data_store`")  # noqa: E501
        # verify the required parameter 'group_name' is set
        if ('group_name' not in params or
                params['group_name'] is None):
            raise ValueError("Missing the required parameter `group_name` when calling `create_data_store`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_name' in params:
            path_params['group_name'] = params['group_name']  # noqa: E501

        query_params = []
        if 'key' in params:
            query_params.append(('key', params['key']))  # noqa: E501

        header_params = {}
        if 'x_iam_token' in params:
            header_params['x-iam-token'] = params['x_iam_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/config/data-store/{group_name}/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_data_store(self, group_name, **kwargs):  # noqa: E501
        """Delete dashboard details.  # noqa: E501

        Delete data_store details for the given group-name, or as per the keys passed in query.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_data_store(group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_name: Group name (required)
        :param str x_iam_token: authentication header object
        :param list[str] key: ID of dashboard
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_data_store_with_http_info(group_name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_data_store_with_http_info(group_name, **kwargs)  # noqa: E501
            return data

    def delete_data_store_with_http_info(self, group_name, **kwargs):  # noqa: E501
        """Delete dashboard details.  # noqa: E501

        Delete data_store details for the given group-name, or as per the keys passed in query.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_data_store_with_http_info(group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_name: Group name (required)
        :param str x_iam_token: authentication header object
        :param list[str] key: ID of dashboard
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_name', 'x_iam_token', 'key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_data_store" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_name' is set
        if ('group_name' not in params or
                params['group_name'] is None):
            raise ValueError("Missing the required parameter `group_name` when calling `delete_data_store`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_name' in params:
            path_params['group_name'] = params['group_name']  # noqa: E501

        query_params = []
        if 'key' in params:
            query_params.append(('key', params['key']))  # noqa: E501
            collection_formats['key'] = 'csv'  # noqa: E501

        header_params = {}
        if 'x_iam_token' in params:
            header_params['x-iam-token'] = params['x_iam_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/config/data-store/{group_name}/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_data_store(self, group_name, **kwargs):  # noqa: E501
        """Delete dashboard details.  # noqa: E501

        Retrieve data_store details for the given group-name, or as per the keys passed in query.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_data_store(group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_name: Group name (required)
        :param str x_iam_token: authentication header object
        :param list[str] key: Key of data_store object
        :return: DatastoreSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_data_store_with_http_info(group_name, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_data_store_with_http_info(group_name, **kwargs)  # noqa: E501
            return data

    def retrieve_data_store_with_http_info(self, group_name, **kwargs):  # noqa: E501
        """Delete dashboard details.  # noqa: E501

        Retrieve data_store details for the given group-name, or as per the keys passed in query.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_data_store_with_http_info(group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_name: Group name (required)
        :param str x_iam_token: authentication header object
        :param list[str] key: Key of data_store object
        :return: DatastoreSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_name', 'x_iam_token', 'key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_data_store" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_name' is set
        if ('group_name' not in params or
                params['group_name'] is None):
            raise ValueError("Missing the required parameter `group_name` when calling `retrieve_data_store`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_name' in params:
            path_params['group_name'] = params['group_name']  # noqa: E501

        query_params = []
        if 'key' in params:
            query_params.append(('key', params['key']))  # noqa: E501
            collection_formats['key'] = 'csv'  # noqa: E501

        header_params = {}
        if 'x_iam_token' in params:
            header_params['x-iam-token'] = params['x_iam_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/config/data-store/{group_name}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DatastoreSchema',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_data_store(self, key, data, group_name, **kwargs):  # noqa: E501
        """Update data_store details.  # noqa: E501

        Update data-store details in database for the requested group name and key.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_data_store(key, data, group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str key: key of data_store (required)
        :param DatastoreSchema data: value of data_store object (required)
        :param str group_name: Group name (required)
        :param str x_iam_token: authentication header object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_data_store_with_http_info(key, data, group_name, **kwargs)  # noqa: E501
        else:
            (data) = self.update_data_store_with_http_info(key, data, group_name, **kwargs)  # noqa: E501
            return data

    def update_data_store_with_http_info(self, key, data, group_name, **kwargs):  # noqa: E501
        """Update data_store details.  # noqa: E501

        Update data-store details in database for the requested group name and key.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_data_store_with_http_info(key, data, group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str key: key of data_store (required)
        :param DatastoreSchema data: value of data_store object (required)
        :param str group_name: Group name (required)
        :param str x_iam_token: authentication header object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key', 'data', 'group_name', 'x_iam_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_data_store" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key' is set
        if ('key' not in params or
                params['key'] is None):
            raise ValueError("Missing the required parameter `key` when calling `update_data_store`")  # noqa: E501
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `update_data_store`")  # noqa: E501
        # verify the required parameter 'group_name' is set
        if ('group_name' not in params or
                params['group_name'] is None):
            raise ValueError("Missing the required parameter `group_name` when calling `update_data_store`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_name' in params:
            path_params['group_name'] = params['group_name']  # noqa: E501

        query_params = []
        if 'key' in params:
            query_params.append(('key', params['key']))  # noqa: E501

        header_params = {}
        if 'x_iam_token' in params:
            header_params['x-iam-token'] = params['x_iam_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/config/data-store/{group_name}/', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
