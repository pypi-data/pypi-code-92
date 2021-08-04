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

import pandas as pd
from pandas import ExcelWriter

from sc_retail_analysis.utils import ConfigUtils, ManifestUtils


class BaseAnalyzer:
    """
    分析基础类
    """

    def __init__(self, *, excel_writer: ExcelWriter):
        # 业务类型
        self._key_business_type = None
        self._business_type = None
        self._excel_writer = excel_writer
        self._key_enabled = None
        # 输出列名清单
        self._target_column_list = list()
        self._read_config()
        self._origin_data: pd.DataFrame = None
        self._key_export_column_list = None
        # 源数据输出列索引清单
        self._export_column_index_list = list()
        self._export_column_list = list()
        # 源数据是否输出所有列
        self._export_all_columns = False

    def _add_export_column_index(self, index):
        column_size = self._origin_data.columns.size
        if index >= column_size or index < 0:
            logging.getLogger(__name__).error(
                "{} 配置不合理：列索引 {} 超出范围".format(self._key_export_column_list, index))
        if index not in self._export_column_index_list:
            self._export_column_index_list.append(index)

    def _add_export_column_manifest_branch(self, origin_data: pd.DataFrame):
        """
        原始输出报表添加花名册所在机构列
        :return:
        """
        return origin_data

    def _read_export_column_list(self):
        """
        从配置文件中读取源数据输出列索引清单
        :return:
        """
        if self._key_export_column_list is None:
            return
        column_list_config = ConfigUtils.get_config().get(self._key_export_column_list)
        if column_list_config is None or type(column_list_config) != list:
            return
        for column_config in column_list_config:
            if type(column_config) == int:
                self._add_export_column_index(column_config)
            elif type(column_config) == str:
                if column_config.lower() == 'all':
                    self._export_all_columns = True
                    break
                elif '-' in column_config:
                    columns = column_config.split('-')
                    if len(columns) == 2:
                        start, end = columns
                        try:
                            start = int(start)
                        except ValueError:
                            logging.getLogger(__name__).error(
                                "{} 配置不合理：{}".format(self._key_export_column_list, column_config))
                            continue
                        try:
                            end = int(end)
                        except ValueError:
                            logging.getLogger(__name__).error(
                                "{} 配置不合理：{}".format(self._key_export_column_list, column_config))
                            continue
                        if start > end:
                            logging.getLogger(__name__).error(
                                "{} 配置不合理：{}".format(self._key_export_column_list, column_config))
                            continue
                        else:
                            value = start
                            while value <= end:
                                self._add_export_column_index(value)
                                value += 1
                    else:
                        logging.getLogger(__name__).error(
                            "{} 配置不合理：{}".format(self._key_export_column_list, column_config))
                        continue
                else:
                    try:
                        value = int(column_config)
                        self._add_export_column_index(value)
                    except ValueError:
                        logging.getLogger(__name__).error(
                            "{} 配置不合理：{}".format(self._key_export_column_list, column_config))
                        continue
            else:
                logging.getLogger(__name__).error("{} 配置不合理：{}".format(self._key_export_column_list, column_config))
        for column in self._export_column_index_list:
            self._export_column_list.append(self._origin_data.columns[column])

    def get_target_columns(self) -> list:
        """
        获取输出列名清单
        :return:
        """
        return self._target_column_list

    def _add_target_column(self, column: str) -> None:
        """
        添加输出列名
        :return:
        """
        # 如果已经存在了，则不添加
        if column in self._target_column_list:
            return
        self._target_column_list.append(column)

    def _enabled(self):
        """
        是否启用分析
        :return: 是否启用分析
        """
        # 配置不存在默认不启用分析
        enabled_config = ConfigUtils.get_config().get(self._key_enabled)
        return False if enabled_config is None else enabled_config

    def get_business_type(self) -> str:
        """
        业务类型
        :return: 业务类型
        """
        return self._business_type

    def _read_config(self):
        """
        读取配置，初始化相关变量
        """
        pass

    def _read_src_file(self) -> pd.DataFrame:
        """
        读取Excel或CSV文件，获取DataFrame
        :return: DataFrame
        """
        return pd.DataFrame()

    def _rename_target_columns(self, *, data: pd.DataFrame) -> pd.DataFrame:
        """
        重命名DataFrame相关列

        :param data: 原DataFrame
        :return: 重命名相关列后的DataFrame
        """
        return data

    def _add_target_columns(self) -> None:
        """
        添加输出列清单

        :return: None
        """
        pass

    def _pre_pivot_table(self, *, data: pd.DataFrame) -> pd.DataFrame:
        """
        在数据透视之前做的操作

        :param data: 原DataFrame
        :return: 操作后的DataFrame
        """
        return data

    def _pivot_table(self, *, data: pd.DataFrame) -> pd.DataFrame:
        """
        对DataFrame进行数据透视

        :param data: 原DataFrame
        :return: 数据透视后的DataFrame
        """
        return data

    def _after_pivot_table(self, *, data: pd.DataFrame) -> pd.DataFrame:
        """
        在数据透视之后做的操作

        :param data: 原DataFrame
        :return: 操作后的DataFrame
        """
        return data

    def _merge_with_manifest(self, *, manifest_data: pd.DataFrame, data: pd.DataFrame) -> pd.DataFrame:
        """
        与花名册合并

        :param manifest_data: 花名册数据，左边表
        :param data: 待合并DataFrame，右边表
        :return: 与花名册合并后的DataFrame
        """
        return data

    def _drop_duplicated_columns(self, *, data: pd.DataFrame) -> pd.DataFrame:
        """
        删除重复列

        :return: 删除重复列后的DataFrame
        """
        return data

    def analysis(self, *, manifest_data: pd.DataFrame) -> pd.DataFrame:
        """
        主分析流程分析

        :param manifest_data: 花名册数据
        :return: 与花名册合并后的分析结果
        """
        self._business_type = ConfigUtils.get_config().get(self._key_business_type)
        # 如果未启用，则直接返回花名册数据
        if not self._enabled():
            logging.getLogger(__name__).info("{} 分析未启用".format(self._business_type))
            return manifest_data
        # 读取业务类型
        logging.getLogger(__name__).info("开始分析 {} 数据".format(self._business_type))
        # 读取Excel或CSV文件，获取DataFrame
        try:
            data = self._read_src_file()
            self._origin_data = data.copy()
            self._export_column_list.clear()
            self._origin_data = self._add_export_column_manifest_branch(self._origin_data)
            self._read_export_column_list()
        except FileNotFoundError as e:
            logging.getLogger(__name__).error("{} 分析失败：{}".format(self._business_type, e))
            return manifest_data
        # 重命名DataFrame相关列
        data = self._rename_target_columns(data=data)
        # 在数据透视之前做的操作
        data = self._pre_pivot_table(data=data)
        # 对DataFrame进行数据透视
        data = self._pivot_table(data=data)
        # 在数据透视之后做的操作
        if not data.empty:
            data = self._after_pivot_table(data=data)
        # 与花名册合并
        data = self._merge_with_manifest(manifest_data=manifest_data, data=data)
        # 删除重复列
        data = self._drop_duplicated_columns(data=data)
        # 添加输出列清单
        self._add_target_columns()
        logging.getLogger(__name__).info("完成分析 {} 数据".format(self._business_type))
        return data

    def write_origin_data(self):
        """
        输出筛选列后原数据到Excel
        :return:
        """
        # 如果未启用，则直接返回花名册数据
        if not self._enabled():
            return
        # 读取源文件失败
        if self._origin_data is None:
            return

        # 调整列顺序，将花名册所在机构调整到第一列
        if ManifestUtils.get_manifest_branch_column_name() in self._origin_data.columns:
            if ManifestUtils.get_manifest_branch_column_name() not in self._export_column_list:
                self._export_column_list.insert(0, ManifestUtils.get_manifest_branch_column_name())
            branch_column = self._origin_data[ManifestUtils.get_manifest_branch_column_name()]
            self._origin_data = self._origin_data.drop(ManifestUtils.get_manifest_branch_column_name(), axis=1)
            self._origin_data.insert(0, ManifestUtils.get_manifest_branch_column_name(), branch_column)

        if self._export_all_columns:
            self._origin_data.to_excel(
                excel_writer=self._excel_writer,
                index=False,
                sheet_name=self._business_type,
            )
        else:
            self._origin_data.to_excel(
                excel_writer=self._excel_writer,
                index=False,
                sheet_name=self._business_type,
                columns=self._export_column_list,
            )
