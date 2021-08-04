# -*- coding: utf-8 -*-
"""
@Author: HuangJianYi
@Date: 2021-08-04 13:41:15
@LastEditTime: 2021-08-04 18:04:22
@LastEditors: HuangJianYi
@Description: 
"""
from seven_cloudapp_frame.models.db_models.tao import tao_coupon_model
from seven_cloudapp_frame.models.seven_model import *
from seven_cloudapp_frame.libs.customize.seven_helper import *
from seven_cloudapp_frame.models.db_models.act.act_prize_model import *
from seven_cloudapp_frame.models.db_models.tao.tao_coupon_model import *

class PrizeBaseModel():
    """
    :description: 奖品基类
    """
    def __init__(self, context):
        self.context = context

    def _delete_act_prize_dependency_key(self,act_id,prize_id):
        """
        :description: 删除活动奖品依赖建
        :param act_id: 活动标识
        :param prize_id: 奖品标识
        :return: 
        :last_editors: HuangJianYi
        """
        redis_init = SevenHelper.redis_init()
        if prize_id:
            redis_init.delete(f"act_prize:prizeid_{prize_id}")
        if act_id:
            redis_init.delete(f"act_prize_list:actid_{act_id}")
        
    def get_act_prize_dict(self,prize_id,is_cache=True):
        """
        :description: 获取活动模块
        :param prize_id: 奖品标识
        :param is_cache: 是否缓存
        :return: 返回活动奖品
        :last_editors: HuangJianYi
        """
        act_prize_model = ActPrizeModel(context=self.context)
        if is_cache:
            dependency_key = f"act_prize:prizeid_{prize_id}"
            act_prize_dict = act_prize_model.get_cache_dict_by_id(prize_id,dependency_key=dependency_key)
        else:
            act_prize_dict = act_prize_model.get_dict_by_id(prize_id)
        if not act_prize_dict or act_prize_dict["is_release"] == 0 or act_prize_dict["is_del"] == 1:
            return None
        return act_prize_dict

    def get_act_prize_list(self,app_id,act_id,prize_name,is_del,page_size,page_index,is_cache=True):
        """
        :description: 获取活动奖品列表
        :param app_id: 应用标识
        :param act_id: 活动标识
        :param prize_name: 奖品名称
        :param is_del: 是否回收站1是0否
        :param page_size: 条数
        :param page_index: 页数
        :param is_cache: 是否缓存
        :return: 
        :last_editors: HuangJianYi
        """
        order_by = "sort_index desc,id asc"
        condition = "app_id=%s and act_id=%s"
        params = [app_id,act_id]
        if is_del !=-1:
            condition += " and is_del=%s"
            params.append(is_del)
        if prize_name:
            condition += " and prize_name=%s"
            params.append(prize_name)
        if is_cache:
            page_list, total = ActPrizeModel(context=self.context).get_cache_dict_page_list(dependency_key=f"act_module_list:actid_{act_id}",field="*", page_index=page_index, page_size=page_size, where=condition, group_by="", order_by=order_by, params=params)
        else:
            page_list, total = ActPrizeModel(context=self.context).get_dict_page_list(field="*", page_index=page_index, page_size=page_size, where=condition, group_by="", order_by=order_by, params=params)    
        return page_list, total

    def save_act_prize(self,app_id,act_id,module_id,prize_id,prize_name,prize_title,prize_pic,prize_detail_json,goods_id,goods_code,goods_code_list,goods_type,prize_type,prize_price,probability,chance,prize_limit,is_prize_notice,prize_total,is_surplus,lottery_type,tag_name,tag_id,is_sku,sku_json,sort_index,is_release,ascription_type=0,i1=0,i2=0,i3=0,i4=0,i5=0,s1='',s2='',s3='',s4='',s5='',d1='',d2=''):
        """
        :description: 添加活动模块信息
        :param app_id: 应用标识
        :param act_id: 活动标识
        :param module_id: 活动模块标识
        :param prize_id: 奖品标识
        :param prize_name: 奖品名称
        :param prize_title: 奖品子标题
        :param prize_pic: 奖品图
        :param prize_detail_json: 奖品详情图（json）
        :param goods_id: 商品id
        :param goods_code: 商品编码
        :param goods_code_list: 多个sku商品编码
        :param goods_type: 物品类型（1虚拟2实物）
        :param prize_type: 奖品类型(1现货2优惠券3红包4参与奖、谢谢参与5预售)
        :param prize_price: 奖品价值
        :param probability: 奖品权重
        :param chance: 概率
        :param prize_limit: 中奖限制数
        :param is_prize_notice: 是否显示跑马灯(1是0否)
        :param prize_total: 奖品总数
        :param is_surplus: 是否显示奖品库存（1显示0-不显示）
        :param lottery_type: 出奖类型（1概率出奖 2强制概率）
        :param tag_name: 标签名称(奖项名称)
        :param tag_id: 标签ID(奖项标识)
        :param is_sku: 是否有SKU
        :param sku_json: sku详情json
        :param sort_index: 排序
        :param is_release: 是否发布（1是0否）
        :param ascription_type: 奖品归属类型（0-活动奖品1-任务奖品）
        :param i1: i1
        :param i2: i2
        :param i3: i3
        :param i4: i4
        :param i5: i5
        :param s1: s1
        :param s2: s2
        :param s3: s3
        :param s4: s4
        :param s5: s5
        :param d1: d1
        :param d2: d2
        :return: 
        :last_editors: HuangJianYi
        """
        invoke_result_data = InvokeResultData()
        if not app_id or (not module_id and not act_id):
            invoke_result_data.success = False
            invoke_result_data.error_code = "param_error"
            invoke_result_data.error_message = "参数不能为空或等于0"
            return invoke_result_data
        
        is_add = False
        old_act_prize = None
        now_datetime = SevenHelper.get_now_datetime()
        act_prize_model = ActPrizeModel(context=self.context)
    
        if prize_id > 0:
            act_prize = act_prize_model.get_entity_by_id(prize_id)
            if not act_prize or act_prize.app_id != app_id:
                invoke_result_data.success = False
                invoke_result_data.error_code = "error"
                invoke_result_data.error_message = "活动奖品信息不存在"
                return invoke_result_data
            old_act_prize = deepcopy(act_prize)
        if not act_prize:
            is_add = True
            act_prize = ActPrize()

        act_prize.app_id = app_id
        act_prize.act_id = act_id
        act_prize.module_id = module_id
        act_prize.ascription_type = ascription_type
        act_prize.prize_name = prize_name
        act_prize.prize_title = prize_title
        act_prize.prize_pic = prize_pic
        act_prize.prize_detail_json = prize_detail_json if prize_detail_json else []
        act_prize.goods_id = goods_id
        act_prize.goods_code = goods_code
        act_prize.goods_code_list = goods_code_list
        act_prize.goods_type = goods_type
        act_prize.prize_type = prize_type
        act_prize.probability = probability
        act_prize.chance = chance
        act_prize.prize_limit = prize_limit
        act_prize.is_prize_notice = is_prize_notice
        act_prize.is_surplus = is_surplus
        act_prize.prize_total = prize_total
        act_prize.lottery_type = lottery_type
        act_prize.tag_name = tag_name
        act_prize.tag_id = tag_id
        act_prize.is_sku = is_sku
        act_prize.sku_json = sku_json if sku_json else {}
        act_prize.sort_index = sort_index
        act_prize.is_release = is_release
        act_prize.i1 = i1
        act_prize.i2 = i2
        act_prize.i3 = i3
        act_prize.i4 = i4
        act_prize.i5 = i5
        act_prize.s1 = s1
        act_prize.s2 = s2
        act_prize.s3 = s3
        act_prize.s4 = s4
        act_prize.s5 = s5
        act_prize.d1 = d1
        act_prize.d2 = d2
        act_prize.modify_date = now_datetime
        
        # 奖品类型为参与奖时
        prize_total = 9999 if prize_type == 4 else prize_total
        
        if is_add:
            act_prize.create_date = now_datetime
            act_prize.surplus = prize_total
            act_prize.prize_total = prize_total
            act_prize.id = act_prize_model.add_entity(act_prize)
        else:
            act_prize_model.update_entity(act_prize,exclude_field_list="app_id,act_id,module_id,prize_total,surplus,hand_out")
            operate_num = prize_total - act_prize.prize_total
            if operate_num != 0:
                act_prize_model.update_table(f"surplus=surplus+{operate_num},prize_total=prize_total+{operate_num}", "id=%s", act_prize.id)
            
        result = {}
        result["is_add"] = is_add
        result["new"] = act_prize
        result["old"] = old_act_prize
        invoke_result_data.data = result
        self._delete_act_prize_dependency_key(act_id,act_prize.id)
        return invoke_result_data
    
    def save_tao_coupon(self,app_id,act_id,prize_id,coupon_type,right_ename,pool_id,coupon_start_date,coupon_end_date):
        """
        :description: 添加奖品关联优惠券
        :param app_id: 应用标识
        :param act_id: 活动标识
        :param prize_id: 奖品标识
        :param coupon_type: 优惠券类型(0无1店铺优惠券2商品优惠券)
        :param right_ename: 发放的权益(奖品)唯一标识
        :param pool_id: 奖池ID
        :param coupon_start_date: 优惠券开始时间
        :param coupon_end_date: 优惠券结束时间
        :return: 
        :last_editors: HuangJianYi
        """
        invoke_result_data = InvokeResultData()
        tao_coupon = None
        tao_coupon_model = TaoCouponModel(context=self.context)
        if prize_id > 0:
            tao_coupon = tao_coupon_model.get_entity("act_id=%s and prize_id=%s",params=[act_id,prize_id])
        if not tao_coupon:
            tao_coupon = TaoCoupon()
        tao_coupon.app_id = app_id
        tao_coupon.act_id = act_id
        tao_coupon.coupon_type = coupon_type
        tao_coupon.right_ename = right_ename
        tao_coupon.pool_id = pool_id
        tao_coupon.coupon_start_date = coupon_start_date if coupon_start_date else "1900-01-01 00:00:00"
        tao_coupon.coupon_end_date = coupon_end_date if coupon_end_date else "2900-01-01 00:00:00"
        tao_coupon.modify_date = SevenHelper.get_now_datetime()
        tao_coupon_model.add_update_entity(tao_coupon)
        return invoke_result_data

    def delete_act_prize(self,app_id,prize_id,is_del):
        """
        :description: 删除或者还原活动奖品
        :param app_id：应用标识
        :param prize_id：奖品标识
        :param is_del：0-还原，1-删除
        :return: 
        :last_editors: HuangJianYi
        """
        invoke_result_data = InvokeResultData()
        act_prize_model = ActPrizeModel(context=self.context)
        act_prize_dict = act_prize_model.get_dict_by_id(prize_id)
        if not act_prize_dict or act_prize_dict["app_id"] != app_id:
            invoke_result_data.success = False
            invoke_result_data.error_code = "error"
            invoke_result_data.error_message = "活动奖品信息不存在"
            return invoke_result_data
        is_release = 0 if is_del == 1 else 1
        modify_date = self.get_now_datetime()
        invoke_result_data.success = act_prize_model.update_table("is_del=%s,is_release=%s,modify_date=%s", "id=%s", [is_del, is_release, modify_date, modify_date, prize_id])
        self._delete_act_prize_dependency_key(act_prize_dict.act_id,prize_id)
        return invoke_result_data
    
    def release_act_prize(self,app_id,prize_id,is_release):
        """
        :description: 活动奖品上下架
        :param app_id：应用标识
        :param prize_id：奖品标识
        :param is_release: 是否发布 1-是 0-否
        :return: 
        :last_editors: HuangJianYi
        """
        invoke_result_data = InvokeResultData()
        act_prize_model = ActPrizeModel(context=self.context)
        act_prize_dict = act_prize_model.get_dict_by_id(prize_id)
        if not act_prize_dict or act_prize_dict["app_id"] != app_id:
            invoke_result_data.success = False
            invoke_result_data.error_code = "error"
            invoke_result_data.error_message = "活动奖品不存在"
            return invoke_result_data
        invoke_result_data.success = act_prize_model.update_table("modify_date=%s,is_release=%s", "id=%s", [SevenHelper.get_now_datetime(), is_release, prize_id])
        self._delete_act_module_dependency_key(act_prize_dict.act_id,prize_id)
        return invoke_result_data