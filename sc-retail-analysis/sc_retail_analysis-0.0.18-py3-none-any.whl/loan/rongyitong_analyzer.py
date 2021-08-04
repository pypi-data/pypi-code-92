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

import pandas as pd

from sc_retail_analysis.utils import ConfigUtils
from .rong_zhuan_xin_card_analyzer import RongZhuanXinAnalyzer


class RongyitongAnalyzer(RongZhuanXinAnalyzer):
    """
    融意通卡分析
    """

    def __init__(self, *, excel_writer: pd.ExcelWriter):
        super().__init__(excel_writer=excel_writer)
        self._key_enabled = "retail.loan.rongyitong.enabled"
        self._key_business_type = "retail.loan.rongyitong.business_type"
        self._key_export_column_list = "retail.loan.rongyitong.sheet_config.export_column_list"

    def _read_config(self):
        config = ConfigUtils.get_config()
        # 融卡发卡及相关数据明细表文件路径
        self._src_filepath = config.get("retail.loan.rongyitong.source_file_path")
        # Sheet名称
        self._sheet_name = config.get("retail.loan.rongyitong.sheet_name")
        # 表头行索引
        self._header_row = config.get("retail.loan.rongyitong.sheet_config.header_row")
        # 客户经理列索引
        self._name_column = config.get("retail.loan.rongyitong.sheet_config.name_column")
        # 垫款额列索引
        self._advance_amount_column = config.get("retail.loan.rongyitong.sheet_config.advance_amount_column")
        # 生成的Excel中融意通卡垫款额的列名
        self._target_advance_amount_column_name = config.get(
            "retail.loan.rongyitong.sheet_config.target_advance_amount_column_name")
