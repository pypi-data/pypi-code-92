#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Mito.
# Distributed under the terms of the Modified BSD License.

import pandas as pd
import pytest

from mitosheet.utils import get_new_id
from mitosheet.errors import EditError
from mitosheet.steps_manager import StepsManager
from mitosheet.tests.test_utils import create_mito_wrapper


def test_create_steps_manager():
    df1 = pd.DataFrame(data={'A': [123]})
    df2 = pd.DataFrame(data={'A': [123]})

    steps_manager = StepsManager([df1, df2])
    assert steps_manager.curr_step_idx == 0
    assert steps_manager.curr_step.step_type == 'initialize'
    assert steps_manager.curr_step.column_metatype == [{'A': 'value'}, {'A': 'value'}]
    assert steps_manager.curr_step.column_spreadsheet_code == [{'A': ''}, {'A': ''}]
    assert steps_manager.curr_step.column_python_code == [{'A': ''}, {'A': ''}]
    assert steps_manager.curr_step.column_evaluation_graph == [{'A': set()}, {'A': set()}]
    assert steps_manager.curr_step.column_python_code == [{'A': ''}, {'A': ''}]
    assert steps_manager.curr_step.dfs[0].equals(df1)
    assert steps_manager.curr_step.dfs[1].equals(df2)

# We assume only column A exists
CELL_EDIT_ERRORS = [
    ('=HI()', 'unsupported_function_error'),
    ('=UPPER(HI())', 'unsupported_function_error'),
    ('=UPPER(HI())', 'unsupported_function_error'),
    ('=C', 'no_column_error'),
    ('=C + D', 'no_column_error'),
    ('=ABCDEFG', 'no_column_error'),
    ('=UPPER(C)', 'no_column_error'),
    ('=B', 'circular_reference_error'),
    ('=UPPER(A, 100)', 'execution_error'),
    ('=UPPER(LOWER(A, 100))', 'execution_error')
]

@pytest.mark.parametrize("formula,error_type", CELL_EDIT_ERRORS)
def test_steps_manager_cell_edit_errors(formula,error_type):
    mito = create_mito_wrapper([123])
    mito.add_column(0, 'B')
    with pytest.raises(EditError) as e_info:
        mito.mito_widget.steps_manager.handle_edit_event({
            'event': 'edit_event',
            'id': get_new_id(),
            'type': 'set_column_formula_edit',
            'step_id': get_new_id(),
            'params': {
                'sheet_index': 0,
                'column_header': 'B',
                'old_formula': '=0',
                'new_formula': formula
            }
        })
    assert e_info.value.type_ == error_type

def test_wrong_column_metatype():
    mito = create_mito_wrapper([123])
    mito.add_column(0, 'B')
    with pytest.raises(EditError) as e_info:
        mito.mito_widget.steps_manager.handle_edit_event({
            'event': 'edit_event',
            'id': get_new_id(),
            'type': 'set_column_formula_edit',
            'step_id': get_new_id(),
            'params': {
                'sheet_index': 0,
                'column_header': 'A',
                'old_formula': '=0',
                'new_formula': '=1'
            }
        })
    assert e_info.value.type_ == 'wrong_column_metatype_error'


def test_overwrites_step_valid():
    mito = create_mito_wrapper([1, 2, 3])
    mito.add_column(0, 'B')

    mito.mito_widget.receive_message(mito.mito_widget, {
        'event': 'edit_event',
        'id': get_new_id(),
        'type': 'add_column_edit',
        'step_id': mito.mito_widget.steps_manager.curr_step.step_id,
        'params': {
            'sheet_index': 0,
            'column_header': 'C',
            'column_header_index': 1
        }
    })

    steps_manager = mito.mito_widget.steps_manager
    assert len(steps_manager.steps) == 3
    assert steps_manager.dfs[0].equals(pd.DataFrame(data={'A': [1, 2, 3], 'C': [0, 0, 0]}))


def test_failed_overwrite_rolls_back_to_previous_state():
    mito = create_mito_wrapper([1, 2, 3])
    mito.add_column(0, 'B')

    mito.mito_widget.receive_message(mito.mito_widget, {
        'event': 'edit_event',
        'id': get_new_id(),
        'type': 'add_column_edit',
        'step_id': mito.mito_widget.steps_manager.curr_step.step_id,
        'params': {
            'sheet_index': 1,
            'column_header': 'C',
            'column_header_index': 2
        }
    })

    steps_manager = mito.mito_widget.steps_manager
    assert len(steps_manager.steps) == 2
    assert steps_manager.dfs[0].equals(pd.DataFrame(data={'A': [1, 2, 3], 'B': [0, 0, 0]}))


