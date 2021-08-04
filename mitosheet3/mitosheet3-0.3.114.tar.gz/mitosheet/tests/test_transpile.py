#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Mito.
# Distributed under the terms of the Modified BSD License.

import pytest
import pandas as pd

from mitosheet.transpiler.transpile import transpile
from mitosheet.tests.test_utils import create_mito_wrapper, create_mito_wrapper_dfs


def test_transpile_single_column():
    mito = create_mito_wrapper(['abc'])
    mito.set_formula('=A', 0, 'B', add_column=True)

    assert mito.transpiled_code == [
        "df1.insert(1, 'B', 0)", 
        'df1[\'B\'] = df1[\'A\']'
    ]


def test_transpile_multiple_columns_no_relationship():
    mito = create_mito_wrapper(['abc'])
    mito.add_column(0, 'B')
    mito.add_column(0, 'C')
    code_container = transpile(mito.mito_widget.steps_manager)
    
    assert len([line for line in code_container['code'] if 'df1.insert(1, \'B\', 0)' in line]) > 0
    assert len([line for line in code_container['code'] if 'df1.insert(2, \'C\', 0)' in line]) > 0

def test_transpile_columns_in_each_sheet():
    mito = create_mito_wrapper(['abc'], sheet_two_A_data=['abc'])
    mito.add_column(0, 'B')
    mito.add_column(1, 'B')
    code_container = transpile(mito.mito_widget.steps_manager)
    assert len([line for line in code_container['code'] if 'df1.insert(1, \'B\', 0)' in line]) > 0
    assert len([line for line in code_container['code'] if 'df2.insert(1, \'B\', 0)' in line]) > 0

def test_transpile_multiple_columns_linear():
    mito = create_mito_wrapper(['abc'])
    mito.set_formula('=A', 0, 'B', add_column=True)
    mito.set_formula('=B', 0, 'C', add_column=True)

    assert mito.transpiled_code == [
        'df1.insert(1, \'B\', 0)',
        'df1[\'B\'] = df1[\'A\']', 
        'df1.insert(2, \'C\', 0)',
        'df1[\'C\'] = df1[\'B\']'
    ]

COLUMN_HEADERS = [
    ('ABC'),
    ('ABC_D'),
    ('ABC_DEF'),
    ('ABC_123'),
    ('ABC_HAHA_123'),
    ('ABC_HAHA-123'),
    ('---data---'),
    ('---da____ta---'),
    ('--'),
]
@pytest.mark.parametrize("column_header", COLUMN_HEADERS)
def test_transpile_column_headers_non_alphabet(column_header):
    mito = create_mito_wrapper(['abc'])
    mito.set_formula('=A', 0, column_header, add_column=True)

    assert mito.transpiled_code == [
        f'df1.insert(1, \'{column_header}\', 0)', 
        f'df1[\'{column_header}\'] = df1[\'A\']'
    ]


COLUMN_HEADERS = [
    ('ABC'),
    ('ABC_D'),
    ('ABC_DEF'),
    ('ABC_123'),
    ('ABC_HAHA_123'),
    ('ABC_HAHA-123'),
    ('---data---'),
    ('---da____ta---'),
    ('--'),
]
@pytest.mark.parametrize("column_header", COLUMN_HEADERS)
def test_transpile_column_headers_non_alphabet_multi_sheet(column_header):
    mito = create_mito_wrapper(['abc'], sheet_two_A_data=['abc'])
    mito.set_formula('=A', 0, column_header, add_column=True)
    mito.set_formula('=A', 1, column_header, add_column=True)

    assert mito.transpiled_code == [
        f'df1.insert(1, \'{column_header}\', 0)', 
        f'df1[\'{column_header}\'] = df1[\'A\']', 
        f'df2.insert(1, \'{column_header}\', 0)', 
        f'df2[\'{column_header}\'] = df2[\'A\']'
    ]

def test_preserves_order_columns():
    mito = create_mito_wrapper(['abc'])
    # Topological sort will currently display this in C, B order
    mito.add_column(0, 'B')
    mito.add_column(0, 'C')

    assert mito.transpiled_code == [
        'df1.insert(1, \'B\', 0)',
        'df1.insert(2, \'C\', 0)',
    ]

def test_transpile_merge_all_columns():
    df_one = pd.DataFrame(data={'A': [1], 'B': [101], 'C': [11]})
    df_two = pd.DataFrame(data={'A': [1], 'D': [100], 'E': [10]})
    mito = create_mito_wrapper_dfs(df_one, df_two)

    mito.merge_sheets(0, 'A', list(df_one.keys()), 1, 'A', list(df_two.keys()))

    assert mito.transpiled_code == [
        'temp_df = df2.drop_duplicates(subset=\'A\')', 
        'df3 = df1.merge(temp_df, left_on=[\'A\'], right_on=[\'A\'], how=\'left\', suffixes=[\'_df1\', \'_df2\'])'
    ]

def test_transpile_merge_some_all_columns():
    df_one = pd.DataFrame(data={'A': [1], 'B': [101], 'C': [11]})
    df_two = pd.DataFrame(data={'A': [1], 'D': [100], 'E': [10]})
    mito = create_mito_wrapper_dfs(df_one, df_two)

    mito.merge_sheets(0, 'A', ['A', 'B'], 1, 'A', ['A', 'D'])

    assert mito.transpiled_code == [
        "temp_df = df2.drop_duplicates(subset='A')", 
        "df1_tmp = df1.drop(['C'], axis=1)", 
        "df2_tmp = temp_df.drop(['E'], axis=1)", 
        "df3 = df1_tmp.merge(df2_tmp, left_on=['A'], right_on=['A'], how='left', suffixes=['_df1', '_df2'])"
    ]

def test_transpile_merge_all_columns_than_some_columns():
    df_one = pd.DataFrame(data={'A': [1], 'B': [101], 'C': [11]})
    df_two = pd.DataFrame(data={'A': [1], 'D': [100], 'E': [10]})
    mito = create_mito_wrapper_dfs(df_one, df_two)

    mito.merge_sheets(0, 'A', list(df_one.keys()), 1, 'A', list(df_two.keys()))    
    mito.merge_sheets(0, 'A', ['A', 'B'], 1, 'A', ['A', 'D'])

    assert mito.transpiled_code == [
        'temp_df = df2.drop_duplicates(subset=\'A\')', 
        'df3 = df1.merge(temp_df, left_on=[\'A\'], right_on=[\'A\'], how=\'left\', suffixes=[\'_df1\', \'_df2\'])',
        "temp_df = df2.drop_duplicates(subset='A')", 
        "df1_tmp = df1.drop(['C'], axis=1)", 
        "df2_tmp = temp_df.drop(['E'], axis=1)", 
        "df4 = df1_tmp.merge(df2_tmp, left_on=['A'], right_on=['A'], how='left', suffixes=['_df1', '_df2'])"
    ]

def test_transpile_delete_column():
    df1 = pd.DataFrame(data={'A': [1], 'B': [101], 'C': [11]})
    mito = create_mito_wrapper_dfs(df1)
    mito.delete_column(0, 'C')

    assert mito.transpiled_code == [
        'df1.drop(\'C\', axis=1, inplace=True)'
    ]


# TESTING OPTIMIZATION

def test_removes_unedited_formulas_for_unedited_sheets():
    df1 = pd.DataFrame(data={'A': [1], 'B': [101], 'C': [11]})
    df2 = pd.DataFrame(data={'A': [1], 'B': [101], 'C': [11]})
    mito = create_mito_wrapper_dfs(df1, df2)

    mito.set_formula('=C', 0, 'D', add_column=True)
    mito.set_formula('=C', 1, 'D', add_column=True)

    mito.merge_sheets(0, 'A', ['A', 'B', 'C', 'D'], 1, 'A', ['A', 'B', 'C', 'D'])

    mito.set_formula('=C + 1', 1, 'D', add_column=True)

    assert mito.transpiled_code == [
        "df1.insert(3, 'D', 0)", 
        'df1[\'D\'] = df1[\'C\']',
        "df2.insert(3, 'D', 0)", 
        'df2[\'D\'] = df2[\'C\']',
        'temp_df = df2.drop_duplicates(subset=\'A\')', 
        'df3 = df1.merge(temp_df, left_on=[\'A\'], right_on=[\'A\'], how=\'left\', suffixes=[\'_df1\', \'_df2\'])',
        'df2[\'D\'] = df2[\'C\'] + 1',
    ]


def test_mulitple_merges_no_formula_steps():
    df1 = pd.DataFrame(data={'A': [1], 'B': [101], 'C': [11]})
    df2 = pd.DataFrame(data={'A': [1], 'B': [101], 'C': [11]})
    mito = create_mito_wrapper_dfs(df1, df2)
    mito.merge_sheets(0, 'A', ['A', 'B', 'C'], 1, 'A', ['A', 'B', 'C'])
    mito.merge_sheets(0, 'A', ['A', 'B', 'C'], 1, 'A', ['A', 'B', 'C'])
    mito.merge_sheets(0, 'A', ['A', 'B', 'C'], 1, 'A', ['A', 'B', 'C'])


    assert mito.transpiled_code == [
        'temp_df = df2.drop_duplicates(subset=\'A\')', 
        'df3 = df1.merge(temp_df, left_on=[\'A\'], right_on=[\'A\'], how=\'left\', suffixes=[\'_df1\', \'_df2\'])',
        'temp_df = df2.drop_duplicates(subset=\'A\')', 
        'df4 = df1.merge(temp_df, left_on=[\'A\'], right_on=[\'A\'], how=\'left\', suffixes=[\'_df1\', \'_df2\'])',
        'temp_df = df2.drop_duplicates(subset=\'A\')', 
        'df5 = df1.merge(temp_df, left_on=[\'A\'], right_on=[\'A\'], how=\'left\', suffixes=[\'_df1\', \'_df2\'])'
    ]

def test_optimization_with_other_edits():
    df1 = pd.DataFrame(data={'A': [1], 'B': [101], 'C': [11]})
    df2 = pd.DataFrame(data={'A': [1], 'B': [101], 'C': [11]})
    mito = create_mito_wrapper_dfs(df1, df2)
    mito.add_column(0, 'D')
    mito.set_formula('=A', 0, 'D')
    mito.merge_sheets(0, 'A', ['A', 'B', 'C', 'D'], 1, 'A', ['A', 'B', 'C'])
    mito.add_column(0, 'AAA')
    mito.delete_column(0, 'AAA')

    assert mito.transpiled_code == [
        "df1.insert(3, 'D', 0)", 
        'df1[\'D\'] = df1[\'A\']',
        'temp_df = df2.drop_duplicates(subset=\'A\')', 
        'df3 = df1.merge(temp_df, left_on=[\'A\'], right_on=[\'A\'], how=\'left\', suffixes=[\'_df1\', \'_df2\'])',
        'df1.insert(4, \'AAA\', 0)',
        'df1.drop(\'AAA\', axis=1, inplace=True)'
    ]

TAB = '    '
NEWLINE_TAB = f'\n{TAB}'
flatten_code = f'pivot_table.columns = [{NEWLINE_TAB}\'_\'.join([str(c) for c in col]).strip() if isinstance(col, tuple) else col{NEWLINE_TAB}for col in pivot_table.columns.values\n]'


def test_transpile_initial_rename_mulitple_columns():
    df1 = pd.DataFrame(data={'First Name': ['Nate', 'Nate'], 'Last Name': ['Rush', 'Jack']})
    mito = create_mito_wrapper_dfs(df1)

    assert mito.transpiled_code == [
        '# Rename headers to make them work with Mito',
        'df1.rename(columns={\"First Name\": \"First_Name\", \"Last Name\": \"Last_Name\"}, inplace=True)',
    ]

def test_transpile_initial_rename_multiple_dfs():
    df1 = pd.DataFrame(data={'First Name': ['Nate', 'Nate'], 'Last_Name': ['Rush', 'Jack']})
    df2 = pd.DataFrame(data={'First_Name': ['Nate', 'Nate'], 'Last Name': ['Rush', 'Jack']})
    mito = create_mito_wrapper_dfs(df1, df2)

    assert mito.transpiled_code == [
        '# Rename headers to make them work with Mito',
        'df1.rename(columns={\"First Name\": \"First_Name\"}, inplace=True)',
        'df2.rename(columns={\"Last Name\": \"Last_Name\"}, inplace=True)',
    ]
    
def test_transpile_reorder_column():
    df1 = pd.DataFrame(data={'A': ['aaron'], 'B': ['jon']})
    mito = create_mito_wrapper_dfs(df1)
    mito.reorder_column(0, 'A', 1)

    assert mito.transpiled_code == [
        'df1_columns = [col for col in df1.columns if col != \'A\']',
        'df1_columns.insert(1, \'A\')',
        'df1 = df1[df1_columns]'
    ]

def test_transpile_two_column_reorders():
    df1 = pd.DataFrame(data={'A': ['aaron'], 'B': ['jon']})
    mito = create_mito_wrapper_dfs(df1)
    mito.reorder_column(0, 'A', 1)
    mito.reorder_column(0, 'B', 1)

    assert mito.transpiled_code == [
        'df1_columns = [col for col in df1.columns if col != \'A\']',
        'df1_columns.insert(1, \'A\')',
        'df1 = df1[df1_columns]',
        'df1_columns = [col for col in df1.columns if col != \'B\']',
        'df1_columns.insert(1, \'B\')',
        'df1 = df1[df1_columns]'
    ]

def test_transpile_reorder_column_invalid():
    df1 = pd.DataFrame(data={'A': ['aaron'], 'B': ['jon']})
    mito = create_mito_wrapper_dfs(df1)
    mito.reorder_column(0, 'A', 5)

    assert mito.transpiled_code == [
        'df1_columns = [col for col in df1.columns if col != \'A\']',
        'df1_columns.insert(1, \'A\')',
        'df1 = df1[df1_columns]',
    ]

def test_transpile_sort_ascending_valid():
    df1 = pd.DataFrame(data={'A': [1, 2, 3, 4, 5]})
    mito = create_mito_wrapper_dfs(df1)
    mito.sort(0, 'A', 'ascending')

    assert mito.transpiled_code == [
        'df1 = df1.sort_values(by=\'A\', ascending=True, na_position=\'first\')',
        'df1 = df1.reset_index(drop=True)',
    ]

def test_transpile_sort_descending_valid():
    df1 = pd.DataFrame(data={'A': [1, 2, 3, 4, 5]})
    mito = create_mito_wrapper_dfs(df1)
    mito.sort(0, 'A', 'descending')

    assert mito.transpiled_code == [
        'df1 = df1.sort_values(by=\'A\', ascending=False, na_position=\'first\')',
        'df1 = df1.reset_index(drop=True)',
    ]

def test_transpile_sort_ascending_then_descending_valid():
    df1 = pd.DataFrame(data={'A': [1, 2, 3, 4, 5]})
    mito = create_mito_wrapper_dfs(df1)
    mito.sort(0, 'A', 'ascending')
    mito.sort(0, 'A', 'descending')

    assert mito.transpiled_code == [
        'df1 = df1.sort_values(by=\'A\', ascending=True, na_position=\'first\')',
        'df1 = df1.reset_index(drop=True)',
        'df1 = df1.sort_values(by=\'A\', ascending=False, na_position=\'first\')',
        'df1 = df1.reset_index(drop=True)'
    ]

def test_transpile_merge_then_sort():
    df1 = pd.DataFrame(data={'Name': ["Aaron", "Nate"], 'Number': [123, 1]})
    df2 = pd.DataFrame(data={'Name': ["Aaron", "Nate"], 'Sign': ['Gemini', "Tarus"]})
    mito = create_mito_wrapper_dfs(df1, df2)
    mito.merge_sheets(0, 'Name', list(df1.keys()), 1, 'Name', list(df2.keys()))
    mito.sort(2, 'Number', 'ascending')

    assert mito.transpiled_code == [
        'temp_df = df2.drop_duplicates(subset=\'Name\')',
        'df3 = df1.merge(temp_df, left_on=[\'Name\'], right_on=[\'Name\'], how=\'left\', suffixes=[\'_df1\', \'_df2\'])',
        'df3 = df3.sort_values(by=\'Number\', ascending=True, na_position=\'first\')',
        'df3 = df3.reset_index(drop=True)'
    ]
