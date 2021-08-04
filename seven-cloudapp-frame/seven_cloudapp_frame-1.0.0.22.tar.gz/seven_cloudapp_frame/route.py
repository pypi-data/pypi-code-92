﻿# -*- coding: utf-8 -*-
"""
:Author: HuangJianYi
:Date: 2020-04-16 14:38:22
@LastEditTime: 2021-08-04 17:48:17
@LastEditors: HuangJianYi
:Description: 基础路由
"""
# 框架引用
from seven_framework.web_tornado.monitor import MonitorHandler
from seven_cloudapp_frame.handlers.core import *
from seven_cloudapp_frame.handlers.server import *
from seven_cloudapp_frame.handlers.client import *

def seven_cloudapp_frame_route():
    return [
        (r"/monitor", MonitorHandler),
        (r"/", IndexHandler),
        #客户端
        (r"/client/address_list", address.AddressInfoListHandler),
        (r"/client/login", user.LoginHandler),
        (r"/client/authorize", user.AuthorizeHandler),
        (r"/client/apply_black_unbind", user.ApplyBlackUnbindHandler),
        (r"/client/user_asset_list", user.UserAssetListHandler),
        (r"/client/asset_log_list", user.AssetLogListHandler),
        (r"/client/theme_info", theme.ThemeInfoHandler),
        (r"/client/save_theme", theme.SaveThemeHandler),
        (r"/client/save_skin", theme.SaveSkinHandler),
        (r"/client/theme_info_list", theme.ThemeInfoListHandler),
        (r"/client/skin_info_list", theme.SkinInfoListHandler),
        (r"/client/ip_info_list", ip.IpInfoListHandler),
        (r"/client/act_info", act.ActInfoHandler),
        (r"/client/app_expire", app.AppExpireHandler),
        (r"/client/submit_sku", goods.SubmitSkuHandler),
        (r"/client/sku_info", goods.SkuInfoHandler),
        (r"/client/goods_list", goods.GoodsListHandler),

        #千牛端
        (r"/server/saas_custom", base_s.SaasCustomHandler),
        (r"/server/login", user_s.LoginHandler),
        (r"/server/get_app_id", base_s.GetAppIDHandler),
        (r"/server/base_info", base_s.BaseInfoHandler),
        (r"/server/send_sms", base_s.SendSmsHandler),
        (r"/server/app_info", app_s.AppInfoHandler),
        (r"/server/instantiate", app_s.InstantiateAppHandler),
        (r"/server/version_upgrade", app_s.VersionUpgradeHandler),
        (r"/server/update_telephone", app_s.UpdateTelephoneHandler),
        (r"/server/act_type_list", act_s.ActTypeListHandler),
        (r"/server/next_progress", act_s.NextProgressHandler),
        (r"/server/add_act_info", act_s.AddActInfoHandler),
        (r"/server/update_act_info", act_s.UpdateActInfoHandler),
        (r"/server/act_info_list", act_s.ActInfoListHandler),
        (r"/server/act_info", act_s.ActInfoHandler),
        (r"/server/delete_act_info", act_s.DeleteActInfoHandler),
        (r"/server/review_act_info", act_s.ReviewActInfoHandler),
        (r"/server/release_act_info", act_s.ReleaseActInfoHandler),
        (r"/server/create_act_qrcode", act_s.CreateActQrCodeHandler),
        (r"/server/save_act_module", module_s.SaveActModuleHandler),
        (r"/server/act_info_list", module_s.ActModuleListHandler),
        (r"/server/act_module", module_s.ActModuleHandler),
        (r"/server/delete_act_module", module_s.DeleteActModuleHandler),
        (r"/server/review_act_module", module_s.ReviewActModuleHandler),
        (r"/server/release_act_module", module_s.ReleaseActModuleHandler),
        (r"/server/stat_report_list", report_s.StatReportListHandler),
        (r"/server/trend_report_list", report_s.TrendReportListHandler),
        (r"/server/update_user_status", user_s.UpdateUserStatusHandler),
        (r"/server/update_user_status_by_black", user_s.UpdateUserStatusByBlackHandler),
        (r"/server/audit_user_black", user_s.AuditUserBlackHandler),
        (r"/server/user_black_list", user_s.UserBlackListHandler),
        (r"/server/update_user_asset", user_s.UpdateUserAssetHandler),
        (r"/server/asset_log_list", user_s.AssetLogListHandler),
        (r"/server/init_launch_goods", launch_s.InitLaunchGoodsHandler),
        (r"/server/async_launch_goods", launch_s.AsyncLaunchGoodsHandler),
        (r"/server/launch_goods_list", launch_s.LaunchGoodsListHandler),
        (r"/server/update_launch_goods_status", launch_s.UpdateLaunchGoodsStatusHandler),
        (r"/server/init_launch_goods_callback", launch_s.InitLaunchGoodsCallBackHandler),
        (r"/server/update_theme", theme_s.UpdateThemeHandler),
        (r"/server/theme_info_list", theme_s.ThemeInfoListHandler),
        (r"/server/skin_info_list", theme_s.SkinInfoListHandler),
        (r"/server/save_ip_info", ip_s.SaveIpInfoHandler),
        (r"/server/delete_ip_info", ip_s.DeleteIpInfoHandler),
        (r"/server/ip_info_list", ip_s.IpInfoListHandler),
        (r"/server/release_ip_info", ip_s.ReleaseIpInfoHandler),
        (r"/server/save_price_gear", price_s.SavePriceGearHandler),
        (r"/server/price_gear_list", price_s.PriceGearListHandler),
        (r"/server/update_price_gear_status", price_s.UpdatePriceGearStatusHandler),
        (r"/server/check_price_gear", price_s.CheckPriceGearHandler),
        (r"/server/goods_list", goods_s.GoodsListHandler),
        (r"/server/goods_list_by_goodsids", goods_s.GoodsListByGoodsIDHandler),
        (r"/server/goods_info", goods_s.GoodsInfoHandler),
        (r"/server/benefit_detail", goods_s.BenefitDetailHandler),
    ]