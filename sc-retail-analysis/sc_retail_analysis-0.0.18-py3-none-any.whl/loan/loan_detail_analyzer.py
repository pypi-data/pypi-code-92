#  The MIT License (MIT)
#
#  Copyright (c) 2021. Scott Lau
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import logging

import numpy as np
import pandas as pd

from sc_retail_analysis.base_analyzer import BaseAnalyzer
from sc_retail_analysis.utils import ConfigUtils, ManifestUtils


class LoanDetailAnalyzer(BaseAnalyzer):
    """
    贷款明细分析
    """

    def __init__(self, *, excel_writer: pd.ExcelWriter):
        self._business_type_mapping_loaded = False
        self._business_type_mapping = dict()
        super().__init__(excel_writer=excel_writer)
        self._key_enabled = "retail.loan.loan_detail.enabled"
        self._key_business_type = "retail.loan.loan_detail.business_type"
        self._key_export_column_list = "retail.loan.loan_detail.sheet_config.export_column_list"

    def get_business_type_mapping(self) -> dict:
        """
        业务种类与业务大类对应关系
        :return: 业务种类与业务大类对应关系
        """
        return self._business_type_mapping

    def _load_business_type_mapping(self):
        """
        加载业务种类与业务大类对应关系
        :return:
        """
        if self._business_type_mapping_loaded:
            return
        mapping = ConfigUtils.get_config().get("retail.loan.loan_detail.business_type_mapping")
        self._business_type_mapping.update(mapping)
        self._business_type_mapping_loaded = True

    def _read_config(self):
        self._load_business_type_mapping()
        config = ConfigUtils.get_config()
        # 贷款明细报表文件路径
        self._src_filepath = config.get("retail.loan.loan_detail.source_file_path")
        # Sheet名称
        self._sheet_name = config.get("retail.loan.loan_detail.sheet_name")
        # 表头行索引
        self._header_row = config.get("retail.loan.loan_detail.sheet_config.header_row")
        # 客户经理列索引
        self._name_column = config.get("retail.loan.loan_detail.sheet_config.name_column")
        # 余额列索引
        self._balance_column = config.get("retail.loan.loan_detail.sheet_config.balance_column")
        # 业务种类列索引
        self._business_type_column = config.get(
            "retail.loan.loan_detail.sheet_config.business_type_column")
        self._business_genre_column_name = "业务大类"

    def _read_src_file(self) -> pd.DataFrame:
        logging.getLogger(__name__).info("读取源文件：{}".format(self._src_filepath))
        data = pd.read_excel(self._src_filepath, sheet_name=self._sheet_name, header=self._header_row)
        self._name_column_name = data.columns[self._name_column]
        self._balance_column_name = data.columns[self._balance_column]
        self._business_type_column_name = data.columns[self._business_type_column]

        # 业务种类与业务大类对应关系
        mapping = self.get_business_type_mapping()
        # 筛选需要统计的业务大类
        criterion = data[self._business_type_column_name].map(lambda x: x in mapping.keys())
        result = data[criterion].copy()
        # 筛选余额不为0的记录
        criterion = result[self._balance_column_name].map(lambda x: x != 0)
        result = result[criterion].copy()
        return result

    def _add_export_column_manifest_branch(self, origin_data: pd.DataFrame):
        if origin_data is None or origin_data.empty:
            return origin_data
        # 与花名册整合，添加花名册所在部门一列
        data = origin_data.merge(
            ManifestUtils.get_name_branch_data_frame(),
            how="left",
            left_on=[self._name_column_name],
            right_on=[ManifestUtils.get_name_column_name()]
        )
        return data

    def _mapping_leave_employee(self, *, data: pd.DataFrame) -> pd.DataFrame:
        """
        映射离职员工到对应的客户经理

        :param data: 原DataFrame
        :return: 操作后的DataFrame
        """
        mapping = ManifestUtils.get_leave_employee_mapping()
        result = data.replace({self._name_column_name: mapping})
        return result

    def _pre_pivot_table(self, *, data: pd.DataFrame) -> pd.DataFrame:
        # 增加业务大类一列
        data[self._business_genre_column_name] = data[self._business_type_column_name]
        # 业务种类与业务大类对应关系
        mapping = self.get_business_type_mapping()
        # 处理业务种类与业务大类对应关系
        data = data.replace({self._business_genre_column_name: mapping})
        # 筛选需要统计的业务大类
        criterion = data[self._business_genre_column_name].map(lambda x: x in mapping.values())
        result = data[criterion].copy()

        return self._mapping_leave_employee(data=result)

    def _pivot_table(self, *, data: pd.DataFrame) -> pd.DataFrame:
        table = pd.pivot_table(data, values=[self._balance_column_name],
                               index=[self._name_column_name],
                               columns=[self._business_genre_column_name],
                               aggfunc=np.sum, fill_value=0)
        return table

    def _after_pivot_table(self, *, data: pd.DataFrame) -> pd.DataFrame:
        data.columns = data.columns.droplevel(0)
        return data.reset_index()

    def _merge_with_manifest(self, *, manifest_data: pd.DataFrame, data: pd.DataFrame) -> pd.DataFrame:
        logging.getLogger(__name__).info("与花名册合并...")
        merge_result = ManifestUtils.merge_with_manifest(manifest_data=manifest_data, data=data,
                                                         name_column_name=self._name_column_name)
        return merge_result

    def _drop_duplicated_columns(self, *, data: pd.DataFrame) -> pd.DataFrame:
        return data.drop(columns=[self._name_column_name])

    def _add_target_columns(self) -> None:
        # 业务种类与业务大类对应关系
        mapping = self.get_business_type_mapping()
        # 筛选需要统计的业务大类
        for column in mapping.values():
            self._add_target_column(column)
