# The MIT License (MIT)
#
# Copyright (c) 2021 Scott Lau
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import logging
import os

from scutils import log_init

log_init()

import pandas as pd

from .utils import ConfigUtils, ManifestUtils, BranchUtils
# from .non_interest_income.fund_analyzer import FundAnalyzer
from .non_interest_income.financing_analyzer import FinancingAnalyzer
from .non_interest_income.precious_metal_analyzer import PreciousMetalAnalyzer
from .non_interest_income.deposit_analyzer import DepositAnalyzer
from .non_interest_income.wealthy_client_analyzer import WealthyClientAnalyzer
from .non_interest_income.fund_purchase_analyzer import FundPurchaseAnalyzer
from .non_interest_income.delegate_insurance_analyzer import DelegateInsuranceAnalyzer
from .loan.rongyitong_analyzer import RongyitongAnalyzer
from .loan.xinyitong_analyzer import XinyitongAnalyzer
from .loan.transfer_payment_card_analyzer import TransferPaymentCardAnalyzer
from .loan.easy_loan_analyzer import EasyLoanAnalyzer
from .loan.large_installments_analyzer import LargeInstallmentsAnalyzer
from .loan.loan_detail_analyzer import LoanDetailAnalyzer
from .hn.hn_client_analyzer import HuNanClientAnalyzer
from .summary.branch_summary_analyzer import BranchSummaryAnalyzer
from .summary.manager_summary_analyzer import ManagerSummaryAnalyzer
from .credit_card.credit_card_amount_analyzer import CreditCardAmountAnalyzer
from .credit_card.credit_card_issue_count_analyzer import CreditCardIssueCountAnalyzer
from .credit_card.credit_card_income_analyzer import CreditCardIncomeAnalyzer


class Runner:

    def __init__(self):
        ConfigUtils.clear()
        config = ConfigUtils.get_config()
        # 生成的目标Excel文件存放路径
        self._target_directory = config.get("retail.target_directory")
        # 目标文件名称
        self._target_filename = config.get("retail.target_filename")
        # 生成的Excel中按客户经理汇总的Sheet的名称
        self._target_manager_summary_sheet_name = config.get("retail.target_manager_summary_sheet_name")
        # 生成的Excel中按客户经理汇总的Sheet的名称
        self._target_branch_summary_sheet_name = config.get("retail.target_branch_summary_sheet_name")

    def _load_branch_stuff(self):
        try:
            # 加载机构名称对应表
            BranchUtils.load_branch_name_mapping()
            # 加载公共户关键字列表
            BranchUtils.load_common_account_keyword_list()
            # 加载业绩归属机构配置
            BranchUtils.load_sales_performance_attribution_mapping()
            # 加载所有发生业务的机构清单
            BranchUtils.load_all_business_branch_list()
            return 0
        except Exception as error:
            logging.getLogger(__name__).error("加载机构名称对应表失败：{}".format(error))
            return 1

    def _load_manifest_stuff(self):
        try:
            # 加载花名册
            ManifestUtils.load_manifest()
            # 加载离职人员调整表
            ManifestUtils.load_leave_employee_mapping()
            # 加载（非息）离职人员归属机构表
            ManifestUtils.load_non_interest_leave_employee_branch_mapping()
            return 0
        except Exception as error:
            logging.getLogger(__name__).error("加载花名册相关信息失败：{}".format(error))
            return 1

    def run(self):
        logging.getLogger(__name__).info("开始进行零售考核数据分析...")

        # 加载机构相关配置
        result = self._load_branch_stuff()
        if result != 0:
            return result

        # 加载花名册相关配置
        result = self._load_manifest_stuff()
        if result != 0:
            return result

        target_filename_full_path = os.path.join(self._target_directory, self._target_filename)
        logging.getLogger(__name__).info("输出文件：{} ".format(target_filename_full_path))
        with pd.ExcelWriter(target_filename_full_path) as excel_writer:
            # 分析客户经理汇总
            manager_summary_analyzer_list, manager_summary_result, target_column_list = \
                self._manager_summary_analysis(excel_writer)
            # 分析机构汇总
            branch_summary_analyzer_list = self._branch_summary_analysis(
                excel_writer,
                manager_summary_result,
                target_column_list
            )
            # 输出原Excel数据
            self._write_original_excel_data(branch_summary_analyzer_list, manager_summary_analyzer_list)
        logging.getLogger(__name__).info("结束零售考核数据分析...")
        return 0

    def _manager_summary_analysis(self, excel_writer):
        manager_summary_analyzer_list = [
            # # 基金
            # FundAnalyzer(excel_writer=excel_writer),
            # 基金业认申购明细
            FundPurchaseAnalyzer(excel_writer=excel_writer),
            # 理财
            FinancingAnalyzer(excel_writer=excel_writer),
            # 贵金属
            PreciousMetalAnalyzer(excel_writer=excel_writer),
            # 存款
            DepositAnalyzer(excel_writer=excel_writer),
            # 代理保险
            DelegateInsuranceAnalyzer(excel_writer=excel_writer),
            # 融意通卡
            RongyitongAnalyzer(excel_writer=excel_writer),
            # 转账支付卡
            TransferPaymentCardAnalyzer(excel_writer=excel_writer),
            # 心意通卡
            XinyitongAnalyzer(excel_writer=excel_writer),
            # 易得贷
            EasyLoanAnalyzer(excel_writer=excel_writer),
            # 信用卡大额分期
            LargeInstallmentsAnalyzer(excel_writer=excel_writer),
            # 贷款明细
            LoanDetailAnalyzer(excel_writer=excel_writer),
            # 信用卡投放额
            CreditCardAmountAnalyzer(excel_writer=excel_writer),
            # 信用卡发卡量
            CreditCardIssueCountAnalyzer(excel_writer=excel_writer),
            # 信用卡收入
            CreditCardIncomeAnalyzer(excel_writer=excel_writer),
        ]
        # 按客户经理汇总结果
        manager_summary_result = ManifestUtils.get_manifest_df().copy()
        # 输出列清单列表
        target_column_list = list()
        logging.getLogger(__name__).info("按客户经理分析...")
        for analyzer in manager_summary_analyzer_list:
            try:
                manager_summary_result = analyzer.analysis(manifest_data=manager_summary_result)
                target_column_list.extend(analyzer.get_target_columns())
            except Exception as e:
                logging.getLogger(__name__).exception("分析 {} 时出错".format(analyzer.get_business_type()), exc_info=e)
        # 客户经理汇总分析，待上述分析完成后，这里做一个总计分析
        analyzer = ManagerSummaryAnalyzer(
            excel_writer=excel_writer,
            target_column_list=target_column_list,
        )
        try:
            manager_summary_result = analyzer.analysis(manifest_data=manager_summary_result)
        except Exception as e:
            logging.getLogger(__name__).exception("分析 {} 时出错".format(analyzer.get_business_type()), exc_info=e)
        # 没有业绩的显示0
        manager_summary_result.fillna(0, inplace=True)
        manager_summary_result.to_excel(excel_writer=excel_writer, index=False,
                                        sheet_name=self._target_manager_summary_sheet_name)
        return manager_summary_analyzer_list, manager_summary_result, target_column_list

    def _branch_summary_analysis(self, excel_writer, manager_summary_result, target_column_list):
        branch_summary_analyzer_list = [
            # 机构汇总
            BranchSummaryAnalyzer(
                manager_summary=manager_summary_result,
                target_column_list=target_column_list,
                excel_writer=excel_writer,
            ),
            # 湘籍企业
            HuNanClientAnalyzer(excel_writer=excel_writer),
            # 财富客户
            WealthyClientAnalyzer(excel_writer=excel_writer),
        ]
        # 唯一的机构清单
        branch_summary_result = pd.DataFrame(
            data=set(BranchUtils.get_branch_name_mapping().values()),
            columns=[ManifestUtils.get_branch_column_name()],
            dtype=str
        )
        logging.getLogger(__name__).info("按机构汇总分析...")
        # 按机构汇总结果
        for analyzer in branch_summary_analyzer_list:
            try:
                branch_summary_result = analyzer.analysis(manifest_data=branch_summary_result)
            except Exception as e:
                logging.getLogger(__name__).exception("分析 {} 时出错".format(analyzer.get_business_type()), exc_info=e)
        # 没有业绩的显示0
        branch_summary_result.fillna(0, inplace=True)
        # 添加机构合计行
        branch_summary_result.set_index(ManifestUtils.get_branch_column_name(), inplace=True)
        branch_summary_result.loc["合计"] = branch_summary_result.apply(lambda x: x.sum())
        branch_summary_result.reset_index(inplace=True)
        # 输出到Excel
        branch_summary_result.to_excel(excel_writer=excel_writer, index=False,
                                       sheet_name=self._target_branch_summary_sheet_name)
        return branch_summary_analyzer_list

    def _write_original_excel_data(self, branch_summary_analyzer_list, manager_summary_analyzer_list):
        logging.getLogger(__name__).info("输出源数据到Excel...")
        # 输出源数据到Excel
        for analyzer in manager_summary_analyzer_list + branch_summary_analyzer_list:
            try:
                analyzer.write_origin_data()
            except Exception as e:
                logging.getLogger(__name__).exception("输出 {} 源数据到Excel时出错".format(analyzer.get_business_type()),
                                                      exc_info=e)


def main():
    try:
        state = Runner().run()
    except Exception as e:
        logging.getLogger(__name__).exception('An error occurred.', exc_info=e)
        return 1
    else:
        return state


if __name__ == '__main__':
    main()
