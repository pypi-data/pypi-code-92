# -*- coding: utf-8 -*-
"""
@Author: HuangJianYi
@Date: 2021-08-02 09:03:41
@LastEditTime: 2021-08-04 12:02:59
@LastEditors: HuangJianYi
@Description: 主题皮肤
"""

from seven_cloudapp_frame.handlers.frame_base import *
from seven_cloudapp_frame.models.theme_base_model import *
from seven_cloudapp_frame.models.db_models.theme.theme_info_model import *
from seven_cloudapp_frame.models.db_models.skin.skin_info_model import *
from seven_cloudapp_frame.models.db_models.act.act_info_model import *
from seven_cloudapp_frame.models.db_models.act.act_module_model import *


class ThemeInfoListHandler(TaoBaseHandler):
    """
    :description: 主题列表
    """
    def get_async(self):
        """
        :description: 主题列表
        :param app_id：应用标识
        :return: 列表
        :last_editors: HuangJianYi
        """
        app_id = self.get_app_id()
        theme_base_model = ThemeBaseModel(context=self)
        self.reponse_json_success(theme_base_model.get_theme_list(app_id,is_cache=False))

class SkinInfoListHandler(TaoBaseHandler):
    """
    :description: 皮肤列表
    """
    @filter_check_params("theme_id")
    def get_async(self):
        """
        :description: 皮肤列表
        :param theme_id：主题标识
        :return: 列表
        :last_editors: HuangJianYi
        """
        theme_id = int(self.get_param("theme_id", 0))
        theme_base_model = ThemeBaseModel(context=self)
        self.reponse_json_success(theme_base_model.get_skin_list(theme_id,is_cache=False))

class UpdateThemeHandler(TaoBaseHandler):
    """
    :description: 更新活动主题和皮肤
    """
    @filter_check_params("act_id,theme_id")
    def get_async(self):
        """
        :description: 更新活动主题和皮肤
        :param act_id：活动标识
        :param theme_id：主题标识
        :return: 
        :last_editors: HuangJianYi
        """
        app_id = self.get_app_id()
        act_id = int(self.get_param("act_id", 0))
        theme_id = int(self.get_param("theme_id", 0))
        is_module = int(self.get_param("is_module", 1))

        theme_base_model = ThemeBaseModel(context=self)
        invoke_result_data = theme_base_model.update_act_theme_and_skin(app_id, act_id, theme_id, is_module)
        if invoke_result_data.success == False:
            return self.reponse_json_error(invoke_result_data.error_code, invoke_result_data.error_message)
        return self.reponse_json_success()