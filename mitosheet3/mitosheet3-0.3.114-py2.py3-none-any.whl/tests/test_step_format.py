#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Mito.
# Distributed under the terms of the Modified BSD License.

"""
Contains tests for edit events.
"""
import random
from typing import List

from mitosheet.step_performers import (
    STEP_PERFORMERS,
    StepPerformer,
    PivotStepPerformer,
    FilterStepPerformer,
    SortStepPerformer,
    ReorderColumnStepPerformer,
    AddColumnStepPerformer,
    SetColumnFormulaStepPerformer,
    MergeStepPerformer,
    DeleteColumnStepPerformer,
    RenameColumnStepPerformer,
    ChangeColumnDtypeStepPerformer,
    SimpleImportStepPerformer,
    DataframeDeleteStepPerformer,
    DataframeDuplicateStepPerformer,
    DataframeRenameStepPerformer
)

def check_step(
        step_performer: StepPerformer, 
        step_version: int, 
        step_type: str
    ):
    """
    Helper function that checks a given step definition against the 
    expected step_version, step_type, and params for that step. 

    Throws an assertion error if any of them do not match! 
    """
    assert step_performer.step_version() == step_version
    assert step_performer.step_type() == step_type

def test_params_static():
    """
    NOTE: This is a regression test! Before changing this test to make it pass, talk to 
    the engineering team and make sure you know what you're doing. 

    Remeber:
    1. Each Mito analysis is written to a file, where each step is saved with its
       parameters.
    2. If the _name_ of the step, or the _parameters to the step_ change, then this
       will break existing user analyses. 
    
    Thus, this test is to make sure that we _know_ when we're breaking things. 
    
    However, note that there are ways to break existing user analyses other than this. 
    For example, if you change how the group step flattens headers, this may cause
    issues if the user then later renames one of those flattened columns. So, this
    regression test is not perfect, but it is a good start!
    """

    check_step(
        AddColumnStepPerformer,
        2,
        'add_column'
    )

    check_step(
        DeleteColumnStepPerformer,
        1,
        'delete_column'
    )

    check_step(
        RenameColumnStepPerformer,
        1,
        'rename_column'
    )

    check_step(
        FilterStepPerformer,
        2,
        'filter_column'
    )
    
    check_step(
        PivotStepPerformer,
        3,
        'pivot'
    )

    check_step(
        MergeStepPerformer,
        1,
        'merge'
    )

    check_step(
        ReorderColumnStepPerformer,
        1,
        'reorder_column'
    )

    check_step(
        SetColumnFormulaStepPerformer,
        1,
        'set_column_formula'
    )

    check_step(
        SortStepPerformer,
        1,
        'sort'
    )


    check_step(
        ChangeColumnDtypeStepPerformer,
        1,
        'change_column_dtype'
    )

    check_step(
        SimpleImportStepPerformer,
        1,
        'simple_import'
    )

    check_step(
        DataframeDeleteStepPerformer,
        1,
        'dataframe_delete'
    )

    check_step(
        DataframeDuplicateStepPerformer,
        1,
        'dataframe_duplicate'
    )

    check_step(
        DataframeRenameStepPerformer,
        1,
        'dataframe_rename'
    )

    assert len(STEP_PERFORMERS) == 14


def get_fake_param(param_name):
    if 'index' in param_name:
        return random.randint(0, 2)
    else:
        return 'data'