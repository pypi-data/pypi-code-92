﻿# -*- coding: utf-8 -*-
"""
:Author: HuangJingCan
:Date: 2020-04-16 14:38:22
:LastEditTime: 2021-07-27 15:47:12
:LastEditors: HuangJingCan
:Description: 潮玩盲盒基础路由
"""
# 框架引用
from seven_framework.web_tornado.monitor import MonitorHandler
from seven_cloudapp.handlers.core import *
from seven_cloudapp.handlers.server import *
from seven_cloudapp.handlers.client import *

from seven_cloudapp_ppmt.handlers.server import *
from seven_cloudapp_ppmt.handlers.client import *


def seven_cloudapp_ppmt_route():
    return [
        (r"/monitor", MonitorHandler),
        (r"/", IndexHandler),
        # 千牛端接口
        (r"/server/saas_custom", base_s.SaasCustomHandler),
        (r"/server/login", user_s.LoginHandler),
        (r"/server/gear_log", user_s.GearLogHandler),
        (r"/server/user_list", user_s.UserListHandler),
        (r"/server/gear_value", user_s.GearValueHandler),
        (r"/server/user_status", user_s.UserStatusHandler),
        (r"/server/user_machine_list", user_s.UserMachineListHandler),
        (r"/server/pay_order_list", order_s.PayOrderListHandler),
        (r"/server/prize_order_list", order_s.PrizeOrderListHandler),
        (r"/server/prize_roster_list", order_s.PrizeRosterListHandler),
        (r"/server/prize_order_status", order_s.PrizeOrderStatusHandler),
        (r"/server/prize_order_remarks", order_s.PrizeOrderRemarksHandler),
        (r"/server/app_info", app_s.AppInfoHandler),
        (r"/server/base_info", app_s.BaseInfoHandler),
        (r"/server/telephone", app_s.TelephoneHandler),
        (r"/server/app_update", app_s.AppUpdateHandler),
        (r"/server/act", act_s.ActHandler),
        (r"/server/act_del", act_s.ActDelHandler),
        (r"/server/act_info", act_s.ActInfoHandler),
        (r"/server/act_save", act_s.ActSaveHandler),
        (r"/server/act_list", act_s.ActListHandler),
        (r"/server/act_create", act_s.ActCreateHandler),
        (r"/server/act_type", act_s.ActTypeListHandler),
        (r"/server/act_qrcode", act_s.ActQrCodeHandler),
        (r"/server/act_review", act_s.ActReviewHandler),
        (r"/server/next_progress", act_s.NextProgressHandler),
        (r"/server/theme_update", theme_s.ThemeUpdate),
        (r"/server/skin_list", theme_s.SkinListHandler),
        (r"/server/theme_list", theme_s.ThemeListHandler),
        (r"/server/machine", machine_s.MachineHandler),
        (r"/server/machine_del", machine_s.MachineDelHandler),
        (r"/server/machine_list", machine_s.MachineListHandler),
        (r"/server/machine_release", machine_s.MachineReleaseHandler),
        (r"/server/update_machineprice_by_gearid", machine_s.UpdateMachinePriceByGearIdHandler),
        (r"/server/goods_list", goods_s.GoodsListHandler),
        (r"/server/goods_info", goods_s.GoodsInfoHandler),
        (r"/server/goods_check", goods_s.GoodsCheckHandler),
        (r"/server/get_goods_list", goods_s.GoodsListByGoodsIDHandler),
        (r"/server/prize", prize_s.PrizeHandler),
        (r"/server/prize_del", prize_s.PrizeDelHandler),
        (r"/server/prize_list", prize_s.PrizeListHandler),
        (r"/server/prize_release", prize_s.PrizeReleaseHandler),
        (r"/server/prize_order_import", order_s.PrizeOrderImportHandler),
        (r"/server/prize_order_export", order_s.PrizeOrderExportHandler),
        (r"/server/prize_roster_export", order_s.PrizeRosterListExportHandler),
        (r"/server/report_info", report_s.ReportInfoHandler),
        (r"/server/report_list2", report_s.ReportInfoListHandler),
        (r"/server/send_sms", sms_s.SendSmsHandler),
        (r"/server/series", series_s.SeriesHandler),
        (r"/server/series_del", series_s.SeriesDelHandler),
        (r"/server/series_list", series_s.SeriesListHandler),
        (r"/server/series_release", series_s.SeriesReleaseHandler),
        (r"/server/price", price_s.PriceHandler),
        (r"/server/price_list", price_s.PriceListHandler),
        (r"/server/price_status", price_s.PriceStatusHandler),
        (r"/server/price_list_recover", price_s.PriceListRecoverHandler),
        (r"/server/throw_goods_list", throw_s.ThrowGoodsListHandler),
        (r"/server/async_throw_goods", throw_s.AsyncThrowGoodsHandler),
        (r"/server/init_throw_goods_list", throw_s.InitThrowGoodsListHandler),
        (r"/server/save_throw_goods_status", throw_s.SaveThrowGoodsStatusHandler),
        (r"/server/init_throw_goods_callback", throw_s.InitThrowGoodsCallBackHandler),
        # 2.0
        (r"/server/get_power_menu", power_s.GetPowerMenuHandler),
        (r"/server/task", task_s.TaskSaveHandler),
        (r"/server/task_list", task_s.TaskListHandler),
        (r"/server/exchange", exchange_s.ExchangeSaveHandler),
        (r"/server/exchange_list", exchange_s.ExchangeListHandler),
        (r"/server/check_buy_endbox", machine_s.CheckBuyEndboxHandler),
        (r"/server/endbox_order_list", order_s.EndBoxOrderListHandler),
        (r"/server/prop", user_s.PropHandler),
        (r"/server/prop_log_list", user_s.PropLogHandler),
        (r"/server/user_detail", user_s.UserDetailHandler),
        (r"/server/integral", user_s.SurplusIntegralHandler),
        (r"/server/lottery_value_log_list", user_s.LotteryValueLogHandler),
        # 2.1优化
        (r"/server/checking_price_gear", machine_s.CheckingPriceGearHandler),  #验证价格档位

        # 客户端接口
        (r"/client/login", user.LoginHandler),
        (r"/client/user", user.UserHandler),
        (r"/client/sync_pay_order", user.SyncPayOrderHandler),
        (r"/client/getunpacknum", user.GetUnpackNumHandler),
        (r"/client/user_prize_order", user.PrizeOrderHandler),
        (r"/client/user_prize_order_series", user.PrizeOrderBySeriesHandler),
        (r"/client/gear_list_num", user.GetNumByPriceGearsListHandler),
        (r"/client/get_horseracelamp_List", user.GetHorseRaceLampListHandler),
        (r"/client/act_info", act.ActInfoHandler),
        (r"/client/machine_list", act.MachineListHandler),
        (r"/client/prize_list", act.PrizeListHandler),
        (r"/client/theme_info", theme.ThemeInfoHandler),
        (r"/client/theme", theme.ThemeSaveHandler),
        (r"/client/skin", theme.SkinSaveHandler),
        (r"/client/lottery", lottery.LotteryHandler),
        (r"/client/shakeit", lottery.ShakeItHandler),
        (r"/client/recover", lottery.RecoverHandler),
        (r"/client/shakeit_prize_list", lottery.ShakeItPrizeListHandler),
        (r"/client/all_prize_list", prize.AllPrizeListHandler),
        (r"/client/user_prize_list", prize.UserPrizeListHandler),
        (r"/client/address", address.GetAddressInfoHandler),
        (r"/client/get_app_expire", app.GetAppExpireHandler),
        (r"/client/series_list", series.SeriesListHandler),
        # 2.0
        (r"/client/get_power_menu", power.GetPowerMenuHandler),
        (r"/client/task_share", task.ShareHandler),
        (r"/client/task_follow", task.FollowHandler),
        (r"/client/task_list", task.TaskListHandler),
        (r"/client/task_inivite", task.InviteHandler),
        (r"/client/task_collect", task.CollectGoodsHandler),
        (r"/client/task_weekly_sign", task.WeeklySignHandler),
        (r"/client/task_inivite_reward", task.InviteRewardHandler),
        (r"/client/exchange", exchange.ExchangeHandler),
        (r"/client/exchange_list", exchange.ExchangeListHandler),
        (r"/client/user_detail", user.GetUserDetailHandler),
        (r"/client/integral_list", user.GetIntegralListHandler),
        (r"/client/lottery_all", lottery.LotteryAllHandler),
        (r"/client/use_reset_card", lottery.UseResetCardHandler),
        (r"/client/use_perspective_card", lottery.UsePerspectiveCardHandler),
        (r"/client/active_new_user", task.ActiveNewUserHandler),
    ]