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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class Account(AbstractModel):
    """帐号列表信息数据。

    """

    def __init__(self):
        """
        :param Id: 唯一ID。
        :type Id: int
        :param Uuid: 云镜客户端唯一Uuid
        :type Uuid: str
        :param MachineIp: 主机内网IP。
        :type MachineIp: str
        :param MachineName: 主机名称。
        :type MachineName: str
        :param Username: 帐号名。
        :type Username: str
        :param Groups: 帐号所属组。
        :type Groups: str
        :param Privilege: 帐号类型。
<li>ORDINARY：普通帐号</li>
<li>SUPPER：超级管理员帐号</li>
        :type Privilege: str
        :param AccountCreateTime: 帐号创建时间。
        :type AccountCreateTime: str
        :param LastLoginTime: 帐号最后登录时间。
        :type LastLoginTime: str
        """
        self.Id = None
        self.Uuid = None
        self.MachineIp = None
        self.MachineName = None
        self.Username = None
        self.Groups = None
        self.Privilege = None
        self.AccountCreateTime = None
        self.LastLoginTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.Username = params.get("Username")
        self.Groups = params.get("Groups")
        self.Privilege = params.get("Privilege")
        self.AccountCreateTime = params.get("AccountCreateTime")
        self.LastLoginTime = params.get("LastLoginTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountStatistics(AbstractModel):
    """帐号统计数据。

    """

    def __init__(self):
        """
        :param Username: 用户名。
        :type Username: str
        :param MachineNum: 主机数量。
        :type MachineNum: int
        """
        self.Username = None
        self.MachineNum = None


    def _deserialize(self, params):
        self.Username = params.get("Username")
        self.MachineNum = params.get("MachineNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetFilters(AbstractModel):
    """容器安全
    描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等
    若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        """
        :param Name: 过滤键的名称。
        :type Name: str
        :param Values: 一个或者多个过滤值。
        :type Values: list of str
        :param ExactMatch: 是否模糊查询
        :type ExactMatch: bool
        """
        self.Name = None
        self.Values = None
        self.ExactMatch = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        self.ExactMatch = params.get("ExactMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssetKeyVal(AbstractModel):
    """key-val类型的通用数据结构

    """

    def __init__(self):
        """
        :param Key: 标签
        :type Key: str
        :param Value: 数量
        :type Value: int
        :param Desc: 描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        """
        self.Key = None
        self.Value = None
        self.Desc = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BashEvent(AbstractModel):
    """高危命令数据

    """

    def __init__(self):
        """
        :param Id: 数据ID
        :type Id: int
        :param Uuid: 云镜ID
        :type Uuid: str
        :param Quuid: 主机ID
        :type Quuid: str
        :param Hostip: 主机内网IP
        :type Hostip: str
        :param User: 执行用户名
        :type User: str
        :param Platform: 平台类型
        :type Platform: int
        :param BashCmd: 执行命令
        :type BashCmd: str
        :param RuleId: 规则ID
        :type RuleId: int
        :param RuleName: 规则名称
        :type RuleName: str
        :param RuleLevel: 规则等级：1-高 2-中 3-低
        :type RuleLevel: int
        :param Status: 处理状态： 0 = 待处理 1= 已处理, 2 = 已加白
        :type Status: int
        :param CreateTime: 发生时间
        :type CreateTime: str
        :param MachineName: 主机名
        :type MachineName: str
        :param DetectBy: 0: bash日志 1: 实时监控(雷霆版)
注意：此字段可能返回 null，表示取不到有效值。
        :type DetectBy: int
        :param Pid: 进程id
注意：此字段可能返回 null，表示取不到有效值。
        :type Pid: str
        :param Exe: 进程名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Exe: str
        :param ModifyTime: 处理时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTime: str
        :param RuleCategory: 规则类别  0=系统规则，1=用户规则
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleCategory: int
        :param RegexBashCmd: 自动生成的正则表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type RegexBashCmd: str
        """
        self.Id = None
        self.Uuid = None
        self.Quuid = None
        self.Hostip = None
        self.User = None
        self.Platform = None
        self.BashCmd = None
        self.RuleId = None
        self.RuleName = None
        self.RuleLevel = None
        self.Status = None
        self.CreateTime = None
        self.MachineName = None
        self.DetectBy = None
        self.Pid = None
        self.Exe = None
        self.ModifyTime = None
        self.RuleCategory = None
        self.RegexBashCmd = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        self.Hostip = params.get("Hostip")
        self.User = params.get("User")
        self.Platform = params.get("Platform")
        self.BashCmd = params.get("BashCmd")
        self.RuleId = params.get("RuleId")
        self.RuleName = params.get("RuleName")
        self.RuleLevel = params.get("RuleLevel")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.MachineName = params.get("MachineName")
        self.DetectBy = params.get("DetectBy")
        self.Pid = params.get("Pid")
        self.Exe = params.get("Exe")
        self.ModifyTime = params.get("ModifyTime")
        self.RuleCategory = params.get("RuleCategory")
        self.RegexBashCmd = params.get("RegexBashCmd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BashRule(AbstractModel):
    """高危命令规则

    """

    def __init__(self):
        """
        :param Id: 规则ID
        :type Id: int
        :param Uuid: 客户端ID
        :type Uuid: str
        :param Name: 规则名称
        :type Name: str
        :param Level: 危险等级(0 ：无 1: 高危 2:中危 3: 低危)
        :type Level: int
        :param Rule: 正则表达式
        :type Rule: str
        :param Decription: 规则描述
        :type Decription: str
        :param Operator: 操作人
        :type Operator: str
        :param IsGlobal: 是否全局规则
        :type IsGlobal: int
        :param Status: 状态 (0: 有效 1: 无效)
        :type Status: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ModifyTime: 修改时间
        :type ModifyTime: str
        :param Hostip: 主机IP
        :type Hostip: str
        :param Uuids: 生效服务器的uuid数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Uuids: list of str
        :param White: 0=黑名单 1=白名单
注意：此字段可能返回 null，表示取不到有效值。
        :type White: int
        :param DealOldEvents: 是否处理之前的事件 0: 不处理 1:处理
注意：此字段可能返回 null，表示取不到有效值。
        :type DealOldEvents: int
        """
        self.Id = None
        self.Uuid = None
        self.Name = None
        self.Level = None
        self.Rule = None
        self.Decription = None
        self.Operator = None
        self.IsGlobal = None
        self.Status = None
        self.CreateTime = None
        self.ModifyTime = None
        self.Hostip = None
        self.Uuids = None
        self.White = None
        self.DealOldEvents = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.Name = params.get("Name")
        self.Level = params.get("Level")
        self.Rule = params.get("Rule")
        self.Decription = params.get("Decription")
        self.Operator = params.get("Operator")
        self.IsGlobal = params.get("IsGlobal")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        self.Hostip = params.get("Hostip")
        self.Uuids = params.get("Uuids")
        self.White = params.get("White")
        self.DealOldEvents = params.get("DealOldEvents")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BruteAttackInfo(AbstractModel):
    """密码破解列表实体

    """

    def __init__(self):
        """
        :param Id: 唯一Id
        :type Id: int
        :param Uuid: 云镜客户端唯一标识UUID
注意：此字段可能返回 null，表示取不到有效值。
        :type Uuid: str
        :param MachineIp: 主机ip
注意：此字段可能返回 null，表示取不到有效值。
        :type MachineIp: str
        :param MachineName: 主机名
注意：此字段可能返回 null，表示取不到有效值。
        :type MachineName: str
        :param UserName: 用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param SrcIp: 来源ip
注意：此字段可能返回 null，表示取不到有效值。
        :type SrcIp: str
        :param Status: 失败：FAILED；成功：SUCCESS
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Country: 国家id
注意：此字段可能返回 null，表示取不到有效值。
        :type Country: int
        :param City: 城市id
注意：此字段可能返回 null，表示取不到有效值。
        :type City: int
        :param Province: 省份id
注意：此字段可能返回 null，表示取不到有效值。
        :type Province: int
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param BanStatus: 阻断状态：0-未阻断；1-已阻断；2-阻断失败；3-内网攻击暂不支持阻断；4-安平暂不支持阻断
注意：此字段可能返回 null，表示取不到有效值。
        :type BanStatus: int
        :param EventType: 事件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type EventType: int
        :param Count: 发生次数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param Quuid: 机器UUID
注意：此字段可能返回 null，表示取不到有效值。
        :type Quuid: str
        :param IsProVersion: 是否为专业版（true/false）
注意：此字段可能返回 null，表示取不到有效值。
        :type IsProVersion: bool
        :param Protocol: 被攻击的服务的用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param Port: 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param ModifyTime: 最近攻击时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTime: str
        """
        self.Id = None
        self.Uuid = None
        self.MachineIp = None
        self.MachineName = None
        self.UserName = None
        self.SrcIp = None
        self.Status = None
        self.Country = None
        self.City = None
        self.Province = None
        self.CreateTime = None
        self.BanStatus = None
        self.EventType = None
        self.Count = None
        self.Quuid = None
        self.IsProVersion = None
        self.Protocol = None
        self.Port = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.UserName = params.get("UserName")
        self.SrcIp = params.get("SrcIp")
        self.Status = params.get("Status")
        self.Country = params.get("Country")
        self.City = params.get("City")
        self.Province = params.get("Province")
        self.CreateTime = params.get("CreateTime")
        self.BanStatus = params.get("BanStatus")
        self.EventType = params.get("EventType")
        self.Count = params.get("Count")
        self.Quuid = params.get("Quuid")
        self.IsProVersion = params.get("IsProVersion")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChargePrepaid(AbstractModel):
    """预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。

    """

    def __init__(self):
        """
        :param Period: 购买实例的时长，单位：月。取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36。
        :type Period: int
        :param RenewFlag: 自动续费标识。取值范围：
<li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费</li>
<li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费</li>
<li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费</li>

默认取值：NOTIFY_AND_MANUAL_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
        :type RenewFlag: str
        """
        self.Period = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseProVersionRequest(AbstractModel):
    """CloseProVersion请求参数结构体

    """

    def __init__(self):
        """
        :param Quuid: 主机唯一标识Uuid。
黑石的InstanceId，CVM的Uuid
        :type Quuid: str
        """
        self.Quuid = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseProVersionResponse(AbstractModel):
    """CloseProVersion返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ComponentStatistics(AbstractModel):
    """组件统计数据。

    """

    def __init__(self):
        """
        :param Id: 组件ID。
        :type Id: int
        :param MachineNum: 主机数量。
        :type MachineNum: int
        :param ComponentName: 组件名称。
        :type ComponentName: str
        :param ComponentType: 组件类型。
<li>WEB：Web组件</li>
<li>SYSTEM：系统组件</li>
        :type ComponentType: str
        :param Description: 组件描述。
        :type Description: str
        """
        self.Id = None
        self.MachineNum = None
        self.ComponentName = None
        self.ComponentType = None
        self.Description = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.MachineNum = params.get("MachineNum")
        self.ComponentName = params.get("ComponentName")
        self.ComponentType = params.get("ComponentType")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBaselineStrategyRequest(AbstractModel):
    """CreateBaselineStrategy请求参数结构体

    """

    def __init__(self):
        """
        :param StrategyName: 策略名称
        :type StrategyName: str
        :param ScanCycle: 检测周期, 表示每隔多少天进行检测.示例: 2, 表示每2天进行检测一次.
        :type ScanCycle: int
        :param ScanAt: 定期检测时间，该时间下发扫描. 示例:“22:00”, 表示在22:00下发检测
        :type ScanAt: str
        :param CategoryIds: 该策略下选择的基线id数组. 示例: [1,3,5,7]
        :type CategoryIds: list of int non-negative
        :param IsGlobal: 扫描范围是否全部服务器, 1:是  0:否, 为1则为全部专业版主机
        :type IsGlobal: int
        :param MachineType: 云主机类型：“CVM”：虚拟主机，"BMS"：裸金属，"ECM"：边缘计算主机
        :type MachineType: str
        :param RegionCode: 主机地域. 示例: "ap-bj"
        :type RegionCode: str
        :param Quuids: 主机id数组. 示例: ["quuid1","quuid2"]
        :type Quuids: list of str
        """
        self.StrategyName = None
        self.ScanCycle = None
        self.ScanAt = None
        self.CategoryIds = None
        self.IsGlobal = None
        self.MachineType = None
        self.RegionCode = None
        self.Quuids = None


    def _deserialize(self, params):
        self.StrategyName = params.get("StrategyName")
        self.ScanCycle = params.get("ScanCycle")
        self.ScanAt = params.get("ScanAt")
        self.CategoryIds = params.get("CategoryIds")
        self.IsGlobal = params.get("IsGlobal")
        self.MachineType = params.get("MachineType")
        self.RegionCode = params.get("RegionCode")
        self.Quuids = params.get("Quuids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBaselineStrategyResponse(AbstractModel):
    """CreateBaselineStrategy返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateProtectServerRequest(AbstractModel):
    """CreateProtectServer请求参数结构体

    """

    def __init__(self):
        """
        :param ProtectDir: 防护目录地址
        :type ProtectDir: str
        :param ProtectHostConfig: 防护机器 信息
        :type ProtectHostConfig: list of ProtectHostConfig
        """
        self.ProtectDir = None
        self.ProtectHostConfig = None


    def _deserialize(self, params):
        self.ProtectDir = params.get("ProtectDir")
        if params.get("ProtectHostConfig") is not None:
            self.ProtectHostConfig = []
            for item in params.get("ProtectHostConfig"):
                obj = ProtectHostConfig()
                obj._deserialize(item)
                self.ProtectHostConfig.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProtectServerResponse(AbstractModel):
    """CreateProtectServer返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateScanMalwareSettingRequest(AbstractModel):
    """CreateScanMalwareSetting请求参数结构体

    """

    def __init__(self):
        """
        :param ScanPattern: 扫描模式 0 全盘扫描, 1 快速扫描
        :type ScanPattern: int
        :param HostType: 服务器分类：1:专业版服务器；2:自选服务器
        :type HostType: int
        :param QuuidList: 自选服务器时生效，主机quuid的string数组
        :type QuuidList: list of str
        :param TimeoutPeriod: 超时时间单位 秒
        :type TimeoutPeriod: int
        """
        self.ScanPattern = None
        self.HostType = None
        self.QuuidList = None
        self.TimeoutPeriod = None


    def _deserialize(self, params):
        self.ScanPattern = params.get("ScanPattern")
        self.HostType = params.get("HostType")
        self.QuuidList = params.get("QuuidList")
        self.TimeoutPeriod = params.get("TimeoutPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateScanMalwareSettingResponse(AbstractModel):
    """CreateScanMalwareSetting返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSearchLogRequest(AbstractModel):
    """CreateSearchLog请求参数结构体

    """

    def __init__(self):
        """
        :param SearchContent: 搜索内容
        :type SearchContent: str
        """
        self.SearchContent = None


    def _deserialize(self, params):
        self.SearchContent = params.get("SearchContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSearchLogResponse(AbstractModel):
    """CreateSearchLog返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 0：成功，非0：失败
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class CreateSearchTemplateRequest(AbstractModel):
    """CreateSearchTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param SearchTemplate: 搜索模板
        :type SearchTemplate: :class:`tencentcloud.cwp.v20180228.models.SearchTemplate`
        """
        self.SearchTemplate = None


    def _deserialize(self, params):
        if params.get("SearchTemplate") is not None:
            self.SearchTemplate = SearchTemplate()
            self.SearchTemplate._deserialize(params.get("SearchTemplate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSearchTemplateResponse(AbstractModel):
    """CreateSearchTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 0：成功，非0：失败
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DefendAttackLog(AbstractModel):
    """网络攻击日志

    """

    def __init__(self):
        """
        :param Id: 日志ID
        :type Id: int
        :param Uuid: 客户端ID
        :type Uuid: str
        :param SrcIp: 来源IP
        :type SrcIp: str
        :param SrcPort: 来源端口
        :type SrcPort: int
        :param HttpMethod: 攻击方式
        :type HttpMethod: str
        :param HttpCgi: 攻击描述
        :type HttpCgi: str
        :param HttpParam: 攻击参数
        :type HttpParam: str
        :param VulType: 威胁类型
        :type VulType: str
        :param CreatedAt: 攻击时间
        :type CreatedAt: str
        :param MachineIp: 目标服务器IP
        :type MachineIp: str
        :param MachineName: 目标服务器名称
        :type MachineName: str
        :param DstIp: 目标IP
        :type DstIp: str
        :param DstPort: 目标端口
        :type DstPort: int
        :param HttpContent: 攻击内容
        :type HttpContent: str
        """
        self.Id = None
        self.Uuid = None
        self.SrcIp = None
        self.SrcPort = None
        self.HttpMethod = None
        self.HttpCgi = None
        self.HttpParam = None
        self.VulType = None
        self.CreatedAt = None
        self.MachineIp = None
        self.MachineName = None
        self.DstIp = None
        self.DstPort = None
        self.HttpContent = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.SrcIp = params.get("SrcIp")
        self.SrcPort = params.get("SrcPort")
        self.HttpMethod = params.get("HttpMethod")
        self.HttpCgi = params.get("HttpCgi")
        self.HttpParam = params.get("HttpParam")
        self.VulType = params.get("VulType")
        self.CreatedAt = params.get("CreatedAt")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.DstIp = params.get("DstIp")
        self.DstPort = params.get("DstPort")
        self.HttpContent = params.get("HttpContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAttackLogsRequest(AbstractModel):
    """DeleteAttackLogs请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 日志ID数组，最大100条。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAttackLogsResponse(AbstractModel):
    """DeleteAttackLogs返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteBashEventsRequest(AbstractModel):
    """DeleteBashEvents请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: ID数组，最大100条。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBashEventsResponse(AbstractModel):
    """DeleteBashEvents返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteBashRulesRequest(AbstractModel):
    """DeleteBashRules请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: ID数组，最大100条。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBashRulesResponse(AbstractModel):
    """DeleteBashRules返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteBruteAttacksRequest(AbstractModel):
    """DeleteBruteAttacks请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 暴力破解事件Id数组。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBruteAttacksResponse(AbstractModel):
    """DeleteBruteAttacks返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLoginWhiteListRequest(AbstractModel):
    """DeleteLoginWhiteList请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 白名单ID
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoginWhiteListResponse(AbstractModel):
    """DeleteLoginWhiteList返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMachineRequest(AbstractModel):
    """DeleteMachine请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端Uuid。
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMachineResponse(AbstractModel):
    """DeleteMachine返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMachineTagRequest(AbstractModel):
    """DeleteMachineTag请求参数结构体

    """

    def __init__(self):
        """
        :param Rid: 关联的标签ID
        :type Rid: int
        """
        self.Rid = None


    def _deserialize(self, params):
        self.Rid = params.get("Rid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMachineTagResponse(AbstractModel):
    """DeleteMachineTag返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMaliciousRequestsRequest(AbstractModel):
    """DeleteMaliciousRequests请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 恶意请求记录ID数组，最大100条。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMaliciousRequestsResponse(AbstractModel):
    """DeleteMaliciousRequests返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteMalwaresRequest(AbstractModel):
    """DeleteMalwares请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 木马记录ID数组 (最大100条)
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMalwaresResponse(AbstractModel):
    """DeleteMalwares返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNonlocalLoginPlacesRequest(AbstractModel):
    """DeleteNonlocalLoginPlaces请求参数结构体

    """

    def __init__(self):
        """
        :param DelType: 删除异地登录事件的方式，可选值："Ids"、"Ip"、"All"，默认为Ids
        :type DelType: str
        :param Ids: 异地登录事件ID数组。DelType为Ids或DelType未填时此项必填
        :type Ids: list of int non-negative
        :param Ip: 异地登录事件的Ip。DelType为Ip时必填
        :type Ip: list of str
        :param Uuid: 主机Uuid
        :type Uuid: str
        """
        self.DelType = None
        self.Ids = None
        self.Ip = None
        self.Uuid = None


    def _deserialize(self, params):
        self.DelType = params.get("DelType")
        self.Ids = params.get("Ids")
        self.Ip = params.get("Ip")
        self.Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNonlocalLoginPlacesResponse(AbstractModel):
    """DeleteNonlocalLoginPlaces返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePrivilegeEventsRequest(AbstractModel):
    """DeletePrivilegeEvents请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: ID数组，最大100条。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrivilegeEventsResponse(AbstractModel):
    """DeletePrivilegeEvents返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePrivilegeRulesRequest(AbstractModel):
    """DeletePrivilegeRules请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: ID数组，最大100条。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrivilegeRulesResponse(AbstractModel):
    """DeletePrivilegeRules返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteReverseShellEventsRequest(AbstractModel):
    """DeleteReverseShellEvents请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: ID数组，最大100条。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReverseShellEventsResponse(AbstractModel):
    """DeleteReverseShellEvents返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteReverseShellRulesRequest(AbstractModel):
    """DeleteReverseShellRules请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: ID数组，最大100条。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReverseShellRulesResponse(AbstractModel):
    """DeleteReverseShellRules返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSearchTemplateRequest(AbstractModel):
    """DeleteSearchTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 模板ID
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSearchTemplateResponse(AbstractModel):
    """DeleteSearchTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 0：成功，非0：失败
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DeleteTagsRequest(AbstractModel):
    """DeleteTags请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 标签ID
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTagsResponse(AbstractModel):
    """DeleteTags返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWebPageEventLogRequest(AbstractModel):
    """DeleteWebPageEventLog请求参数结构体

    """


class DeleteWebPageEventLogResponse(AbstractModel):
    """DeleteWebPageEventLog返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccountStatisticsRequest(AbstractModel):
    """DescribeAccountStatistics请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Username - String - 是否必填：否 - 帐号用户名</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountStatisticsResponse(AbstractModel):
    """DescribeAccountStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 帐号统计列表记录总数。
        :type TotalCount: int
        :param AccountStatistics: 帐号统计列表。
        :type AccountStatistics: list of AccountStatistics
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AccountStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AccountStatistics") is not None:
            self.AccountStatistics = []
            for item in params.get("AccountStatistics"):
                obj = AccountStatistics()
                obj._deserialize(item)
                self.AccountStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端唯一Uuid。Username和Uuid必填其一，使用Uuid表示，查询该主机下列表信息。
        :type Uuid: str
        :param Username: 云镜客户端唯一Uuid。Username和Uuid必填其一，使用Username表示，查询该用户名下列表信息。
        :type Username: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Username - String - 是否必填：否 - 帐号名</li>
<li>Privilege - String - 是否必填：否 - 帐号类型（ORDINARY: 普通帐号 | SUPPER: 超级管理员帐号）</li>
<li>MachineIp - String - 是否必填：否 - 主机内网IP</li>
        :type Filters: list of Filter
        """
        self.Uuid = None
        self.Username = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Username = params.get("Username")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 帐号列表记录总数。
        :type TotalCount: int
        :param Accounts: 帐号数据列表。
        :type Accounts: list of Account
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Accounts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAssetInfoRequest(AbstractModel):
    """DescribeAssetInfo请求参数结构体

    """


class DescribeAssetInfoResponse(AbstractModel):
    """DescribeAssetInfo返回参数结构体

    """

    def __init__(self):
        """
        :param MachineCount: 主机数
        :type MachineCount: int
        :param AccountCount: 账号数
        :type AccountCount: int
        :param PortCount: 端口数
        :type PortCount: int
        :param ProcessCount: 进程数
        :type ProcessCount: int
        :param SoftwareCount: 软件数
        :type SoftwareCount: int
        :param DatabaseCount: 数据库数
        :type DatabaseCount: int
        :param WebAppCount: Web应用数
        :type WebAppCount: int
        :param WebFrameCount: Web框架数
        :type WebFrameCount: int
        :param WebServiceCount: Web服务数
        :type WebServiceCount: int
        :param WebLocationCount: Web站点数
        :type WebLocationCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MachineCount = None
        self.AccountCount = None
        self.PortCount = None
        self.ProcessCount = None
        self.SoftwareCount = None
        self.DatabaseCount = None
        self.WebAppCount = None
        self.WebFrameCount = None
        self.WebServiceCount = None
        self.WebLocationCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MachineCount = params.get("MachineCount")
        self.AccountCount = params.get("AccountCount")
        self.PortCount = params.get("PortCount")
        self.ProcessCount = params.get("ProcessCount")
        self.SoftwareCount = params.get("SoftwareCount")
        self.DatabaseCount = params.get("DatabaseCount")
        self.WebAppCount = params.get("WebAppCount")
        self.WebFrameCount = params.get("WebFrameCount")
        self.WebServiceCount = params.get("WebServiceCount")
        self.WebLocationCount = params.get("WebLocationCount")
        self.RequestId = params.get("RequestId")


class DescribeAssetRecentMachineInfoRequest(AbstractModel):
    """DescribeAssetRecentMachineInfo请求参数结构体

    """

    def __init__(self):
        """
        :param BeginDate: 开始时间，如：2020-09-22
        :type BeginDate: str
        :param EndDate: 结束时间，如：2020-09-22
        :type EndDate: str
        """
        self.BeginDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssetRecentMachineInfoResponse(AbstractModel):
    """DescribeAssetRecentMachineInfo返回参数结构体

    """

    def __init__(self):
        """
        :param TotalList: 总数量列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalList: list of AssetKeyVal
        :param LiveList: 在线数量列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveList: list of AssetKeyVal
        :param OfflineList: 离线数量列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OfflineList: list of AssetKeyVal
        :param RiskList: 风险数量列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskList: list of AssetKeyVal
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalList = None
        self.LiveList = None
        self.OfflineList = None
        self.RiskList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TotalList") is not None:
            self.TotalList = []
            for item in params.get("TotalList"):
                obj = AssetKeyVal()
                obj._deserialize(item)
                self.TotalList.append(obj)
        if params.get("LiveList") is not None:
            self.LiveList = []
            for item in params.get("LiveList"):
                obj = AssetKeyVal()
                obj._deserialize(item)
                self.LiveList.append(obj)
        if params.get("OfflineList") is not None:
            self.OfflineList = []
            for item in params.get("OfflineList"):
                obj = AssetKeyVal()
                obj._deserialize(item)
                self.OfflineList.append(obj)
        if params.get("RiskList") is not None:
            self.RiskList = []
            for item in params.get("RiskList"):
                obj = AssetKeyVal()
                obj._deserialize(item)
                self.RiskList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAttackLogInfoRequest(AbstractModel):
    """DescribeAttackLogInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 日志ID
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAttackLogInfoResponse(AbstractModel):
    """DescribeAttackLogInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Id: 日志ID
        :type Id: int
        :param Quuid: 主机ID
        :type Quuid: str
        :param SrcPort: 攻击来源端口
        :type SrcPort: int
        :param SrcIp: 攻击来源IP
        :type SrcIp: str
        :param DstPort: 攻击目标端口
        :type DstPort: int
        :param DstIp: 攻击目标IP
        :type DstIp: str
        :param HttpMethod: 攻击方法
        :type HttpMethod: str
        :param HttpHost: 攻击目标主机
        :type HttpHost: str
        :param HttpHead: 攻击头信息
        :type HttpHead: str
        :param HttpUserAgent: 攻击者浏览器标识
        :type HttpUserAgent: str
        :param HttpReferer: 请求源
        :type HttpReferer: str
        :param VulType: 威胁类型
        :type VulType: str
        :param HttpCgi: 攻击路径
        :type HttpCgi: str
        :param HttpParam: 攻击参数
        :type HttpParam: str
        :param CreatedAt: 攻击时间
        :type CreatedAt: str
        :param HttpContent: 攻击内容
        :type HttpContent: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.Quuid = None
        self.SrcPort = None
        self.SrcIp = None
        self.DstPort = None
        self.DstIp = None
        self.HttpMethod = None
        self.HttpHost = None
        self.HttpHead = None
        self.HttpUserAgent = None
        self.HttpReferer = None
        self.VulType = None
        self.HttpCgi = None
        self.HttpParam = None
        self.CreatedAt = None
        self.HttpContent = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Quuid = params.get("Quuid")
        self.SrcPort = params.get("SrcPort")
        self.SrcIp = params.get("SrcIp")
        self.DstPort = params.get("DstPort")
        self.DstIp = params.get("DstIp")
        self.HttpMethod = params.get("HttpMethod")
        self.HttpHost = params.get("HttpHost")
        self.HttpHead = params.get("HttpHead")
        self.HttpUserAgent = params.get("HttpUserAgent")
        self.HttpReferer = params.get("HttpReferer")
        self.VulType = params.get("VulType")
        self.HttpCgi = params.get("HttpCgi")
        self.HttpParam = params.get("HttpParam")
        self.CreatedAt = params.get("CreatedAt")
        self.HttpContent = params.get("HttpContent")
        self.RequestId = params.get("RequestId")


class DescribeAttackLogsRequest(AbstractModel):
    """DescribeAttackLogs请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>HttpMethod - String - 是否必填：否 - 攻击方法(POST|GET)</li>
<li>DateRange - String - 是否必填：否 - 时间范围(存储最近3个月的数据)，如最近一个月["2019-11-17", "2019-12-17"]</li>
<li>VulType - String 威胁类型 - 是否必填: 否</li>
<li>SrcIp - String 攻击源IP - 是否必填: 否</li>
<li>DstIp - String 攻击目标IP - 是否必填: 否</li>
<li>SrcPort - String 攻击源端口 - 是否必填: 否</li>
<li>DstPort - String 攻击目标端口 - 是否必填: 否</li>
        :type Filters: list of Filter
        :param Uuid: 主机安全客户端ID
        :type Uuid: str
        :param Quuid: 云主机机器ID
        :type Quuid: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Uuid = None
        self.Quuid = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAttackLogsResponse(AbstractModel):
    """DescribeAttackLogs返回参数结构体

    """

    def __init__(self):
        """
        :param AttackLogs: 日志列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AttackLogs: list of DefendAttackLog
        :param TotalCount: 总条数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AttackLogs = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AttackLogs") is not None:
            self.AttackLogs = []
            for item in params.get("AttackLogs"):
                obj = DefendAttackLog()
                obj._deserialize(item)
                self.AttackLogs.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAttackVulTypeListRequest(AbstractModel):
    """DescribeAttackVulTypeList请求参数结构体

    """


class DescribeAttackVulTypeListResponse(AbstractModel):
    """DescribeAttackVulTypeList返回参数结构体

    """

    def __init__(self):
        """
        :param List: 威胁类型列表
        :type List: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.List = params.get("List")
        self.RequestId = params.get("RequestId")


class DescribeBashEventsRequest(AbstractModel):
    """DescribeBashEvents请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 关键词(主机内网IP)</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBashEventsResponse(AbstractModel):
    """DescribeBashEvents返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总条数
        :type TotalCount: int
        :param List: 高危命令事件列表
        :type List: list of BashEvent
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = BashEvent()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBashRulesRequest(AbstractModel):
    """DescribeBashRules请求参数结构体

    """

    def __init__(self):
        """
        :param Type: 0-系统规则; 1-用户规则
        :type Type: int
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 关键字(规则名称)</li>
        :type Filters: list of Filter
        """
        self.Type = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBashRulesResponse(AbstractModel):
    """DescribeBashRules返回参数结构体

    """

    def __init__(self):
        """
        :param List: 列表内容
        :type List: list of BashRule
        :param TotalCount: 总条数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = BashRule()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeBruteAttackListRequest(AbstractModel):
    """DescribeBruteAttackList请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>IpOrAlias - String - 是否必填：否 - 主机ip或别名筛选</li>
<li>Status - String - 是否必填：否 - 状态筛选：失败：FAILED 成功：SUCCESS</li>
<li>UserName - String - 是否必填：否 - UserName筛选</li>
<li>SrcIp - String - 是否必填：否 - 来源ip筛选</li>
<li>CreateBeginTime - String - 是否必填：否 - 创建时间筛选，开始时间</li>
<li>CreateEndTime - String - 是否必填：否 - 创建时间筛选，结束时间</li>
<li>Banned - String - 是否必填：否 - 阻断状态筛选，多个用","分割：0-未阻断（全局ZK开关关闭），82-未阻断(非专业版)，83-未阻断(已加白名单)，1-已阻断，2-未阻断-程序异常，3-未阻断-内网攻击暂不支持阻断，4-未阻断-安平暂不支持阻断</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBruteAttackListResponse(AbstractModel):
    """DescribeBruteAttackList返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param BruteAttackList: 密码破解列表
注意：此字段可能返回 null，表示取不到有效值。
        :type BruteAttackList: list of BruteAttackInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.BruteAttackList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BruteAttackList") is not None:
            self.BruteAttackList = []
            for item in params.get("BruteAttackList"):
                obj = BruteAttackInfo()
                obj._deserialize(item)
                self.BruteAttackList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeComponentStatisticsRequest(AbstractModel):
    """DescribeComponentStatistics请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
ComponentName - String - 是否必填：否 - 组件名称
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeComponentStatisticsResponse(AbstractModel):
    """DescribeComponentStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 组件统计列表记录总数。
        :type TotalCount: int
        :param ComponentStatistics: 组件统计列表数据数组。
        :type ComponentStatistics: list of ComponentStatistics
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ComponentStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ComponentStatistics") is not None:
            self.ComponentStatistics = []
            for item in params.get("ComponentStatistics"):
                obj = ComponentStatistics()
                obj._deserialize(item)
                self.ComponentStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeESAggregationsRequest(AbstractModel):
    """DescribeESAggregations请求参数结构体

    """

    def __init__(self):
        """
        :param Query: ES聚合条件JSON
        :type Query: str
        """
        self.Query = None


    def _deserialize(self, params):
        self.Query = params.get("Query")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeESAggregationsResponse(AbstractModel):
    """DescribeESAggregations返回参数结构体

    """

    def __init__(self):
        """
        :param Data: ES聚合结果JSON
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeESHitsRequest(AbstractModel):
    """DescribeESHits请求参数结构体

    """

    def __init__(self):
        """
        :param Query: ES查询条件JSON
        :type Query: str
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        """
        self.Query = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Query = params.get("Query")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeESHitsResponse(AbstractModel):
    """DescribeESHits返回参数结构体

    """

    def __init__(self):
        """
        :param Data: ES查询结果JSON
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeExportMachinesRequest(AbstractModel):
    """DescribeExportMachines请求参数结构体

    """

    def __init__(self):
        """
        :param MachineType: 云主机类型。
<li>CVM：表示虚拟主机</li>
<li>BM:  表示黑石物理机</li>
        :type MachineType: str
        :param MachineRegion: 机器所属地域。如：ap-guangzhou，ap-shanghai
        :type MachineRegion: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 查询关键字 </li>
<li>Status - String - 是否必填：否 - 客户端在线状态（OFFLINE: 离线 | ONLINE: 在线 | UNINSTALLED：未安装）</li>
<li>Version - String  是否必填：否 - 当前防护版本（ PRO_VERSION：专业版 | BASIC_VERSION：基础版）</li>
每个过滤条件只支持一个值，暂不支持多个值“或”关系查询
        :type Filters: list of Filter
        :param ProjectIds: 机器所属业务ID列表
        :type ProjectIds: list of int non-negative
        """
        self.MachineType = None
        self.MachineRegion = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.ProjectIds = None


    def _deserialize(self, params):
        self.MachineType = params.get("MachineType")
        self.MachineRegion = params.get("MachineRegion")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.ProjectIds = params.get("ProjectIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExportMachinesResponse(AbstractModel):
    """DescribeExportMachines返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务id
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DescribeGeneralStatRequest(AbstractModel):
    """DescribeGeneralStat请求参数结构体

    """

    def __init__(self):
        """
        :param MachineType: 云主机类型。
<li>CVM：表示虚拟主机</li>
<li>BM:  表示黑石物理机</li>
        :type MachineType: str
        :param MachineRegion: 机器所属地域。如：ap-guangzhou，ap-shanghai
        :type MachineRegion: str
        """
        self.MachineType = None
        self.MachineRegion = None


    def _deserialize(self, params):
        self.MachineType = params.get("MachineType")
        self.MachineRegion = params.get("MachineRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGeneralStatResponse(AbstractModel):
    """DescribeGeneralStat返回参数结构体

    """

    def __init__(self):
        """
        :param MachinesAll: 云主机总数
        :type MachinesAll: int
        :param MachinesUninstalled: 云主机没有安装主机安全客户端的总数
        :type MachinesUninstalled: int
        :param AgentsAll: 主机安全客户端总数的总数
        :type AgentsAll: int
        :param AgentsOnline: 主机安全客户端在线的总数
        :type AgentsOnline: int
        :param AgentsOffline: 主机安全客户端离线的总数
        :type AgentsOffline: int
        :param AgentsPro: 主机安全客户端专业版的总数
        :type AgentsPro: int
        :param AgentsBasic: 主机安全客户端基础版的总数
        :type AgentsBasic: int
        :param AgentsProExpireWithInSevenDays: 7天内到期的预付费专业版总数
        :type AgentsProExpireWithInSevenDays: int
        :param RiskMachine: 风险主机总数
        :type RiskMachine: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MachinesAll = None
        self.MachinesUninstalled = None
        self.AgentsAll = None
        self.AgentsOnline = None
        self.AgentsOffline = None
        self.AgentsPro = None
        self.AgentsBasic = None
        self.AgentsProExpireWithInSevenDays = None
        self.RiskMachine = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MachinesAll = params.get("MachinesAll")
        self.MachinesUninstalled = params.get("MachinesUninstalled")
        self.AgentsAll = params.get("AgentsAll")
        self.AgentsOnline = params.get("AgentsOnline")
        self.AgentsOffline = params.get("AgentsOffline")
        self.AgentsPro = params.get("AgentsPro")
        self.AgentsBasic = params.get("AgentsBasic")
        self.AgentsProExpireWithInSevenDays = params.get("AgentsProExpireWithInSevenDays")
        self.RiskMachine = params.get("RiskMachine")
        self.RequestId = params.get("RequestId")


class DescribeHistoryAccountsRequest(AbstractModel):
    """DescribeHistoryAccounts请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Username - String - 是否必填：否 - 帐号名</li>
        :type Filters: list of Filter
        """
        self.Uuid = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHistoryAccountsResponse(AbstractModel):
    """DescribeHistoryAccounts返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 帐号变更历史列表记录总数。
        :type TotalCount: int
        :param HistoryAccounts: 帐号变更历史数据数组。
        :type HistoryAccounts: list of HistoryAccount
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.HistoryAccounts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("HistoryAccounts") is not None:
            self.HistoryAccounts = []
            for item in params.get("HistoryAccounts"):
                obj = HistoryAccount()
                obj._deserialize(item)
                self.HistoryAccounts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeHistoryServiceRequest(AbstractModel):
    """DescribeHistoryService请求参数结构体

    """


class DescribeHistoryServiceResponse(AbstractModel):
    """DescribeHistoryService返回参数结构体

    """

    def __init__(self):
        """
        :param BuyStatus: 1 可购买 2 只能升降配 3 只能跳到续费管理页
        :type BuyStatus: int
        :param InquireNum: 用户已购容量 单位 G
        :type InquireNum: int
        :param EndTime: 到期时间
        :type EndTime: str
        :param IsAutoOpenRenew: 是否自动续费,0 初始值, 1 开通 2 没开通
        :type IsAutoOpenRenew: int
        :param ResourceId: 资源ID
        :type ResourceId: str
        :param Status: 0 没开通 1 正常 2隔离 3销毁
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BuyStatus = None
        self.InquireNum = None
        self.EndTime = None
        self.IsAutoOpenRenew = None
        self.ResourceId = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BuyStatus = params.get("BuyStatus")
        self.InquireNum = params.get("InquireNum")
        self.EndTime = params.get("EndTime")
        self.IsAutoOpenRenew = params.get("IsAutoOpenRenew")
        self.ResourceId = params.get("ResourceId")
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeImportMachineInfoRequest(AbstractModel):
    """DescribeImportMachineInfo请求参数结构体

    """

    def __init__(self):
        """
        :param MachineList: 服务器内网IP（默认）/ 服务器名称 / 服务器ID 数组
        :type MachineList: list of str
        :param ImportType: 批量导入的数据类型：Ip、Name、Id 三选一
        :type ImportType: str
        :param IsQueryProMachine: 是否仅支持专业版机器的查询（true：仅专业版   false：专业版+基础版）
        :type IsQueryProMachine: bool
        """
        self.MachineList = None
        self.ImportType = None
        self.IsQueryProMachine = None


    def _deserialize(self, params):
        self.MachineList = params.get("MachineList")
        self.ImportType = params.get("ImportType")
        self.IsQueryProMachine = params.get("IsQueryProMachine")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImportMachineInfoResponse(AbstractModel):
    """DescribeImportMachineInfo返回参数结构体

    """

    def __init__(self):
        """
        :param EffectiveMachineInfoList: 有效的机器信息列表：机器名称、机器公网/内网ip、机器标签
注意：此字段可能返回 null，表示取不到有效值。
        :type EffectiveMachineInfoList: list of EffectiveMachineInfo
        :param InvalidMachineList: 用户批量导入失败的机器列表（比如机器不存在等...）
注意：此字段可能返回 null，表示取不到有效值。
        :type InvalidMachineList: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EffectiveMachineInfoList = None
        self.InvalidMachineList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EffectiveMachineInfoList") is not None:
            self.EffectiveMachineInfoList = []
            for item in params.get("EffectiveMachineInfoList"):
                obj = EffectiveMachineInfo()
                obj._deserialize(item)
                self.EffectiveMachineInfoList.append(obj)
        self.InvalidMachineList = params.get("InvalidMachineList")
        self.RequestId = params.get("RequestId")


class DescribeIndexListRequest(AbstractModel):
    """DescribeIndexList请求参数结构体

    """


class DescribeIndexListResponse(AbstractModel):
    """DescribeIndexList返回参数结构体

    """

    def __init__(self):
        """
        :param Data: ES 索引信息
        :type Data: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeLogStorageStatisticRequest(AbstractModel):
    """DescribeLogStorageStatistic请求参数结构体

    """


class DescribeLogStorageStatisticResponse(AbstractModel):
    """DescribeLogStorageStatistic返回参数结构体

    """

    def __init__(self):
        """
        :param TotalSize: 总容量（单位：GB）
        :type TotalSize: int
        :param UsedSize: 已使用容量（单位：GB）
        :type UsedSize: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalSize = None
        self.UsedSize = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalSize = params.get("TotalSize")
        self.UsedSize = params.get("UsedSize")
        self.RequestId = params.get("RequestId")


class DescribeLoginWhiteListRequest(AbstractModel):
    """DescribeLoginWhiteList请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 查询关键字 </li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoginWhiteListResponse(AbstractModel):
    """DescribeLoginWhiteList返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 记录总数
        :type TotalCount: int
        :param LoginWhiteLists: 异地登录白名单数组
        :type LoginWhiteLists: list of LoginWhiteLists
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.LoginWhiteLists = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("LoginWhiteLists") is not None:
            self.LoginWhiteLists = []
            for item in params.get("LoginWhiteLists"):
                obj = LoginWhiteLists()
                obj._deserialize(item)
                self.LoginWhiteLists.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMachineInfoRequest(AbstractModel):
    """DescribeMachineInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        :param Quuid: cvm id， quuid、uuid必填一个
        :type Quuid: str
        """
        self.Uuid = None
        self.Quuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMachineInfoResponse(AbstractModel):
    """DescribeMachineInfo返回参数结构体

    """

    def __init__(self):
        """
        :param MachineIp: 机器ip。
        :type MachineIp: str
        :param ProtectDays: 受云镜保护天数。
        :type ProtectDays: int
        :param MachineOs: 操作系统。
        :type MachineOs: str
        :param MachineName: 主机名称。
        :type MachineName: str
        :param MachineStatus: 在线状态。
<li>ONLINE： 在线</li>
<li>OFFLINE：离线</li>
        :type MachineStatus: str
        :param InstanceId: CVM或BM主机唯一标识。
        :type InstanceId: str
        :param MachineWanIp: 主机外网IP。
        :type MachineWanIp: str
        :param Quuid: CVM或BM主机唯一Uuid。
        :type Quuid: str
        :param Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        :param IsProVersion: 是否开通专业版。
<li>true：是</li>
<li>false：否</li>
        :type IsProVersion: bool
        :param ProVersionOpenDate: 专业版开通时间。
        :type ProVersionOpenDate: str
        :param MachineType: 云主机类型。
<li>CVM: 虚拟主机</li>
<li>BM: 黑石物理机</li>
        :type MachineType: str
        :param MachineRegion: 机器所属地域。如：ap-guangzhou，ap-shanghai
        :type MachineRegion: str
        :param PayMode: 主机状态。
<li>POSTPAY: 表示后付费，即按量计费  </li>
<li>PREPAY: 表示预付费，即包年包月</li>
        :type PayMode: str
        :param FreeMalwaresLeft: 免费木马剩余检测数量。
        :type FreeMalwaresLeft: int
        :param FreeVulsLeft: 免费漏洞剩余检测数量。
        :type FreeVulsLeft: int
        :param AgentVersion: agent版本号
        :type AgentVersion: str
        :param ProVersionDeadline: 专业版到期时间(仅预付费)
        :type ProVersionDeadline: str
        :param HasAssetScan: 是否有资产扫描记录，0无，1有
        :type HasAssetScan: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MachineIp = None
        self.ProtectDays = None
        self.MachineOs = None
        self.MachineName = None
        self.MachineStatus = None
        self.InstanceId = None
        self.MachineWanIp = None
        self.Quuid = None
        self.Uuid = None
        self.IsProVersion = None
        self.ProVersionOpenDate = None
        self.MachineType = None
        self.MachineRegion = None
        self.PayMode = None
        self.FreeMalwaresLeft = None
        self.FreeVulsLeft = None
        self.AgentVersion = None
        self.ProVersionDeadline = None
        self.HasAssetScan = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MachineIp = params.get("MachineIp")
        self.ProtectDays = params.get("ProtectDays")
        self.MachineOs = params.get("MachineOs")
        self.MachineName = params.get("MachineName")
        self.MachineStatus = params.get("MachineStatus")
        self.InstanceId = params.get("InstanceId")
        self.MachineWanIp = params.get("MachineWanIp")
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        self.IsProVersion = params.get("IsProVersion")
        self.ProVersionOpenDate = params.get("ProVersionOpenDate")
        self.MachineType = params.get("MachineType")
        self.MachineRegion = params.get("MachineRegion")
        self.PayMode = params.get("PayMode")
        self.FreeMalwaresLeft = params.get("FreeMalwaresLeft")
        self.FreeVulsLeft = params.get("FreeVulsLeft")
        self.AgentVersion = params.get("AgentVersion")
        self.ProVersionDeadline = params.get("ProVersionDeadline")
        self.HasAssetScan = params.get("HasAssetScan")
        self.RequestId = params.get("RequestId")


class DescribeMachineListRequest(AbstractModel):
    """DescribeMachineList请求参数结构体

    """

    def __init__(self):
        """
        :param MachineType: 云主机类型。
<li>CVM：表示虚拟主机</li>
<li>BM:  表示黑石物理机</li>
        :type MachineType: str
        :param MachineRegion: 机器所属地域。如：ap-guangzhou，ap-shanghai
        :type MachineRegion: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 查询关键字 </li>
<li>Status - String - 是否必填：否 - 客户端在线状态（OFFLINE: 离线 | ONLINE: 在线 | UNINSTALLED：未安装）</li>
<li>Version - String  是否必填：否 - 当前防护版本（ PRO_VERSION：专业版 | BASIC_VERSION：基础版）</li>
每个过滤条件只支持一个值，暂不支持多个值“或”关系查询
        :type Filters: list of AssetFilters
        """
        self.MachineType = None
        self.MachineRegion = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.MachineType = params.get("MachineType")
        self.MachineRegion = params.get("MachineRegion")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMachineListResponse(AbstractModel):
    """DescribeMachineList返回参数结构体

    """

    def __init__(self):
        """
        :param Machines: 主机列表
        :type Machines: list of Machine
        :param TotalCount: 主机数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Machines = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Machines") is not None:
            self.Machines = []
            for item in params.get("Machines"):
                obj = Machine()
                obj._deserialize(item)
                self.Machines.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeMachineOsListRequest(AbstractModel):
    """DescribeMachineOsList请求参数结构体

    """


class DescribeMachineOsListResponse(AbstractModel):
    """DescribeMachineOsList返回参数结构体

    """

    def __init__(self):
        """
        :param List: 操作系统列表
        :type List: list of OsName
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = OsName()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMachineRegionsRequest(AbstractModel):
    """DescribeMachineRegions请求参数结构体

    """


class DescribeMachineRegionsResponse(AbstractModel):
    """DescribeMachineRegions返回参数结构体

    """

    def __init__(self):
        """
        :param CVM: CVM 云服务器地域列表
        :type CVM: list of RegionInfo
        :param BM: BM 黑石机器地域列表
        :type BM: list of RegionInfo
        :param LH: LH 轻量应用服务器地域列表
        :type LH: list of RegionInfo
        :param ECM: ECM 边缘计算服务器地域列表
        :type ECM: list of RegionInfo
        :param Other: Other 混合云地域列表
        :type Other: list of RegionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CVM = None
        self.BM = None
        self.LH = None
        self.ECM = None
        self.Other = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CVM") is not None:
            self.CVM = []
            for item in params.get("CVM"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.CVM.append(obj)
        if params.get("BM") is not None:
            self.BM = []
            for item in params.get("BM"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.BM.append(obj)
        if params.get("LH") is not None:
            self.LH = []
            for item in params.get("LH"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.LH.append(obj)
        if params.get("ECM") is not None:
            self.ECM = []
            for item in params.get("ECM"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.ECM.append(obj)
        if params.get("Other") is not None:
            self.Other = []
            for item in params.get("Other"):
                obj = RegionInfo()
                obj._deserialize(item)
                self.Other.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMachinesRequest(AbstractModel):
    """DescribeMachines请求参数结构体

    """

    def __init__(self):
        """
        :param MachineType: 云主机类型。
<li>CVM：表示虚拟主机</li>
<li>BM:  表示黑石物理机</li>
        :type MachineType: str
        :param MachineRegion: 机器所属地域。如：ap-guangzhou，ap-shanghai
        :type MachineRegion: str
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 查询关键字 </li>
<li>Status - String - 是否必填：否 - 客户端在线状态（OFFLINE: 离线/关机 | ONLINE: 在线 | UNINSTALLED：未安装 | AGENT_OFFLINE 离线| AGENT_SHUTDOWN 已关机）</li>
<li>Version - String  是否必填：否 - 当前防护版本（ PRO_VERSION：专业版 | BASIC_VERSION：基础版）</li>
<li>Risk - String 是否必填: 否 - 风险主机( yes ) </li>
<li>Os -String 是否必填: 否 - 操作系统( DescribeMachineOsList 接口 值 )
每个过滤条件只支持一个值，暂不支持多个值“或”关系查询
        :type Filters: list of Filter
        :param ProjectIds: 机器所属业务ID列表
        :type ProjectIds: list of int non-negative
        """
        self.MachineType = None
        self.MachineRegion = None
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.ProjectIds = None


    def _deserialize(self, params):
        self.MachineType = params.get("MachineType")
        self.MachineRegion = params.get("MachineRegion")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.ProjectIds = params.get("ProjectIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMachinesResponse(AbstractModel):
    """DescribeMachines返回参数结构体

    """

    def __init__(self):
        """
        :param Machines: 主机列表
        :type Machines: list of Machine
        :param TotalCount: 主机数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Machines = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Machines") is not None:
            self.Machines = []
            for item in params.get("Machines"):
                obj = Machine()
                obj._deserialize(item)
                self.Machines.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeMalwareInfoRequest(AbstractModel):
    """DescribeMalwareInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 唯一ID
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMalwareInfoResponse(AbstractModel):
    """DescribeMalwareInfo返回参数结构体

    """

    def __init__(self):
        """
        :param MalwareInfo: 恶意文件详情信息
        :type MalwareInfo: :class:`tencentcloud.cwp.v20180228.models.MalwareInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MalwareInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MalwareInfo") is not None:
            self.MalwareInfo = MalwareInfo()
            self.MalwareInfo._deserialize(params.get("MalwareInfo"))
        self.RequestId = params.get("RequestId")


class DescribeMalwareTimingScanSettingRequest(AbstractModel):
    """DescribeMalwareTimingScanSetting请求参数结构体

    """


class DescribeMalwareTimingScanSettingResponse(AbstractModel):
    """DescribeMalwareTimingScanSetting返回参数结构体

    """

    def __init__(self):
        """
        :param CheckPattern: 检测模式 0 全盘检测  1快速检测
        :type CheckPattern: int
        :param StartTime: 检测周期 开始时间
        :type StartTime: str
        :param EndTime: 检测周期 超时结束时间
        :type EndTime: str
        :param IsGlobal: 是否全部服务器 1 全部 2 自选
        :type IsGlobal: int
        :param QuuidList: 自选服务器时必须 主机quuid的string数组
注意：此字段可能返回 null，表示取不到有效值。
        :type QuuidList: list of str
        :param MonitoringPattern: 监控模式 0 标准 1深度
        :type MonitoringPattern: int
        :param Cycle: 周期 1每天
        :type Cycle: int
        :param EnableScan: 定时检测开关 0 关闭1 开启
        :type EnableScan: int
        :param Id: 唯一ID
        :type Id: int
        :param RealTimeMonitoring: 实时监控0 关闭 1开启
        :type RealTimeMonitoring: int
        :param AutoIsolation: 是否自动隔离：1-是，0-否
        :type AutoIsolation: int
        :param ClickTimeout: 一键扫描超时时长，如：1800秒（s）
        :type ClickTimeout: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CheckPattern = None
        self.StartTime = None
        self.EndTime = None
        self.IsGlobal = None
        self.QuuidList = None
        self.MonitoringPattern = None
        self.Cycle = None
        self.EnableScan = None
        self.Id = None
        self.RealTimeMonitoring = None
        self.AutoIsolation = None
        self.ClickTimeout = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CheckPattern = params.get("CheckPattern")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.IsGlobal = params.get("IsGlobal")
        self.QuuidList = params.get("QuuidList")
        self.MonitoringPattern = params.get("MonitoringPattern")
        self.Cycle = params.get("Cycle")
        self.EnableScan = params.get("EnableScan")
        self.Id = params.get("Id")
        self.RealTimeMonitoring = params.get("RealTimeMonitoring")
        self.AutoIsolation = params.get("AutoIsolation")
        self.ClickTimeout = params.get("ClickTimeout")
        self.RequestId = params.get("RequestId")


class DescribeOpenPortStatisticsRequest(AbstractModel):
    """DescribeOpenPortStatistics请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Port - Uint64 - 是否必填：否 - 端口号</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOpenPortStatisticsResponse(AbstractModel):
    """DescribeOpenPortStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 端口统计列表总数
        :type TotalCount: int
        :param OpenPortStatistics: 端口统计数据列表
        :type OpenPortStatistics: list of OpenPortStatistics
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.OpenPortStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("OpenPortStatistics") is not None:
            self.OpenPortStatistics = []
            for item in params.get("OpenPortStatistics"):
                obj = OpenPortStatistics()
                obj._deserialize(item)
                self.OpenPortStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOverviewStatisticsRequest(AbstractModel):
    """DescribeOverviewStatistics请求参数结构体

    """


class DescribeOverviewStatisticsResponse(AbstractModel):
    """DescribeOverviewStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param OnlineMachineNum: 服务器在线数。
        :type OnlineMachineNum: int
        :param ProVersionMachineNum: 专业服务器数。
        :type ProVersionMachineNum: int
        :param MalwareNum: 木马文件数。
        :type MalwareNum: int
        :param NonlocalLoginNum: 异地登录数。
        :type NonlocalLoginNum: int
        :param BruteAttackSuccessNum: 暴力破解成功数。
        :type BruteAttackSuccessNum: int
        :param VulNum: 漏洞数。
        :type VulNum: int
        :param BaseLineNum: 安全基线数。
        :type BaseLineNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OnlineMachineNum = None
        self.ProVersionMachineNum = None
        self.MalwareNum = None
        self.NonlocalLoginNum = None
        self.BruteAttackSuccessNum = None
        self.VulNum = None
        self.BaseLineNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OnlineMachineNum = params.get("OnlineMachineNum")
        self.ProVersionMachineNum = params.get("ProVersionMachineNum")
        self.MalwareNum = params.get("MalwareNum")
        self.NonlocalLoginNum = params.get("NonlocalLoginNum")
        self.BruteAttackSuccessNum = params.get("BruteAttackSuccessNum")
        self.VulNum = params.get("VulNum")
        self.BaseLineNum = params.get("BaseLineNum")
        self.RequestId = params.get("RequestId")


class DescribePrivilegeEventsRequest(AbstractModel):
    """DescribePrivilegeEvents请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 关键词(主机IP)</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrivilegeEventsResponse(AbstractModel):
    """DescribePrivilegeEvents返回参数结构体

    """

    def __init__(self):
        """
        :param List: 数据列表
        :type List: list of PrivilegeEscalationProcess
        :param TotalCount: 总条数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = PrivilegeEscalationProcess()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribePrivilegeRulesRequest(AbstractModel):
    """DescribePrivilegeRules请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 关键字(进程名称)</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrivilegeRulesResponse(AbstractModel):
    """DescribePrivilegeRules返回参数结构体

    """

    def __init__(self):
        """
        :param List: 列表内容
        :type List: list of PrivilegeRule
        :param TotalCount: 总条数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = PrivilegeRule()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeProVersionInfoRequest(AbstractModel):
    """DescribeProVersionInfo请求参数结构体

    """


class DescribeProVersionInfoResponse(AbstractModel):
    """DescribeProVersionInfo返回参数结构体

    """

    def __init__(self):
        """
        :param PostPayCost: 后付费昨日扣费
        :type PostPayCost: int
        :param IsAutoOpenProVersion: 新增主机是否自动开通专业版
        :type IsAutoOpenProVersion: bool
        :param ProVersionNum: 开通专业版主机数
        :type ProVersionNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PostPayCost = None
        self.IsAutoOpenProVersion = None
        self.ProVersionNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PostPayCost = params.get("PostPayCost")
        self.IsAutoOpenProVersion = params.get("IsAutoOpenProVersion")
        self.ProVersionNum = params.get("ProVersionNum")
        self.RequestId = params.get("RequestId")


class DescribeProcessStatisticsRequest(AbstractModel):
    """DescribeProcessStatistics请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>ProcessName - String - 是否必填：否 - 进程名</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProcessStatisticsResponse(AbstractModel):
    """DescribeProcessStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 进程统计列表记录总数。
        :type TotalCount: int
        :param ProcessStatistics: 进程统计列表数据数组。
        :type ProcessStatistics: list of ProcessStatistics
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ProcessStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ProcessStatistics") is not None:
            self.ProcessStatistics = []
            for item in params.get("ProcessStatistics"):
                obj = ProcessStatistics()
                obj._deserialize(item)
                self.ProcessStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeReverseShellEventsRequest(AbstractModel):
    """DescribeReverseShellEvents请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 关键字(主机内网IP|进程名)</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReverseShellEventsResponse(AbstractModel):
    """DescribeReverseShellEvents返回参数结构体

    """

    def __init__(self):
        """
        :param List: 列表内容
        :type List: list of ReverseShell
        :param TotalCount: 总条数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = ReverseShell()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeReverseShellRulesRequest(AbstractModel):
    """DescribeReverseShellRules请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 关键字(进程名称)</li>
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReverseShellRulesResponse(AbstractModel):
    """DescribeReverseShellRules返回参数结构体

    """

    def __init__(self):
        """
        :param List: 列表内容
        :type List: list of ReverseShellRule
        :param TotalCount: 总条数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = ReverseShellRule()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRiskDnsListRequest(AbstractModel):
    """DescribeRiskDnsList请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Filters: 过滤条件。
<li>IpOrAlias - String - 是否必填：否 - 主机ip或别名筛选</li>
<li>Url - String - 是否必填：否 - Url筛选</li>
<li>Status - String - 是否必填：否 - 状态筛选0:待处理；2:信任；3:不信任</li>
<li>MergeBeginTime - String - 是否必填：否 - 最近访问开始时间</li>
<li>MergeEndTime - String - 是否必填：否 - 最近访问结束时间</li>
        :type Filters: list of Filter
        :param Order: 排序方式：根据请求次数排序：asc-升序/desc-降序
        :type Order: str
        :param By: 排序字段：AccessCount-请求次数
        :type By: str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.Order = None
        self.By = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskDnsListResponse(AbstractModel):
    """DescribeRiskDnsList返回参数结构体

    """

    def __init__(self):
        """
        :param RiskDnsList: 恶意请求列表数组
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskDnsList: list of RiskDnsList
        :param TotalCount: 总数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RiskDnsList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RiskDnsList") is not None:
            self.RiskDnsList = []
            for item in params.get("RiskDnsList"):
                obj = RiskDnsList()
                obj._deserialize(item)
                self.RiskDnsList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeScanMalwareScheduleRequest(AbstractModel):
    """DescribeScanMalwareSchedule请求参数结构体

    """


class DescribeScanMalwareScheduleResponse(AbstractModel):
    """DescribeScanMalwareSchedule返回参数结构体

    """

    def __init__(self):
        """
        :param Schedule: 扫描进度（单位：%）
        :type Schedule: int
        :param RiskFileNumber: 风险文件数,当进度满了以后才有该值
        :type RiskFileNumber: int
        :param IsSchedule: 是否正在扫描中
        :type IsSchedule: bool
        :param ScanStatus: 0 从未扫描过、 1 扫描中、 2扫描完成、 3停止中、 4停止完成
        :type ScanStatus: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Schedule = None
        self.RiskFileNumber = None
        self.IsSchedule = None
        self.ScanStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Schedule = params.get("Schedule")
        self.RiskFileNumber = params.get("RiskFileNumber")
        self.IsSchedule = params.get("IsSchedule")
        self.ScanStatus = params.get("ScanStatus")
        self.RequestId = params.get("RequestId")


class DescribeScanTaskDetailsRequest(AbstractModel):
    """DescribeScanTaskDetails请求参数结构体

    """

    def __init__(self):
        """
        :param ModuleType: 模块类型 当前提供 Malware 木马 , Vul 漏洞 , Baseline 基线
        :type ModuleType: str
        :param TaskId: 任务ID
        :type TaskId: int
        :param Filters: 过滤参数
        :type Filters: list of Filters
        :param Limit: 需要返回的数量，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self.ModuleType = None
        self.TaskId = None
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ModuleType = params.get("ModuleType")
        self.TaskId = params.get("TaskId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScanTaskDetailsResponse(AbstractModel):
    """DescribeScanTaskDetails返回参数结构体

    """

    def __init__(self):
        """
        :param ScanTaskDetailList: 扫描任务信息列表
        :type ScanTaskDetailList: list of ScanTaskDetails
        :param TotalCount: 总数
        :type TotalCount: int
        :param ScanMachineCount: 扫描机器总数
        :type ScanMachineCount: int
        :param RiskMachineCount: 发现风险机器数
        :type RiskMachineCount: int
        :param ScanBeginTime: 扫描开始时间
        :type ScanBeginTime: str
        :param ScanEndTime: 扫描结束时间
        :type ScanEndTime: str
        :param ScanTime: 检测时间
        :type ScanTime: int
        :param ScanProgress: 扫描进度
        :type ScanProgress: int
        :param ScanLeftTime: 扫描剩余时间
        :type ScanLeftTime: int
        :param ScanContent: 扫描内容
        :type ScanContent: list of str
        :param VulInfo: 漏洞信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VulInfo: list of VulDetailInfo
        :param RiskEventCount: 风险事件个数
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskEventCount: int
        :param Type: 0一键检测 1定时检测
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param StoppingAll: 任务是否全部正在被停止 ture是
注意：此字段可能返回 null，表示取不到有效值。
        :type StoppingAll: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ScanTaskDetailList = None
        self.TotalCount = None
        self.ScanMachineCount = None
        self.RiskMachineCount = None
        self.ScanBeginTime = None
        self.ScanEndTime = None
        self.ScanTime = None
        self.ScanProgress = None
        self.ScanLeftTime = None
        self.ScanContent = None
        self.VulInfo = None
        self.RiskEventCount = None
        self.Type = None
        self.StoppingAll = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ScanTaskDetailList") is not None:
            self.ScanTaskDetailList = []
            for item in params.get("ScanTaskDetailList"):
                obj = ScanTaskDetails()
                obj._deserialize(item)
                self.ScanTaskDetailList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.ScanMachineCount = params.get("ScanMachineCount")
        self.RiskMachineCount = params.get("RiskMachineCount")
        self.ScanBeginTime = params.get("ScanBeginTime")
        self.ScanEndTime = params.get("ScanEndTime")
        self.ScanTime = params.get("ScanTime")
        self.ScanProgress = params.get("ScanProgress")
        self.ScanLeftTime = params.get("ScanLeftTime")
        self.ScanContent = params.get("ScanContent")
        if params.get("VulInfo") is not None:
            self.VulInfo = []
            for item in params.get("VulInfo"):
                obj = VulDetailInfo()
                obj._deserialize(item)
                self.VulInfo.append(obj)
        self.RiskEventCount = params.get("RiskEventCount")
        self.Type = params.get("Type")
        self.StoppingAll = params.get("StoppingAll")
        self.RequestId = params.get("RequestId")


class DescribeScanVulSettingRequest(AbstractModel):
    """DescribeScanVulSetting请求参数结构体

    """


class DescribeScanVulSettingResponse(AbstractModel):
    """DescribeScanVulSetting返回参数结构体

    """

    def __init__(self):
        """
        :param VulCategories: 漏洞类型：1: web应用漏洞 2:系统组件漏洞 (多选英文逗号分隔)
        :type VulCategories: str
        :param VulLevels: 危害等级：1-低危；2-中危；3-高危；4-严重 (多选英文逗号分隔)
        :type VulLevels: str
        :param TimerInterval: 定期检测间隔时间（天）
        :type TimerInterval: int
        :param TimerTime: 定期检测时间，如：00:00
        :type TimerTime: str
        :param VulEmergency: 是否紧急漏洞：0-否 1-是
        :type VulEmergency: int
        :param StartTime: 开始时间
        :type StartTime: str
        :param EnableScan: 是否开启
        :type EnableScan: int
        :param EndTime: 结束时间
        :type EndTime: str
        :param ClickTimeout: 一键扫描超时时长，如：1800秒（s）
        :type ClickTimeout: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VulCategories = None
        self.VulLevels = None
        self.TimerInterval = None
        self.TimerTime = None
        self.VulEmergency = None
        self.StartTime = None
        self.EnableScan = None
        self.EndTime = None
        self.ClickTimeout = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VulCategories = params.get("VulCategories")
        self.VulLevels = params.get("VulLevels")
        self.TimerInterval = params.get("TimerInterval")
        self.TimerTime = params.get("TimerTime")
        self.VulEmergency = params.get("VulEmergency")
        self.StartTime = params.get("StartTime")
        self.EnableScan = params.get("EnableScan")
        self.EndTime = params.get("EndTime")
        self.ClickTimeout = params.get("ClickTimeout")
        self.RequestId = params.get("RequestId")


class DescribeSearchExportListRequest(AbstractModel):
    """DescribeSearchExportList请求参数结构体

    """

    def __init__(self):
        """
        :param Query: ES查询条件JSON
        :type Query: str
        """
        self.Query = None


    def _deserialize(self, params):
        self.Query = params.get("Query")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSearchExportListResponse(AbstractModel):
    """DescribeSearchExportList返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 导出的任务号
        :type TaskId: int
        :param DownloadUrl: 下载地址
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class DescribeSearchLogsRequest(AbstractModel):
    """DescribeSearchLogs请求参数结构体

    """


class DescribeSearchLogsResponse(AbstractModel):
    """DescribeSearchLogs返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 历史搜索记录
        :type Data: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeSearchTemplatesRequest(AbstractModel):
    """DescribeSearchTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSearchTemplatesResponse(AbstractModel):
    """DescribeSearchTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总数
        :type TotalCount: int
        :param List: 模板列表
        :type List: list of SearchTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = SearchTemplate()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecurityDynamicsRequest(AbstractModel):
    """DescribeSecurityDynamics请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 返回数量，默认为10，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityDynamicsResponse(AbstractModel):
    """DescribeSecurityDynamics返回参数结构体

    """

    def __init__(self):
        """
        :param SecurityDynamics: 安全事件消息数组。
        :type SecurityDynamics: list of SecurityDynamic
        :param TotalCount: 记录总数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SecurityDynamics = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityDynamics") is not None:
            self.SecurityDynamics = []
            for item in params.get("SecurityDynamics"):
                obj = SecurityDynamic()
                obj._deserialize(item)
                self.SecurityDynamics.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSecurityEventsCntRequest(AbstractModel):
    """DescribeSecurityEventsCnt请求参数结构体

    """


class DescribeSecurityEventsCntResponse(AbstractModel):
    """DescribeSecurityEventsCnt返回参数结构体

    """

    def __init__(self):
        """
        :param Malware: 木马文件相关风险事件
        :type Malware: :class:`tencentcloud.cwp.v20180228.models.SecurityEventInfo`
        :param HostLogin: 登录审计相关风险事件
        :type HostLogin: :class:`tencentcloud.cwp.v20180228.models.SecurityEventInfo`
        :param BruteAttack: 密码破解相关风险事件
        :type BruteAttack: :class:`tencentcloud.cwp.v20180228.models.SecurityEventInfo`
        :param RiskDns: 恶意请求相关风险事件
        :type RiskDns: :class:`tencentcloud.cwp.v20180228.models.SecurityEventInfo`
        :param Bash: 高危命令相关风险事件
        :type Bash: :class:`tencentcloud.cwp.v20180228.models.SecurityEventInfo`
        :param PrivilegeRules: 本地提权相关风险事件
        :type PrivilegeRules: :class:`tencentcloud.cwp.v20180228.models.SecurityEventInfo`
        :param ReverseShell: 反弹Shell相关风险事件
        :type ReverseShell: :class:`tencentcloud.cwp.v20180228.models.SecurityEventInfo`
        :param SysVul: 系统组件相关风险事件
        :type SysVul: :class:`tencentcloud.cwp.v20180228.models.SecurityEventInfo`
        :param WebVul: Web应用漏洞相关风险事件
        :type WebVul: :class:`tencentcloud.cwp.v20180228.models.SecurityEventInfo`
        :param EmergencyVul: 应急漏洞相关风险事件
        :type EmergencyVul: :class:`tencentcloud.cwp.v20180228.models.SecurityEventInfo`
        :param BaseLine: 安全基线相关风险事件
        :type BaseLine: :class:`tencentcloud.cwp.v20180228.models.SecurityEventInfo`
        :param AttackLogs: 攻击检测相关风险事件
        :type AttackLogs: :class:`tencentcloud.cwp.v20180228.models.SecurityEventInfo`
        :param EffectMachineCount: 受影响机器数
        :type EffectMachineCount: int
        :param EventsCount: 所有事件总数
        :type EventsCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Malware = None
        self.HostLogin = None
        self.BruteAttack = None
        self.RiskDns = None
        self.Bash = None
        self.PrivilegeRules = None
        self.ReverseShell = None
        self.SysVul = None
        self.WebVul = None
        self.EmergencyVul = None
        self.BaseLine = None
        self.AttackLogs = None
        self.EffectMachineCount = None
        self.EventsCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Malware") is not None:
            self.Malware = SecurityEventInfo()
            self.Malware._deserialize(params.get("Malware"))
        if params.get("HostLogin") is not None:
            self.HostLogin = SecurityEventInfo()
            self.HostLogin._deserialize(params.get("HostLogin"))
        if params.get("BruteAttack") is not None:
            self.BruteAttack = SecurityEventInfo()
            self.BruteAttack._deserialize(params.get("BruteAttack"))
        if params.get("RiskDns") is not None:
            self.RiskDns = SecurityEventInfo()
            self.RiskDns._deserialize(params.get("RiskDns"))
        if params.get("Bash") is not None:
            self.Bash = SecurityEventInfo()
            self.Bash._deserialize(params.get("Bash"))
        if params.get("PrivilegeRules") is not None:
            self.PrivilegeRules = SecurityEventInfo()
            self.PrivilegeRules._deserialize(params.get("PrivilegeRules"))
        if params.get("ReverseShell") is not None:
            self.ReverseShell = SecurityEventInfo()
            self.ReverseShell._deserialize(params.get("ReverseShell"))
        if params.get("SysVul") is not None:
            self.SysVul = SecurityEventInfo()
            self.SysVul._deserialize(params.get("SysVul"))
        if params.get("WebVul") is not None:
            self.WebVul = SecurityEventInfo()
            self.WebVul._deserialize(params.get("WebVul"))
        if params.get("EmergencyVul") is not None:
            self.EmergencyVul = SecurityEventInfo()
            self.EmergencyVul._deserialize(params.get("EmergencyVul"))
        if params.get("BaseLine") is not None:
            self.BaseLine = SecurityEventInfo()
            self.BaseLine._deserialize(params.get("BaseLine"))
        if params.get("AttackLogs") is not None:
            self.AttackLogs = SecurityEventInfo()
            self.AttackLogs._deserialize(params.get("AttackLogs"))
        self.EffectMachineCount = params.get("EffectMachineCount")
        self.EventsCount = params.get("EventsCount")
        self.RequestId = params.get("RequestId")


class DescribeSecurityTrendsRequest(AbstractModel):
    """DescribeSecurityTrends请求参数结构体

    """

    def __init__(self):
        """
        :param BeginDate: 开始时间，如：2021-07-10
        :type BeginDate: str
        :param EndDate: 结束时间，如：2021-07-10
        :type EndDate: str
        """
        self.BeginDate = None
        self.EndDate = None


    def _deserialize(self, params):
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityTrendsResponse(AbstractModel):
    """DescribeSecurityTrends返回参数结构体

    """

    def __init__(self):
        """
        :param Malwares: 木马事件统计数据数组。
        :type Malwares: list of SecurityTrend
        :param NonLocalLoginPlaces: 异地登录事件统计数据数组。
        :type NonLocalLoginPlaces: list of SecurityTrend
        :param BruteAttacks: 密码破解事件统计数据数组。
        :type BruteAttacks: list of SecurityTrend
        :param Vuls: 漏洞统计数据数组。
        :type Vuls: list of SecurityTrend
        :param BaseLines: 基线统计数据数组。
        :type BaseLines: list of SecurityTrend
        :param MaliciousRequests: 恶意请求统计数据数组。
        :type MaliciousRequests: list of SecurityTrend
        :param HighRiskBashs: 高危命令统计数据数组。
        :type HighRiskBashs: list of SecurityTrend
        :param ReverseShells: 反弹shell统计数据数组。
        :type ReverseShells: list of SecurityTrend
        :param PrivilegeEscalations: 本地提权统计数据数组。
        :type PrivilegeEscalations: list of SecurityTrend
        :param CyberAttacks: 网络攻击统计数据数组。
        :type CyberAttacks: list of SecurityTrend
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Malwares = None
        self.NonLocalLoginPlaces = None
        self.BruteAttacks = None
        self.Vuls = None
        self.BaseLines = None
        self.MaliciousRequests = None
        self.HighRiskBashs = None
        self.ReverseShells = None
        self.PrivilegeEscalations = None
        self.CyberAttacks = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Malwares") is not None:
            self.Malwares = []
            for item in params.get("Malwares"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.Malwares.append(obj)
        if params.get("NonLocalLoginPlaces") is not None:
            self.NonLocalLoginPlaces = []
            for item in params.get("NonLocalLoginPlaces"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.NonLocalLoginPlaces.append(obj)
        if params.get("BruteAttacks") is not None:
            self.BruteAttacks = []
            for item in params.get("BruteAttacks"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.BruteAttacks.append(obj)
        if params.get("Vuls") is not None:
            self.Vuls = []
            for item in params.get("Vuls"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.Vuls.append(obj)
        if params.get("BaseLines") is not None:
            self.BaseLines = []
            for item in params.get("BaseLines"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.BaseLines.append(obj)
        if params.get("MaliciousRequests") is not None:
            self.MaliciousRequests = []
            for item in params.get("MaliciousRequests"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.MaliciousRequests.append(obj)
        if params.get("HighRiskBashs") is not None:
            self.HighRiskBashs = []
            for item in params.get("HighRiskBashs"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.HighRiskBashs.append(obj)
        if params.get("ReverseShells") is not None:
            self.ReverseShells = []
            for item in params.get("ReverseShells"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.ReverseShells.append(obj)
        if params.get("PrivilegeEscalations") is not None:
            self.PrivilegeEscalations = []
            for item in params.get("PrivilegeEscalations"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.PrivilegeEscalations.append(obj)
        if params.get("CyberAttacks") is not None:
            self.CyberAttacks = []
            for item in params.get("CyberAttacks"):
                obj = SecurityTrend()
                obj._deserialize(item)
                self.CyberAttacks.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTagMachinesRequest(AbstractModel):
    """DescribeTagMachines请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 标签ID
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagMachinesResponse(AbstractModel):
    """DescribeTagMachines返回参数结构体

    """

    def __init__(self):
        """
        :param List: 列表数据
        :type List: list of TagMachine
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = TagMachine()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTagsRequest(AbstractModel):
    """DescribeTags请求参数结构体

    """

    def __init__(self):
        """
        :param MachineType: 云主机类型。
<li>CVM：表示虚拟主机</li>
<li>BM:  表示黑石物理机</li>
        :type MachineType: str
        :param MachineRegion: 机器所属地域。如：ap-guangzhou，ap-shanghai
        :type MachineRegion: str
        :param Filters: 过滤条件。
<li>Keywords - String - 是否必填：否 - 查询关键字(机器名称/机器IP </li>
<li>Status - String - 是否必填：否 - 客户端在线状态（OFFLINE: 离线 | ONLINE: 在线 | UNINSTALLED：未安装 | SHUTDOWN 已关机）</li>
<li>Version - String  是否必填：否 - 当前防护版本（ PRO_VERSION：专业版 | BASIC_VERSION：基础版）</li>
<li>Risk - String 是否必填: 否 - 风险主机( yes ) </li>
<li>Os -String 是否必填: 否 - 操作系统( DescribeMachineOsList 接口 值 )
每个过滤条件只支持一个值，暂不支持多个值“或”关系查询
        :type Filters: list of Filters
        """
        self.MachineType = None
        self.MachineRegion = None
        self.Filters = None


    def _deserialize(self, params):
        self.MachineType = params.get("MachineType")
        self.MachineRegion = params.get("MachineRegion")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagsResponse(AbstractModel):
    """DescribeTags返回参数结构体

    """

    def __init__(self):
        """
        :param List: 列表信息
        :type List: list of Tag
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = Tag()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUsualLoginPlacesRequest(AbstractModel):
    """DescribeUsualLoginPlaces请求参数结构体

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端UUID
        :type Uuid: str
        """
        self.Uuid = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsualLoginPlacesResponse(AbstractModel):
    """DescribeUsualLoginPlaces返回参数结构体

    """

    def __init__(self):
        """
        :param UsualLoginPlaces: 常用登录地数组
        :type UsualLoginPlaces: list of UsualPlace
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UsualLoginPlaces = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UsualLoginPlaces") is not None:
            self.UsualLoginPlaces = []
            for item in params.get("UsualLoginPlaces"):
                obj = UsualPlace()
                obj._deserialize(item)
                self.UsualLoginPlaces.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWebPageGeneralizeRequest(AbstractModel):
    """DescribeWebPageGeneralize请求参数结构体

    """


class DescribeWebPageGeneralizeResponse(AbstractModel):
    """DescribeWebPageGeneralize返回参数结构体

    """

    def __init__(self):
        """
        :param ProtectMonitor: 防护监测 0 未开启 1 已开启 2 异常
        :type ProtectMonitor: int
        :param ProtectDirNum: 防护目录数
        :type ProtectDirNum: int
        :param ProtectFileNum: 防护文件数
        :type ProtectFileNum: int
        :param TamperFileNum: 篡改文件数
        :type TamperFileNum: int
        :param TamperNum: 篡改数
        :type TamperNum: int
        :param ProtectToday: 今日防护数
        :type ProtectToday: int
        :param ProtectHostNum: 防护主机数
        :type ProtectHostNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProtectMonitor = None
        self.ProtectDirNum = None
        self.ProtectFileNum = None
        self.TamperFileNum = None
        self.TamperNum = None
        self.ProtectToday = None
        self.ProtectHostNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProtectMonitor = params.get("ProtectMonitor")
        self.ProtectDirNum = params.get("ProtectDirNum")
        self.ProtectFileNum = params.get("ProtectFileNum")
        self.TamperFileNum = params.get("TamperFileNum")
        self.TamperNum = params.get("TamperNum")
        self.ProtectToday = params.get("ProtectToday")
        self.ProtectHostNum = params.get("ProtectHostNum")
        self.RequestId = params.get("RequestId")


class EditBashRulesRequest(AbstractModel):
    """EditBashRules请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 规则名称
        :type Name: str
        :param Rule: 正则表达式
        :type Rule: str
        :param Id: 规则ID（新增时不填）
        :type Id: int
        :param Uuids: 客户端ID数组
        :type Uuids: list of str
        :param HostIp: 主机IP
        :type HostIp: str
        :param Level: 危险等级(0:无，1: 高危 2:中危 3: 低危)
        :type Level: int
        :param IsGlobal: 是否全局规则(默认否)：1-全局，0-非全局
        :type IsGlobal: int
        :param White: 0=黑名单， 1=白名单
        :type White: int
        :param EventId: 事件列表点击“加入白名单”时,需要传EventId 事件的id
        :type EventId: int
        :param DealOldEvents: 是否处理旧事件为白名单 0=不处理 1=处理
        :type DealOldEvents: int
        """
        self.Name = None
        self.Rule = None
        self.Id = None
        self.Uuids = None
        self.HostIp = None
        self.Level = None
        self.IsGlobal = None
        self.White = None
        self.EventId = None
        self.DealOldEvents = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Rule = params.get("Rule")
        self.Id = params.get("Id")
        self.Uuids = params.get("Uuids")
        self.HostIp = params.get("HostIp")
        self.Level = params.get("Level")
        self.IsGlobal = params.get("IsGlobal")
        self.White = params.get("White")
        self.EventId = params.get("EventId")
        self.DealOldEvents = params.get("DealOldEvents")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditBashRulesResponse(AbstractModel):
    """EditBashRules返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EditTagsRequest(AbstractModel):
    """EditTags请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 标签名
        :type Name: str
        :param Id: 标签ID
        :type Id: int
        :param Quuids: CVM主机ID
        :type Quuids: list of str
        """
        self.Name = None
        self.Id = None
        self.Quuids = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Id = params.get("Id")
        self.Quuids = params.get("Quuids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EditTagsResponse(AbstractModel):
    """EditTags返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EffectiveMachineInfo(AbstractModel):
    """批量导入机器信息.

    """

    def __init__(self):
        """
        :param MachineName: 机器名称
注意：此字段可能返回 null，表示取不到有效值。
        :type MachineName: str
        :param MachinePublicIp: 机器公网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type MachinePublicIp: str
        :param MachinePrivateIp: 机器内网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type MachinePrivateIp: str
        :param MachineTag: 机器标签
注意：此字段可能返回 null，表示取不到有效值。
        :type MachineTag: list of MachineTag
        :param Quuid: 机器Quuid
注意：此字段可能返回 null，表示取不到有效值。
        :type Quuid: str
        :param Uuid: 云镜Uuid
注意：此字段可能返回 null，表示取不到有效值。
        :type Uuid: str
        """
        self.MachineName = None
        self.MachinePublicIp = None
        self.MachinePrivateIp = None
        self.MachineTag = None
        self.Quuid = None
        self.Uuid = None


    def _deserialize(self, params):
        self.MachineName = params.get("MachineName")
        self.MachinePublicIp = params.get("MachinePublicIp")
        self.MachinePrivateIp = params.get("MachinePrivateIp")
        if params.get("MachineTag") is not None:
            self.MachineTag = []
            for item in params.get("MachineTag"):
                obj = MachineTag()
                obj._deserialize(item)
                self.MachineTag.append(obj)
        self.Quuid = params.get("Quuid")
        self.Uuid = params.get("Uuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportAssetCoreModuleListRequest(AbstractModel):
    """ExportAssetCoreModuleList请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤条件。
<li>Name- string - 是否必填：否 - 包名</li>
<li>User- string - 是否必填：否 - 用户</li>
        :type Filters: list of AssetFilters
        :param Order: 排序方式，asc升序 或 desc降序
        :type Order: str
        :param By: 排序依据:Size,ProcessCount,ModuleCount
        :type By: str
        :param Uuid: 服务器Uuid
        :type Uuid: str
        :param Quuid: 服务器Quuid
        :type Quuid: str
        """
        self.Filters = None
        self.Order = None
        self.By = None
        self.Uuid = None
        self.Quuid = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = AssetFilters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Order = params.get("Order")
        self.By = params.get("By")
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportAssetCoreModuleListResponse(AbstractModel):
    """ExportAssetCoreModuleList返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 异步下载任务ID，需要配合ExportTasks接口使用
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportAttackLogsRequest(AbstractModel):
    """ExportAttackLogs请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤条件。
<li>HttpMethod - String - 是否必填：否 - 攻击方法(POST|GET)</li>
<li>DateRange - String - 是否必填：否 - 时间范围(存储最近3个月的数据)，如最近一个月["2019-11-17", "2019-12-17"]</li>
<li>VulType - String 威胁类型 - 是否必填: 否</li>
<li>SrcIp - String 攻击源IP - 是否必填: 否</li>
<li>DstIp - String 攻击目标IP - 是否必填: 否</li>
<li>SrcPort - String 攻击源端口 - 是否必填: 否</li>
<li>DstPort - String 攻击目标端口 - 是否必填: 否</li>
        :type Filters: list of Filters
        :param Uuid: 主机安全客户端ID
        :type Uuid: str
        :param Quuid: 云主机机器ID
        :type Quuid: str
        """
        self.Filters = None
        self.Uuid = None
        self.Quuid = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportAttackLogsResponse(AbstractModel):
    """ExportAttackLogs返回参数结构体

    """

    def __init__(self):
        """
        :param DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param TaskId: 导出任务ID
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportBashEventsRequest(AbstractModel):
    """ExportBashEvents请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤参数
        :type Filters: list of Filters
        """
        self.Filters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportBashEventsResponse(AbstractModel):
    """ExportBashEvents返回参数结构体

    """

    def __init__(self):
        """
        :param DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param TaskId: 导出任务ID
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportBruteAttacksRequest(AbstractModel):
    """ExportBruteAttacks请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤参数
        :type Filters: list of Filters
        """
        self.Filters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportBruteAttacksResponse(AbstractModel):
    """ExportBruteAttacks返回参数结构体

    """

    def __init__(self):
        """
        :param DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param TaskId: 导出任务ID
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportMaliciousRequestsRequest(AbstractModel):
    """ExportMaliciousRequests请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤参数
        :type Filters: list of Filters
        """
        self.Filters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportMaliciousRequestsResponse(AbstractModel):
    """ExportMaliciousRequests返回参数结构体

    """

    def __init__(self):
        """
        :param DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class ExportMalwaresRequest(AbstractModel):
    """ExportMalwares请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 限制条数,默认10
        :type Limit: int
        :param Offset: 偏移量 默认0
        :type Offset: int
        :param Filters: 过滤参数。
<li>IpOrAlias - String - 是否必填：否 - 主机ip或别名筛选</li>
<li>FilePath - String - 是否必填：否 - 路径筛选</li>
<li>VirusName - String - 是否必填：否 - 描述筛选</li>
<li>CreateBeginTime - String - 是否必填：否 - 创建时间筛选-开始时间</li>
<li>CreateEndTime - String - 是否必填：否 - 创建时间筛选-结束时间</li>
<li>Status - String - 是否必填：否 - 状态筛选</li>
        :type Filters: list of Filters
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportMalwaresResponse(AbstractModel):
    """ExportMalwares返回参数结构体

    """

    def __init__(self):
        """
        :param DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param TaskId: 任务id
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportNonlocalLoginPlacesRequest(AbstractModel):
    """ExportNonlocalLoginPlaces请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: <li>Status - int - 是否必填：否 - 状态筛选1:正常登录；2：异地登录</li>
        :type Filters: list of Filter
        """
        self.Filters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportNonlocalLoginPlacesResponse(AbstractModel):
    """ExportNonlocalLoginPlaces返回参数结构体

    """

    def __init__(self):
        """
        :param DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param TaskId: 导出任务ID
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportPrivilegeEventsRequest(AbstractModel):
    """ExportPrivilegeEvents请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤参数
        :type Filters: list of Filters
        """
        self.Filters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportPrivilegeEventsResponse(AbstractModel):
    """ExportPrivilegeEvents返回参数结构体

    """

    def __init__(self):
        """
        :param DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param TaskId: 导出任务ID
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportReverseShellEventsRequest(AbstractModel):
    """ExportReverseShellEvents请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤参数
        :type Filters: list of Filters
        """
        self.Filters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportReverseShellEventsResponse(AbstractModel):
    """ExportReverseShellEvents返回参数结构体

    """

    def __init__(self):
        """
        :param DownloadUrl: 导出文件下载链接地址。
        :type DownloadUrl: str
        :param TaskId: 任务id
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportTasksRequest(AbstractModel):
    """ExportTasks请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportTasksResponse(AbstractModel):
    """ExportTasks返回参数结构体

    """

    def __init__(self):
        """
        :param Status: PENDING：正在生成下载链接，FINISHED：下载链接已生成，ERROR：网络异常等异常情况
        :type Status: str
        :param DownloadUrl: 下载链接
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class ExportVulDetectionExcelRequest(AbstractModel):
    """ExportVulDetectionExcel请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 本次漏洞检测任务id（不同于出参的导出本次漏洞检测Excel的任务Id）
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportVulDetectionExcelResponse(AbstractModel):
    """ExportVulDetectionExcel返回参数结构体

    """

    def __init__(self):
        """
        :param DownloadUrl: 导出文件下载链接地址
        :type DownloadUrl: str
        :param TaskId: 导出本次漏洞检测Excel的任务Id（不同于入参的本次漏洞检测任务id）
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ExportVulDetectionReportRequest(AbstractModel):
    """ExportVulDetectionReport请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 漏洞扫描任务id（不同于出参的导出检测报告的任务Id）
        :type TaskId: int
        :param Filters: 过滤参数
        :type Filters: list of Filters
        :param Limit: 需要返回的数量，默认为10，最大值为100
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self.TaskId = None
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filters()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportVulDetectionReportResponse(AbstractModel):
    """ExportVulDetectionReport返回参数结构体

    """

    def __init__(self):
        """
        :param DownloadUrl: 导出文件下载链接地址
        :type DownloadUrl: str
        :param TaskId: 导出检测报告的任务Id（不同于入参的漏洞扫描任务id）
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等

    若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    * 最多只能有5个Filter
    * 同一个Filter存在多个Values，Values值数量最多不能超过5个。

    """

    def __init__(self):
        """
        :param Name: 过滤键的名称。
        :type Name: str
        :param Values: 一个或者多个过滤值。
        :type Values: list of str
        :param ExactMatch: 模糊搜索
        :type ExactMatch: bool
        """
        self.Name = None
        self.Values = None
        self.ExactMatch = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        self.ExactMatch = params.get("ExactMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filters(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等

    若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        """
        :param Name: 过滤键的名称。
        :type Name: str
        :param Values: 一个或者多个过滤值。
        :type Values: list of str
        :param ExactMatch: 是否模糊匹配，前端框架会带上，可以不管
        :type ExactMatch: bool
        """
        self.Name = None
        self.Values = None
        self.ExactMatch = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        self.ExactMatch = params.get("ExactMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HistoryAccount(AbstractModel):
    """账号变更历史数据。

    """

    def __init__(self):
        """
        :param Id: 唯一ID。
        :type Id: int
        :param Uuid: 云镜客户端唯一Uuid。
        :type Uuid: str
        :param MachineIp: 主机内网IP。
        :type MachineIp: str
        :param MachineName: 主机名。
        :type MachineName: str
        :param Username: 帐号名。
        :type Username: str
        :param ModifyType: 帐号变更类型。
<li>CREATE：表示新增帐号</li>
<li>MODIFY：表示修改帐号</li>
<li>DELETE：表示删除帐号</li>
        :type ModifyType: str
        :param ModifyTime: 变更时间。
        :type ModifyTime: str
        """
        self.Id = None
        self.Uuid = None
        self.MachineIp = None
        self.MachineName = None
        self.Username = None
        self.ModifyType = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.MachineIp = params.get("MachineIp")
        self.MachineName = params.get("MachineName")
        self.Username = params.get("Username")
        self.ModifyType = params.get("ModifyType")
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IgnoreImpactedHostsRequest(AbstractModel):
    """IgnoreImpactedHosts请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 漏洞ID数组。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IgnoreImpactedHostsResponse(AbstractModel):
    """IgnoreImpactedHosts返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class InquiryPriceOpenProVersionPrepaidRequest(AbstractModel):
    """InquiryPriceOpenProVersionPrepaid请求参数结构体

    """

    def __init__(self):
        """
        :param ChargePrepaid: 预付费模式(包年包月)参数设置。
        :type ChargePrepaid: :class:`tencentcloud.cwp.v20180228.models.ChargePrepaid`
        :param Machines: 需要开通专业版机器列表数组。
        :type Machines: list of ProVersionMachine
        """
        self.ChargePrepaid = None
        self.Machines = None


    def _deserialize(self, params):
        if params.get("ChargePrepaid") is not None:
            self.ChargePrepaid = ChargePrepaid()
            self.ChargePrepaid._deserialize(params.get("ChargePrepaid"))
        if params.get("Machines") is not None:
            self.Machines = []
            for item in params.get("Machines"):
                obj = ProVersionMachine()
                obj._deserialize(item)
                self.Machines.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceOpenProVersionPrepaidResponse(AbstractModel):
    """InquiryPriceOpenProVersionPrepaid返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalPrice: 预支费用的原价，单位：元。
        :type OriginalPrice: float
        :param DiscountPrice: 预支费用的折扣价，单位：元。
        :type DiscountPrice: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OriginalPrice = None
        self.DiscountPrice = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.DiscountPrice = params.get("DiscountPrice")
        self.RequestId = params.get("RequestId")


class LoginWhiteLists(AbstractModel):
    """异地登录白名单

    """

    def __init__(self):
        """
        :param Id: 记录ID
        :type Id: int
        :param Uuid: 云镜客户端ID
        :type Uuid: str
        :param Places: 白名单地域
        :type Places: list of Place
        :param UserName: 白名单用户（多个用户逗号隔开）
        :type UserName: str
        :param SrcIp: 白名单IP（多个IP逗号隔开）
        :type SrcIp: str
        :param IsGlobal: 是否为全局规则
        :type IsGlobal: bool
        :param CreateTime: 创建白名单时间
        :type CreateTime: str
        :param ModifyTime: 修改白名单时间
        :type ModifyTime: str
        :param MachineName: 机器名
        :type MachineName: str
        :param HostIp: 机器IP
        :type HostIp: str
        :param StartTime: 起始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        """
        self.Id = None
        self.Uuid = None
        self.Places = None
        self.UserName = None
        self.SrcIp = None
        self.IsGlobal = None
        self.CreateTime = None
        self.ModifyTime = None
        self.MachineName = None
        self.HostIp = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        if params.get("Places") is not None:
            self.Places = []
            for item in params.get("Places"):
                obj = Place()
                obj._deserialize(item)
                self.Places.append(obj)
        self.UserName = params.get("UserName")
        self.SrcIp = params.get("SrcIp")
        self.IsGlobal = params.get("IsGlobal")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        self.MachineName = params.get("MachineName")
        self.HostIp = params.get("HostIp")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Machine(AbstractModel):
    """主机列表

    """

    def __init__(self):
        """
        :param MachineName: 主机名称。
        :type MachineName: str
        :param MachineOs: 主机系统。
        :type MachineOs: str
        :param MachineStatus: 主机状态。
<li>OFFLINE: 离线  </li>
<li>ONLINE: 在线</li>
<li>SHUTDOWN: 已关机</li>
        :type MachineStatus: str
        :param Uuid: 云镜客户端唯一Uuid，若客户端长时间不在线将返回空字符。
        :type Uuid: str
        :param Quuid: CVM或BM机器唯一Uuid。
        :type Quuid: str
        :param VulNum: 漏洞数。
        :type VulNum: int
        :param MachineIp: 主机IP。
        :type MachineIp: str
        :param IsProVersion: 是否是专业版。
<li>true： 是</li>
<li>false：否</li>
        :type IsProVersion: bool
        :param MachineWanIp: 主机外网IP。
        :type MachineWanIp: str
        :param PayMode: 主机状态。
<li>POSTPAY: 表示后付费，即按量计费  </li>
<li>PREPAY: 表示预付费，即包年包月</li>
        :type PayMode: str
        :param MalwareNum: 木马数。
        :type MalwareNum: int
        :param Tag: 标签信息
        :type Tag: list of MachineTag
        :param BaselineNum: 基线风险数。
        :type BaselineNum: int
        :param CyberAttackNum: 网络风险数。
        :type CyberAttackNum: int
        :param SecurityStatus: 风险状态。
<li>SAFE：安全</li>
<li>RISK：风险</li>
<li>UNKNOWN：未知</li>
        :type SecurityStatus: str
        :param InvasionNum: 入侵事件数
        :type InvasionNum: int
        :param RegionInfo: 地域信息
        :type RegionInfo: :class:`tencentcloud.cwp.v20180228.models.RegionInfo`
        :param InstanceState: 实例状态 TERMINATED_PRO_VERSION 已销毁
        :type InstanceState: str
        :param LicenseStatus: 授权状态 1 授权 0 未授权
        :type LicenseStatus: int
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param HasAssetScan: 是否有资产扫描接口，0无，1有
        :type HasAssetScan: int
        """
        self.MachineName = None
        self.MachineOs = None
        self.MachineStatus = None
        self.Uuid = None
        self.Quuid = None
        self.VulNum = None
        self.MachineIp = None
        self.IsProVersion = None
        self.MachineWanIp = None
        self.PayMode = None
        self.MalwareNum = None
        self.Tag = None
        self.BaselineNum = None
        self.CyberAttackNum = None
        self.SecurityStatus = None
        self.InvasionNum = None
        self.RegionInfo = None
        self.InstanceState = None
        self.LicenseStatus = None
        self.ProjectId = None
        self.HasAssetScan = None


    def _deserialize(self, params):
        self.MachineName = params.get("MachineName")
        self.MachineOs = params.get("MachineOs")
        self.MachineStatus = params.get("MachineStatus")
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        self.VulNum = params.get("VulNum")
        self.MachineIp = params.get("MachineIp")
        self.IsProVersion = params.get("IsProVersion")
        self.MachineWanIp = params.get("MachineWanIp")
        self.PayMode = params.get("PayMode")
        self.MalwareNum = params.get("MalwareNum")
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = MachineTag()
                obj._deserialize(item)
                self.Tag.append(obj)
        self.BaselineNum = params.get("BaselineNum")
        self.CyberAttackNum = params.get("CyberAttackNum")
        self.SecurityStatus = params.get("SecurityStatus")
        self.InvasionNum = params.get("InvasionNum")
        if params.get("RegionInfo") is not None:
            self.RegionInfo = RegionInfo()
            self.RegionInfo._deserialize(params.get("RegionInfo"))
        self.InstanceState = params.get("InstanceState")
        self.LicenseStatus = params.get("LicenseStatus")
        self.ProjectId = params.get("ProjectId")
        self.HasAssetScan = params.get("HasAssetScan")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachineTag(AbstractModel):
    """服务器标签信息

    """

    def __init__(self):
        """
        :param Rid: 关联标签ID
        :type Rid: int
        :param Name: 标签名
        :type Name: str
        :param TagId: 标签ID
        :type TagId: int
        """
        self.Rid = None
        self.Name = None
        self.TagId = None


    def _deserialize(self, params):
        self.Rid = params.get("Rid")
        self.Name = params.get("Name")
        self.TagId = params.get("TagId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MalwareInfo(AbstractModel):
    """恶意文件详情

    """

    def __init__(self):
        """
        :param VirusName: 病毒名称
        :type VirusName: str
        :param FileSize: 文件大小
        :type FileSize: int
        :param MD5: 文件MD5
        :type MD5: str
        :param FilePath: 文件地址
        :type FilePath: str
        :param FileCreateTime: 首次运行时间
        :type FileCreateTime: str
        :param FileModifierTime: 最近一次运行时间
        :type FileModifierTime: str
        :param HarmDescribe: 危害描述
        :type HarmDescribe: str
        :param SuggestScheme: 建议方案
        :type SuggestScheme: str
        :param ServersName: 服务器名称
        :type ServersName: str
        :param HostIp: 服务器IP
        :type HostIp: str
        :param ProcessName: 进程名称
        :type ProcessName: str
        :param ProcessID: 进程ID
        :type ProcessID: str
        :param Tags: 标签特性
        :type Tags: list of str
        :param Breadth: 影响广度 // 暂时不提供
注意：此字段可能返回 null，表示取不到有效值。
        :type Breadth: str
        :param Heat: 查询热度 // 暂时不提供
注意：此字段可能返回 null，表示取不到有效值。
        :type Heat: str
        :param Id: 唯一ID
        :type Id: int
        :param FileName: 文件名称
        :type FileName: str
        :param CreateTime: 首次发现时间
        :type CreateTime: str
        :param LatestScanTime: 最近扫描时间
        :type LatestScanTime: str
        """
        self.VirusName = None
        self.FileSize = None
        self.MD5 = None
        self.FilePath = None
        self.FileCreateTime = None
        self.FileModifierTime = None
        self.HarmDescribe = None
        self.SuggestScheme = None
        self.ServersName = None
        self.HostIp = None
        self.ProcessName = None
        self.ProcessID = None
        self.Tags = None
        self.Breadth = None
        self.Heat = None
        self.Id = None
        self.FileName = None
        self.CreateTime = None
        self.LatestScanTime = None


    def _deserialize(self, params):
        self.VirusName = params.get("VirusName")
        self.FileSize = params.get("FileSize")
        self.MD5 = params.get("MD5")
        self.FilePath = params.get("FilePath")
        self.FileCreateTime = params.get("FileCreateTime")
        self.FileModifierTime = params.get("FileModifierTime")
        self.HarmDescribe = params.get("HarmDescribe")
        self.SuggestScheme = params.get("SuggestScheme")
        self.ServersName = params.get("ServersName")
        self.HostIp = params.get("HostIp")
        self.ProcessName = params.get("ProcessName")
        self.ProcessID = params.get("ProcessID")
        self.Tags = params.get("Tags")
        self.Breadth = params.get("Breadth")
        self.Heat = params.get("Heat")
        self.Id = params.get("Id")
        self.FileName = params.get("FileName")
        self.CreateTime = params.get("CreateTime")
        self.LatestScanTime = params.get("LatestScanTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoOpenProVersionConfigRequest(AbstractModel):
    """ModifyAutoOpenProVersionConfig请求参数结构体

    """

    def __init__(self):
        """
        :param Status: 设置自动开通状态。
<li>CLOSE：关闭</li>
<li>OPEN：打开</li>
        :type Status: str
        """
        self.Status = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoOpenProVersionConfigResponse(AbstractModel):
    """ModifyAutoOpenProVersionConfig返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMalwareTimingScanSettingsRequest(AbstractModel):
    """ModifyMalwareTimingScanSettings请求参数结构体

    """

    def __init__(self):
        """
        :param CheckPattern: 检测模式 0 全盘检测  1快速检测
        :type CheckPattern: int
        :param StartTime: 检测周期 开始时间，如：02:00:00
        :type StartTime: str
        :param EndTime: 检测周期 超时结束时间，如：04:00:00
        :type EndTime: str
        :param IsGlobal: 是否全部服务器 1 全部 2 自选
        :type IsGlobal: int
        :param EnableScan: 定时检测开关 0 关闭 1开启
        :type EnableScan: int
        :param MonitoringPattern: 监控模式 0 标准 1深度
        :type MonitoringPattern: int
        :param Cycle: 扫描周期 默认每天 1
        :type Cycle: int
        :param RealTimeMonitoring: 实时监控 0 关闭 1开启
        :type RealTimeMonitoring: int
        :param QuuidList: 自选服务器时必须 主机quuid的string数组
        :type QuuidList: list of str
        :param AutoIsolation: 是否自动隔离 1隔离 0 不隔离
        :type AutoIsolation: int
        """
        self.CheckPattern = None
        self.StartTime = None
        self.EndTime = None
        self.IsGlobal = None
        self.EnableScan = None
        self.MonitoringPattern = None
        self.Cycle = None
        self.RealTimeMonitoring = None
        self.QuuidList = None
        self.AutoIsolation = None


    def _deserialize(self, params):
        self.CheckPattern = params.get("CheckPattern")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.IsGlobal = params.get("IsGlobal")
        self.EnableScan = params.get("EnableScan")
        self.MonitoringPattern = params.get("MonitoringPattern")
        self.Cycle = params.get("Cycle")
        self.RealTimeMonitoring = params.get("RealTimeMonitoring")
        self.QuuidList = params.get("QuuidList")
        self.AutoIsolation = params.get("AutoIsolation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMalwareTimingScanSettingsResponse(AbstractModel):
    """ModifyMalwareTimingScanSettings返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyProVersionRenewFlagRequest(AbstractModel):
    """ModifyProVersionRenewFlag请求参数结构体

    """

    def __init__(self):
        """
        :param RenewFlag: 自动续费标识。取值范围：
<li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费</li>
<li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费</li>
<li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费</li>
        :type RenewFlag: str
        :param Quuid: 主机唯一ID，对应CVM的uuid、BM的instanceId。
        :type Quuid: str
        """
        self.RenewFlag = None
        self.Quuid = None


    def _deserialize(self, params):
        self.RenewFlag = params.get("RenewFlag")
        self.Quuid = params.get("Quuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProVersionRenewFlagResponse(AbstractModel):
    """ModifyProVersionRenewFlag返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyWebPageProtectSettingRequest(AbstractModel):
    """ModifyWebPageProtectSetting请求参数结构体

    """

    def __init__(self):
        """
        :param ModifyType: 需要操作的类型1 目录名称 2 防护文件类型
        :type ModifyType: int
        :param Value: 提交值
        :type Value: str
        :param Id: 配置对应的protect_path
        :type Id: str
        """
        self.ModifyType = None
        self.Value = None
        self.Id = None


    def _deserialize(self, params):
        self.ModifyType = params.get("ModifyType")
        self.Value = params.get("Value")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWebPageProtectSettingResponse(AbstractModel):
    """ModifyWebPageProtectSetting返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OpenPortStatistics(AbstractModel):
    """端口统计列表

    """

    def __init__(self):
        """
        :param Port: 端口号
        :type Port: int
        :param MachineNum: 主机数量
        :type MachineNum: int
        """
        self.Port = None
        self.MachineNum = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.MachineNum = params.get("MachineNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenProVersionPrepaidRequest(AbstractModel):
    """OpenProVersionPrepaid请求参数结构体

    """

    def __init__(self):
        """
        :param ChargePrepaid: 购买相关参数。
        :type ChargePrepaid: :class:`tencentcloud.cwp.v20180228.models.ChargePrepaid`
        :param Machines: 需要开通专业版主机信息数组。
        :type Machines: list of ProVersionMachine
        """
        self.ChargePrepaid = None
        self.Machines = None


    def _deserialize(self, params):
        if params.get("ChargePrepaid") is not None:
            self.ChargePrepaid = ChargePrepaid()
            self.ChargePrepaid._deserialize(params.get("ChargePrepaid"))
        if params.get("Machines") is not None:
            self.Machines = []
            for item in params.get("Machines"):
                obj = ProVersionMachine()
                obj._deserialize(item)
                self.Machines.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenProVersionPrepaidResponse(AbstractModel):
    """OpenProVersionPrepaid返回参数结构体

    """

    def __init__(self):
        """
        :param DealIds: 订单ID列表。
        :type DealIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealIds = params.get("DealIds")
        self.RequestId = params.get("RequestId")


class OpenProVersionRequest(AbstractModel):
    """OpenProVersion请求参数结构体

    """

    def __init__(self):
        """
        :param MachineType: 云主机类型。
<li>CVM：表示虚拟主机</li>
<li>BM:  表示黑石物理机</li>
        :type MachineType: str
        :param MachineRegion: 机器所属地域。
如：ap-guangzhou，ap-shanghai
        :type MachineRegion: str
        :param Quuids: 主机唯一标识Uuid数组。
黑石的InstanceId，CVM的Uuid
        :type Quuids: list of str
        :param ActivityId: 活动ID。
        :type ActivityId: int
        """
        self.MachineType = None
        self.MachineRegion = None
        self.Quuids = None
        self.ActivityId = None


    def _deserialize(self, params):
        self.MachineType = params.get("MachineType")
        self.MachineRegion = params.get("MachineRegion")
        self.Quuids = params.get("Quuids")
        self.ActivityId = params.get("ActivityId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenProVersionResponse(AbstractModel):
    """OpenProVersion返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OsName(AbstractModel):
    """操作系统名称

    """

    def __init__(self):
        """
        :param Name: 系统名称
        :type Name: str
        :param MachineOSType: 操作系统类型枚举值
        :type MachineOSType: int
        """
        self.Name = None
        self.MachineOSType = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.MachineOSType = params.get("MachineOSType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Place(AbstractModel):
    """登录地信息

    """

    def __init__(self):
        """
        :param CityId: 城市 ID。
        :type CityId: int
        :param ProvinceId: 省份 ID。
        :type ProvinceId: int
        :param CountryId: 国家ID，暂只支持国内：1。
        :type CountryId: int
        :param Location: 位置名称
        :type Location: str
        """
        self.CityId = None
        self.ProvinceId = None
        self.CountryId = None
        self.Location = None


    def _deserialize(self, params):
        self.CityId = params.get("CityId")
        self.ProvinceId = params.get("ProvinceId")
        self.CountryId = params.get("CountryId")
        self.Location = params.get("Location")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrivilegeEscalationProcess(AbstractModel):
    """本地提权数据

    """

    def __init__(self):
        """
        :param Id: 数据ID
        :type Id: int
        :param Uuid: 云镜ID
        :type Uuid: str
        :param Quuid: 主机ID
        :type Quuid: str
        :param Hostip: 主机内网IP
        :type Hostip: str
        :param ProcessName: 进程名
        :type ProcessName: str
        :param FullPath: 进程路径
        :type FullPath: str
        :param CmdLine: 执行命令
        :type CmdLine: str
        :param UserName: 用户名
        :type UserName: str
        :param UserGroup: 用户组
        :type UserGroup: str
        :param ProcFilePrivilege: 进程文件权限
        :type ProcFilePrivilege: str
        :param ParentProcName: 父进程名
        :type ParentProcName: str
        :param ParentProcUser: 父进程用户名
        :type ParentProcUser: str
        :param ParentProcGroup: 父进程用户组
        :type ParentProcGroup: str
        :param ParentProcPath: 父进程路径
        :type ParentProcPath: str
        :param ProcTree: 进程树
        :type ProcTree: str
        :param Status: 处理状态
        :type Status: int
        :param CreateTime: 发生时间
        :type CreateTime: str
        :param MachineName: 机器名
        :type MachineName: str
        """
        self.Id = None
        self.Uuid = None
        self.Quuid = None
        self.Hostip = None
        self.ProcessName = None
        self.FullPath = None
        self.CmdLine = None
        self.UserName = None
        self.UserGroup = None
        self.ProcFilePrivilege = None
        self.ParentProcName = None
        self.ParentProcUser = None
        self.ParentProcGroup = None
        self.ParentProcPath = None
        self.ProcTree = None
        self.Status = None
        self.CreateTime = None
        self.MachineName = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        self.Hostip = params.get("Hostip")
        self.ProcessName = params.get("ProcessName")
        self.FullPath = params.get("FullPath")
        self.CmdLine = params.get("CmdLine")
        self.UserName = params.get("UserName")
        self.UserGroup = params.get("UserGroup")
        self.ProcFilePrivilege = params.get("ProcFilePrivilege")
        self.ParentProcName = params.get("ParentProcName")
        self.ParentProcUser = params.get("ParentProcUser")
        self.ParentProcGroup = params.get("ParentProcGroup")
        self.ParentProcPath = params.get("ParentProcPath")
        self.ProcTree = params.get("ProcTree")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.MachineName = params.get("MachineName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrivilegeRule(AbstractModel):
    """本地提权规则

    """

    def __init__(self):
        """
        :param Id: 规则ID
        :type Id: int
        :param Uuid: 客户端ID
        :type Uuid: str
        :param ProcessName: 进程名
        :type ProcessName: str
        :param SMode: 是否S权限
        :type SMode: int
        :param Operator: 操作人
        :type Operator: str
        :param IsGlobal: 是否全局规则
        :type IsGlobal: int
        :param Status: 状态(0: 有效 1: 无效)
        :type Status: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ModifyTime: 修改时间
        :type ModifyTime: str
        :param Hostip: 主机IP
        :type Hostip: str
        """
        self.Id = None
        self.Uuid = None
        self.ProcessName = None
        self.SMode = None
        self.Operator = None
        self.IsGlobal = None
        self.Status = None
        self.CreateTime = None
        self.ModifyTime = None
        self.Hostip = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.ProcessName = params.get("ProcessName")
        self.SMode = params.get("SMode")
        self.Operator = params.get("Operator")
        self.IsGlobal = params.get("IsGlobal")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        self.Hostip = params.get("Hostip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProVersionMachine(AbstractModel):
    """需要开通专业版机器信息。

    """

    def __init__(self):
        """
        :param MachineType: 主机类型。
<li>CVM: 虚拟主机</li>
<li>BM: 黑石物理机</li>
        :type MachineType: str
        :param MachineRegion: 主机所在地域。
如：ap-guangzhou、ap-beijing
        :type MachineRegion: str
        :param Quuid: 主机唯一标识Uuid。
黑石的InstanceId，CVM的Uuid
        :type Quuid: str
        """
        self.MachineType = None
        self.MachineRegion = None
        self.Quuid = None


    def _deserialize(self, params):
        self.MachineType = params.get("MachineType")
        self.MachineRegion = params.get("MachineRegion")
        self.Quuid = params.get("Quuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProcessStatistics(AbstractModel):
    """进程数据统计数据。

    """

    def __init__(self):
        """
        :param ProcessName: 进程名。
        :type ProcessName: str
        :param MachineNum: 主机数量。
        :type MachineNum: int
        """
        self.ProcessName = None
        self.MachineNum = None


    def _deserialize(self, params):
        self.ProcessName = params.get("ProcessName")
        self.MachineNum = params.get("MachineNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtectHostConfig(AbstractModel):
    """防护机器信息

    """

    def __init__(self):
        """
        :param Quuid: 机器唯一ID
        :type Quuid: str
        :param ProtectSwitch: 防护开关 0  关闭 1开启
        :type ProtectSwitch: int
        :param AutoRecovery: 自动恢复开关 0 关闭 1开启
        :type AutoRecovery: int
        """
        self.Quuid = None
        self.ProtectSwitch = None
        self.AutoRecovery = None


    def _deserialize(self, params):
        self.Quuid = params.get("Quuid")
        self.ProtectSwitch = params.get("ProtectSwitch")
        self.AutoRecovery = params.get("AutoRecovery")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverMalwaresRequest(AbstractModel):
    """RecoverMalwares请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 木马Id数组（最大100条）
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverMalwaresResponse(AbstractModel):
    """RecoverMalwares返回参数结构体

    """

    def __init__(self):
        """
        :param SuccessIds: 恢复成功id数组，若无则返回空数组
        :type SuccessIds: list of int non-negative
        :param FailedIds: 恢复失败id数组，若无则返回空数组
        :type FailedIds: list of int non-negative
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessIds = None
        self.FailedIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessIds = params.get("SuccessIds")
        self.FailedIds = params.get("FailedIds")
        self.RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """地域信息

    """

    def __init__(self):
        """
        :param Region: 地域标志，如 ap-guangzhou，ap-shanghai，ap-beijing
        :type Region: str
        :param RegionName: 地域中文名，如华南地区（广州），华东地区（上海金融），华北地区（北京）
        :type RegionName: str
        :param RegionId: 地域ID
        :type RegionId: int
        :param RegionCode: 地域代码，如 gz，sh，bj
        :type RegionCode: str
        :param RegionNameEn: 地域英文名
        :type RegionNameEn: str
        """
        self.Region = None
        self.RegionName = None
        self.RegionId = None
        self.RegionCode = None
        self.RegionNameEn = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionName = params.get("RegionName")
        self.RegionId = params.get("RegionId")
        self.RegionCode = params.get("RegionCode")
        self.RegionNameEn = params.get("RegionNameEn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewProVersionRequest(AbstractModel):
    """RenewProVersion请求参数结构体

    """

    def __init__(self):
        """
        :param ChargePrepaid: 购买相关参数。
        :type ChargePrepaid: :class:`tencentcloud.cwp.v20180228.models.ChargePrepaid`
        :param Quuid: 主机唯一ID，对应CVM的uuid、BM的InstanceId。
        :type Quuid: str
        """
        self.ChargePrepaid = None
        self.Quuid = None


    def _deserialize(self, params):
        if params.get("ChargePrepaid") is not None:
            self.ChargePrepaid = ChargePrepaid()
            self.ChargePrepaid._deserialize(params.get("ChargePrepaid"))
        self.Quuid = params.get("Quuid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewProVersionResponse(AbstractModel):
    """RenewProVersion返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RescanImpactedHostRequest(AbstractModel):
    """RescanImpactedHost请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 漏洞ID。
        :type Id: int
        """
        self.Id = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RescanImpactedHostResponse(AbstractModel):
    """RescanImpactedHost返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReverseShell(AbstractModel):
    """反弹Shell数据

    """

    def __init__(self):
        """
        :param Id: ID
        :type Id: int
        :param Uuid: 云镜UUID
        :type Uuid: str
        :param Quuid: 主机ID
        :type Quuid: str
        :param Hostip: 主机内网IP
        :type Hostip: str
        :param DstIp: 目标IP
        :type DstIp: str
        :param DstPort: 目标端口
        :type DstPort: int
        :param ProcessName: 进程名
        :type ProcessName: str
        :param FullPath: 进程路径
        :type FullPath: str
        :param CmdLine: 命令详情
        :type CmdLine: str
        :param UserName: 执行用户
        :type UserName: str
        :param UserGroup: 执行用户组
        :type UserGroup: str
        :param ParentProcName: 父进程名
        :type ParentProcName: str
        :param ParentProcUser: 父进程用户
        :type ParentProcUser: str
        :param ParentProcGroup: 父进程用户组
        :type ParentProcGroup: str
        :param ParentProcPath: 父进程路径
        :type ParentProcPath: str
        :param Status: 处理状态
        :type Status: int
        :param CreateTime: 产生时间
        :type CreateTime: str
        :param MachineName: 主机名
        :type MachineName: str
        :param ProcTree: 进程树
        :type ProcTree: str
        """
        self.Id = None
        self.Uuid = None
        self.Quuid = None
        self.Hostip = None
        self.DstIp = None
        self.DstPort = None
        self.ProcessName = None
        self.FullPath = None
        self.CmdLine = None
        self.UserName = None
        self.UserGroup = None
        self.ParentProcName = None
        self.ParentProcUser = None
        self.ParentProcGroup = None
        self.ParentProcPath = None
        self.Status = None
        self.CreateTime = None
        self.MachineName = None
        self.ProcTree = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        self.Hostip = params.get("Hostip")
        self.DstIp = params.get("DstIp")
        self.DstPort = params.get("DstPort")
        self.ProcessName = params.get("ProcessName")
        self.FullPath = params.get("FullPath")
        self.CmdLine = params.get("CmdLine")
        self.UserName = params.get("UserName")
        self.UserGroup = params.get("UserGroup")
        self.ParentProcName = params.get("ParentProcName")
        self.ParentProcUser = params.get("ParentProcUser")
        self.ParentProcGroup = params.get("ParentProcGroup")
        self.ParentProcPath = params.get("ParentProcPath")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.MachineName = params.get("MachineName")
        self.ProcTree = params.get("ProcTree")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReverseShellRule(AbstractModel):
    """反弹Shell规则

    """

    def __init__(self):
        """
        :param Id: 规则ID
        :type Id: int
        :param Uuid: 客户端ID
        :type Uuid: str
        :param ProcessName: 进程名称
        :type ProcessName: str
        :param DestIp: 目标IP
        :type DestIp: str
        :param DestPort: 目标端口
        :type DestPort: str
        :param Operator: 操作人
        :type Operator: str
        :param IsGlobal: 是否全局规则
        :type IsGlobal: int
        :param Status: 状态 (0: 有效 1: 无效)
        :type Status: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ModifyTime: 修改时间
        :type ModifyTime: str
        :param Hostip: 主机IP
        :type Hostip: str
        """
        self.Id = None
        self.Uuid = None
        self.ProcessName = None
        self.DestIp = None
        self.DestPort = None
        self.Operator = None
        self.IsGlobal = None
        self.Status = None
        self.CreateTime = None
        self.ModifyTime = None
        self.Hostip = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.ProcessName = params.get("ProcessName")
        self.DestIp = params.get("DestIp")
        self.DestPort = params.get("DestPort")
        self.Operator = params.get("Operator")
        self.IsGlobal = params.get("IsGlobal")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        self.Hostip = params.get("Hostip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskDnsList(AbstractModel):
    """恶意请求列表

    """

    def __init__(self):
        """
        :param Url: 对外访问域名
        :type Url: str
        :param AccessCount: 访问次数
        :type AccessCount: int
        :param ProcessName: 进程名
        :type ProcessName: str
        :param ProcessMd5: 进程MD5
        :type ProcessMd5: str
        :param GlobalRuleId: 是否为全局规则，0否，1是
        :type GlobalRuleId: int
        :param UserRuleId: 用户规则id
        :type UserRuleId: int
        :param Status: 状态；0-待处理，2-已加白，3-非信任状态
        :type Status: int
        :param CreateTime: 首次访问时间
        :type CreateTime: str
        :param MergeTime: 最近访问时间
        :type MergeTime: str
        :param Quuid: 唯一 Quuid
        :type Quuid: str
        :param HostIp: 主机ip
        :type HostIp: str
        :param Alias: 别名
        :type Alias: str
        :param Description: 描述
        :type Description: str
        :param Id: 唯一ID
        :type Id: int
        :param Reference: 参考
        :type Reference: str
        :param CmdLine: 命令行
        :type CmdLine: str
        :param Pid: 进程号
        :type Pid: int
        :param Uuid: 唯一UUID
        :type Uuid: str
        :param SuggestScheme: 建议方案
        :type SuggestScheme: str
        :param Tags: 标签特性
        :type Tags: list of str
        """
        self.Url = None
        self.AccessCount = None
        self.ProcessName = None
        self.ProcessMd5 = None
        self.GlobalRuleId = None
        self.UserRuleId = None
        self.Status = None
        self.CreateTime = None
        self.MergeTime = None
        self.Quuid = None
        self.HostIp = None
        self.Alias = None
        self.Description = None
        self.Id = None
        self.Reference = None
        self.CmdLine = None
        self.Pid = None
        self.Uuid = None
        self.SuggestScheme = None
        self.Tags = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.AccessCount = params.get("AccessCount")
        self.ProcessName = params.get("ProcessName")
        self.ProcessMd5 = params.get("ProcessMd5")
        self.GlobalRuleId = params.get("GlobalRuleId")
        self.UserRuleId = params.get("UserRuleId")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.MergeTime = params.get("MergeTime")
        self.Quuid = params.get("Quuid")
        self.HostIp = params.get("HostIp")
        self.Alias = params.get("Alias")
        self.Description = params.get("Description")
        self.Id = params.get("Id")
        self.Reference = params.get("Reference")
        self.CmdLine = params.get("CmdLine")
        self.Pid = params.get("Pid")
        self.Uuid = params.get("Uuid")
        self.SuggestScheme = params.get("SuggestScheme")
        self.Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanAssetRequest(AbstractModel):
    """ScanAsset请求参数结构体

    """

    def __init__(self):
        """
        :param AssetTypeIds: 资产指纹类型id列表
        :type AssetTypeIds: list of int non-negative
        :param Quuids: Quuid列表
        :type Quuids: list of str
        """
        self.AssetTypeIds = None
        self.Quuids = None


    def _deserialize(self, params):
        self.AssetTypeIds = params.get("AssetTypeIds")
        self.Quuids = params.get("Quuids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanAssetResponse(AbstractModel):
    """ScanAsset返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ScanTaskDetails(AbstractModel):
    """扫描任务详情列表信息

    """

    def __init__(self):
        """
        :param HostIp: 服务器IP
        :type HostIp: str
        :param HostName: 服务器名称
        :type HostName: str
        :param OsName: 操作系统
        :type OsName: str
        :param RiskNum: 风险数量
        :type RiskNum: int
        :param ScanBeginTime: 扫描开始时间
        :type ScanBeginTime: str
        :param ScanEndTime: 扫描结束时间
        :type ScanEndTime: str
        :param Uuid: 唯一Uuid
        :type Uuid: str
        :param Quuid: 唯一Quuid
        :type Quuid: str
        :param Status: 状态码
        :type Status: str
        :param Description: 描述
        :type Description: str
        :param Id: id唯一
        :type Id: int
        :param FailType: 失败详情
        :type FailType: int
        """
        self.HostIp = None
        self.HostName = None
        self.OsName = None
        self.RiskNum = None
        self.ScanBeginTime = None
        self.ScanEndTime = None
        self.Uuid = None
        self.Quuid = None
        self.Status = None
        self.Description = None
        self.Id = None
        self.FailType = None


    def _deserialize(self, params):
        self.HostIp = params.get("HostIp")
        self.HostName = params.get("HostName")
        self.OsName = params.get("OsName")
        self.RiskNum = params.get("RiskNum")
        self.ScanBeginTime = params.get("ScanBeginTime")
        self.ScanEndTime = params.get("ScanEndTime")
        self.Uuid = params.get("Uuid")
        self.Quuid = params.get("Quuid")
        self.Status = params.get("Status")
        self.Description = params.get("Description")
        self.Id = params.get("Id")
        self.FailType = params.get("FailType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanVulAgainRequest(AbstractModel):
    """ScanVulAgain请求参数结构体

    """

    def __init__(self):
        """
        :param EventIds: 漏洞事件id串，多个用英文逗号分隔
        :type EventIds: str
        :param Uuids: 重新检查的机器uuid,多个逗号分隔
        :type Uuids: str
        """
        self.EventIds = None
        self.Uuids = None


    def _deserialize(self, params):
        self.EventIds = params.get("EventIds")
        self.Uuids = params.get("Uuids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanVulAgainResponse(AbstractModel):
    """ScanVulAgain返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ScanVulRequest(AbstractModel):
    """ScanVul请求参数结构体

    """

    def __init__(self):
        """
        :param VulCategories: 漏洞类型：1: web应用漏洞 2:系统组件漏洞 (多选英文;分隔)
        :type VulCategories: str
        :param VulLevels: 危害等级：1-低危；2-中危；3-高危；4-严重 (多选英文;分隔)
        :type VulLevels: str
        :param HostType: 服务器分类：1:专业版服务器；2:自选服务器
        :type HostType: int
        :param QuuidList: 自选服务器时生效，主机quuid的string数组
        :type QuuidList: list of str
        :param VulEmergency: 是否是应急漏洞 0 否 1 是
        :type VulEmergency: int
        :param TimeoutPeriod: 超时时长 单位秒
        :type TimeoutPeriod: int
        :param VulIds: 需要扫描的漏洞id
        :type VulIds: list of int non-negative
        """
        self.VulCategories = None
        self.VulLevels = None
        self.HostType = None
        self.QuuidList = None
        self.VulEmergency = None
        self.TimeoutPeriod = None
        self.VulIds = None


    def _deserialize(self, params):
        self.VulCategories = params.get("VulCategories")
        self.VulLevels = params.get("VulLevels")
        self.HostType = params.get("HostType")
        self.QuuidList = params.get("QuuidList")
        self.VulEmergency = params.get("VulEmergency")
        self.TimeoutPeriod = params.get("TimeoutPeriod")
        self.VulIds = params.get("VulIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanVulResponse(AbstractModel):
    """ScanVul返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ScanVulSettingRequest(AbstractModel):
    """ScanVulSetting请求参数结构体

    """

    def __init__(self):
        """
        :param TimerInterval: 定期检测间隔时间（天）
        :type TimerInterval: int
        :param VulCategories: 漏洞类型：1: web应用漏洞 2:系统组件漏洞, 以数组方式传参[1,2]
        :type VulCategories: list of int non-negative
        :param VulLevels: 危害等级：1-低危；2-中危；3-高危；4-严重,以数组方式传参[1,2,3]
        :type VulLevels: list of int non-negative
        :param TimerTime: 定期检测时间，如：02:10:50
        :type TimerTime: str
        :param VulEmergency: 是否是应急漏洞 0 否 1 是
        :type VulEmergency: int
        :param StartTime: 扫描开始时间，如：00:00
        :type StartTime: str
        :param EndTime: 扫描结束时间，如：08:00
        :type EndTime: str
        :param EnableScan: 是否开启扫描 1开启 0不开启
        :type EnableScan: int
        """
        self.TimerInterval = None
        self.VulCategories = None
        self.VulLevels = None
        self.TimerTime = None
        self.VulEmergency = None
        self.StartTime = None
        self.EndTime = None
        self.EnableScan = None


    def _deserialize(self, params):
        self.TimerInterval = params.get("TimerInterval")
        self.VulCategories = params.get("VulCategories")
        self.VulLevels = params.get("VulLevels")
        self.TimerTime = params.get("TimerTime")
        self.VulEmergency = params.get("VulEmergency")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.EnableScan = params.get("EnableScan")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScanVulSettingResponse(AbstractModel):
    """ScanVulSetting返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SearchTemplate(AbstractModel):
    """快速搜索模板

    """

    def __init__(self):
        """
        :param Name: 检索名称
        :type Name: str
        :param LogType: 检索索引类型
        :type LogType: str
        :param Condition: 检索语句
        :type Condition: str
        :param TimeRange: 时间范围
        :type TimeRange: str
        :param Query: 转换的检索语句内容
        :type Query: str
        :param Flag: 检索方式。输入框检索：standard,过滤，检索：simple
        :type Flag: str
        :param DisplayData: 展示数据
        :type DisplayData: str
        :param Id: 规则ID
        :type Id: int
        """
        self.Name = None
        self.LogType = None
        self.Condition = None
        self.TimeRange = None
        self.Query = None
        self.Flag = None
        self.DisplayData = None
        self.Id = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.LogType = params.get("LogType")
        self.Condition = params.get("Condition")
        self.TimeRange = params.get("TimeRange")
        self.Query = params.get("Query")
        self.Flag = params.get("Flag")
        self.DisplayData = params.get("DisplayData")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityDynamic(AbstractModel):
    """安全事件消息数据。

    """

    def __init__(self):
        """
        :param Uuid: 云镜客户端UUID。
        :type Uuid: str
        :param EventTime: 安全事件发生时间。
        :type EventTime: str
        :param EventType: 安全事件类型。
<li>MALWARE：木马事件</li>
<li>NON_LOCAL_LOGIN：异地登录</li>
<li>BRUTEATTACK_SUCCESS：密码破解成功</li>
<li>VUL：漏洞</li>
<li>BASELINE：安全基线</li>
        :type EventType: str
        :param Message: 安全事件消息。
        :type Message: str
        :param SecurityLevel: 安全事件等级。
<li>RISK: 严重</li>
<li>HIGH: 高危</li>
<li>NORMAL: 中危</li>
<li>LOW: 低危</li>
        :type SecurityLevel: str
        """
        self.Uuid = None
        self.EventTime = None
        self.EventType = None
        self.Message = None
        self.SecurityLevel = None


    def _deserialize(self, params):
        self.Uuid = params.get("Uuid")
        self.EventTime = params.get("EventTime")
        self.EventType = params.get("EventType")
        self.Message = params.get("Message")
        self.SecurityLevel = params.get("SecurityLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityEventInfo(AbstractModel):
    """安全事件统计列表

    """

    def __init__(self):
        """
        :param EventCnt: 安全事件数
        :type EventCnt: int
        :param UuidCnt: 受影响机器数
        :type UuidCnt: int
        """
        self.EventCnt = None
        self.UuidCnt = None


    def _deserialize(self, params):
        self.EventCnt = params.get("EventCnt")
        self.UuidCnt = params.get("UuidCnt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityTrend(AbstractModel):
    """安全趋势统计数据。

    """

    def __init__(self):
        """
        :param Date: 事件时间。
        :type Date: str
        :param EventNum: 事件数量。
        :type EventNum: int
        """
        self.Date = None
        self.EventNum = None


    def _deserialize(self, params):
        self.Date = params.get("Date")
        self.EventNum = params.get("EventNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SeparateMalwaresRequest(AbstractModel):
    """SeparateMalwares请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 木马事件ID数组。(最大100条)
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SeparateMalwaresResponse(AbstractModel):
    """SeparateMalwares返回参数结构体

    """

    def __init__(self):
        """
        :param SuccessIds: 隔离成功的id数组，若无则返回空数组
        :type SuccessIds: list of int non-negative
        :param FailedIds: 隔离失败的id数组，若无则返回空数组
        :type FailedIds: list of int non-negative
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessIds = None
        self.FailedIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessIds = params.get("SuccessIds")
        self.FailedIds = params.get("FailedIds")
        self.RequestId = params.get("RequestId")


class SetBashEventsStatusRequest(AbstractModel):
    """SetBashEventsStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: ID数组，最大100条。
        :type Ids: list of int non-negative
        :param Status: 新状态(0-待处理 1-高危 2-正常)
        :type Status: int
        """
        self.Ids = None
        self.Status = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetBashEventsStatusResponse(AbstractModel):
    """SetBashEventsStatus返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SwitchBashRulesRequest(AbstractModel):
    """SwitchBashRules请求参数结构体

    """

    def __init__(self):
        """
        :param Id: 规则ID
        :type Id: int
        :param Disabled: 是否禁用
        :type Disabled: int
        """
        self.Id = None
        self.Disabled = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Disabled = params.get("Disabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchBashRulesResponse(AbstractModel):
    """SwitchBashRules返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SyncAssetScanRequest(AbstractModel):
    """SyncAssetScan请求参数结构体

    """

    def __init__(self):
        """
        :param Sync: 是否同步
        :type Sync: bool
        """
        self.Sync = None


    def _deserialize(self, params):
        self.Sync = params.get("Sync")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncAssetScanResponse(AbstractModel):
    """SyncAssetScan返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """标签信息

    """

    def __init__(self):
        """
        :param Id: 标签ID
        :type Id: int
        :param Name: 标签名
        :type Name: str
        :param Count: 服务器数
        :type Count: int
        """
        self.Id = None
        self.Name = None
        self.Count = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagMachine(AbstractModel):
    """标签相关服务器信息

    """

    def __init__(self):
        """
        :param Id: ID
        :type Id: str
        :param Quuid: 主机ID
        :type Quuid: str
        :param MachineName: 主机名称
        :type MachineName: str
        :param MachineIp: 主机内网IP
        :type MachineIp: str
        :param MachineWanIp: 主机外网IP
        :type MachineWanIp: str
        :param MachineRegion: 主机区域
        :type MachineRegion: str
        :param MachineType: 主机区域类型
        :type MachineType: str
        """
        self.Id = None
        self.Quuid = None
        self.MachineName = None
        self.MachineIp = None
        self.MachineWanIp = None
        self.MachineRegion = None
        self.MachineType = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Quuid = params.get("Quuid")
        self.MachineName = params.get("MachineName")
        self.MachineIp = params.get("MachineIp")
        self.MachineWanIp = params.get("MachineWanIp")
        self.MachineRegion = params.get("MachineRegion")
        self.MachineType = params.get("MachineType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrustMalwaresRequest(AbstractModel):
    """TrustMalwares请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 木马ID数组（单次不超过的最大条数：100）
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrustMalwaresResponse(AbstractModel):
    """TrustMalwares返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UntrustMalwaresRequest(AbstractModel):
    """UntrustMalwares请求参数结构体

    """

    def __init__(self):
        """
        :param Ids: 木马ID数组，单次最大处理不能超过200条。
        :type Ids: list of int non-negative
        """
        self.Ids = None


    def _deserialize(self, params):
        self.Ids = params.get("Ids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UntrustMalwaresResponse(AbstractModel):
    """UntrustMalwares返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateBaselineStrategyRequest(AbstractModel):
    """UpdateBaselineStrategy请求参数结构体

    """

    def __init__(self):
        """
        :param StrategyId: 策略id
        :type StrategyId: int
        :param StrategyName: 策略名称
        :type StrategyName: str
        :param ScanCycle: 检测周期
        :type ScanCycle: int
        :param ScanAt: 定期检测时间，该时间下发扫描
        :type ScanAt: str
        :param CategoryIds: 该策略下选择的基线id数组
        :type CategoryIds: list of str
        :param IsGlobal: 扫描范围是否全部服务器, 1:是  0:否, 为1则为全部专业版主机
        :type IsGlobal: int
        :param MachineType: 云主机类型：cvm：虚拟主机，bms：裸金属，ecm：边缘计算主机
        :type MachineType: str
        :param RegionCode: 主机地域
        :type RegionCode: str
        :param Quuids: 主机id数组
        :type Quuids: list of str
        """
        self.StrategyId = None
        self.StrategyName = None
        self.ScanCycle = None
        self.ScanAt = None
        self.CategoryIds = None
        self.IsGlobal = None
        self.MachineType = None
        self.RegionCode = None
        self.Quuids = None


    def _deserialize(self, params):
        self.StrategyId = params.get("StrategyId")
        self.StrategyName = params.get("StrategyName")
        self.ScanCycle = params.get("ScanCycle")
        self.ScanAt = params.get("ScanAt")
        self.CategoryIds = params.get("CategoryIds")
        self.IsGlobal = params.get("IsGlobal")
        self.MachineType = params.get("MachineType")
        self.RegionCode = params.get("RegionCode")
        self.Quuids = params.get("Quuids")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateBaselineStrategyResponse(AbstractModel):
    """UpdateBaselineStrategy返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UsualPlace(AbstractModel):
    """常用登录地

    """

    def __init__(self):
        """
        :param Id: ID。
        :type Id: int
        :param Uuid: 云镜客户端唯一标识UUID。
        :type Uuid: str
        :param CountryId: 国家 ID。
        :type CountryId: int
        :param ProvinceId: 省份 ID。
        :type ProvinceId: int
        :param CityId: 城市 ID。
        :type CityId: int
        """
        self.Id = None
        self.Uuid = None
        self.CountryId = None
        self.ProvinceId = None
        self.CityId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Uuid = params.get("Uuid")
        self.CountryId = params.get("CountryId")
        self.ProvinceId = params.get("ProvinceId")
        self.CityId = params.get("CityId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulDetailInfo(AbstractModel):
    """漏洞详细信息

    """

    def __init__(self):
        """
        :param VulId: 漏洞ID
        :type VulId: int
        :param Level: 漏洞级别
        :type Level: int
        :param Name: 漏洞名称
        :type Name: str
        :param CveId: cve编号
        :type CveId: str
        :param VulCategory: 漏洞分类
        :type VulCategory: int
        :param Descript: 漏洞描述
        :type Descript: str
        :param Fix: 修复建议
        :type Fix: str
        :param Reference: 参考链接
        :type Reference: str
        :param CvssScore: CVSS评分
        :type CvssScore: float
        :param Cvss: CVSS详情
        :type Cvss: str
        :param PublishTime: 发布时间
        :type PublishTime: str
        """
        self.VulId = None
        self.Level = None
        self.Name = None
        self.CveId = None
        self.VulCategory = None
        self.Descript = None
        self.Fix = None
        self.Reference = None
        self.CvssScore = None
        self.Cvss = None
        self.PublishTime = None


    def _deserialize(self, params):
        self.VulId = params.get("VulId")
        self.Level = params.get("Level")
        self.Name = params.get("Name")
        self.CveId = params.get("CveId")
        self.VulCategory = params.get("VulCategory")
        self.Descript = params.get("Descript")
        self.Fix = params.get("Fix")
        self.Reference = params.get("Reference")
        self.CvssScore = params.get("CvssScore")
        self.Cvss = params.get("Cvss")
        self.PublishTime = params.get("PublishTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        