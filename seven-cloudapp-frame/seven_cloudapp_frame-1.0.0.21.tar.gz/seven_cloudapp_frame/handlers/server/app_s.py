# -*- coding: utf-8 -*-
"""
@Author: HuangJianYi
@Date: 2021-08-03 10:43:58
@LastEditTime: 2021-08-03 14:53:46
@LastEditors: HuangJianYi
@Description: 
"""
from seven_cloudapp_frame.handlers.frame_base import *
from seven_cloudapp_frame.models.top_base_model import *
from seven_cloudapp_frame.models.app_base_model import *

class InstantiateAppHandler(TaoBaseHandler):
    """
    :description: 实例化小程序
    """
    def get_async(self):
        """
        :description: 实例化小程序
        :param app_id:应用标识
        :param user_nick:用户昵称
        :param access_token:access_token
        :param is_log：是否记录返回信息
        :return app_info
        :last_editors: HuangJianYi
        """
        app_id = self.get_app_id()
        user_nick = self.get_taobao_param().user_nick
        access_token = self.get_taobao_param().access_token
        is_log = bool(self.get_param("is_log",False))

        cache_key = f"instantiate:{user_nick}"
        if SevenHelper.is_continue_request(cache_key, 10000) == True:
            return self.reponse_json_error("error","操作太频繁,请10秒后再试")
        top_base_model = TopBaseModel(context=self)
        invoke_result_data = top_base_model.instantiate(app_id,user_nick,access_token,is_log)
        SevenHelper.redis_init().delete(cache_key)
        if invoke_result_data.success == False:
            return self.reponse_json_error(invoke_result_data.error_code, invoke_result_data.error_message,invoke_result_data.data)
        return self.reponse_json_success(invoke_result_data.data)


class UpdateTelephoneHandler(TaoBaseHandler):
    """
    :description: 更新手机号
    """
    @filter_check_params("telephone")
    def get_async(self):
        """
        :description: 更新手机号
        :param app_id:应用标识
        :param telephone：手机号
        :param check_code：验证码
        :return: 
        :last_editors: HuangJianYi
        """
        open_id = self.get_taobao_param().open_id
        app_id = self.get_app_id()
        telephone = self.get_param("telephone")
        check_code = self.get_param("check_code")
        modify_date = self.get_now_datetime()

        check_code_re = self.redis_init().get("user_" + open_id + "_bind_phone_code")
        if check_code_re == None:
            return self.reponse_json_error("error", "验证码已过期")
        check_code_re = str(check_code_re, 'utf-8')
        if check_code != check_code_re:
            return self.reponse_json_error("error", "验证码错误")
        AppInfoModel(context=self).update_table("app_telephone=%s,modify_date=%s", "app_id=%s", [telephone, modify_date, app_id])
        return self.reponse_json_success()


class VersionUpgradeHandler(TaoBaseHandler):
    """
    :description: 前端版本更新
    """
    @filter_check_params()
    def get_async(self):
        """
        :description: 前端版本更新
        :param app_id:应用标识
        :return: 
        :last_editors: HuangJianYi
        """
        app_id = self.get_app_id()
        client_template_id = config.get_value("client_template_id")
        test_client_ver = config.get_value("test_client_ver")
        access_token = self.get_taobao_param().access_token
        is_log = bool(self.get_param("is_log", False))

        base_info = BaseInfoModel(context=self).get_entity()
        client_ver = base_info.client_ver

        app_info = AppInfoModel(context=self).get_entity("app_id=%s", params=app_id)
        if not app_info:
            return self.reponse_json_error("no_app", "小程序不存在")
        #指定账号升级
        if test_client_ver and self.get_taobao_param().user_nick == config.get_value("test_user_nick"):
            client_ver = test_client_ver
        top_base_model = TopBaseModel(context=self)
        invoke_result_data = top_base_model.version_upgrade(app_id, client_template_id, client_ver, access_token, app_info, is_log)
        if invoke_result_data.success == False:
            return self.reponse_json_error(invoke_result_data.error_code, invoke_result_data.error_message)
        return self.reponse_json_success(invoke_result_data.data)


class AppInfoHandler(TaoBaseHandler):
    """
    :description: 获取小程序信息
    """
    @filter_check_params()
    def get_async(self):
        """
        :description: 获取小程序信息
        :return app_info
        :last_editors: HuangJianYi
        """
        app_base_model = AppBaseModel(context=self)
        invoke_result_data = app_base_model.get_app_info_result(self.get_taobao_param().user_nick, self.get_taobao_param().open_id, self.get_taobao_param().access_token)
        if invoke_result_data.success == False:
            return self.reponse_json_error(invoke_result_data.error_code, invoke_result_data.error_message)
        return self.reponse_json_success(invoke_result_data.data)