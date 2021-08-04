#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Mito.

import json
import uuid 
from copy import copy, deepcopy
import pandas as pd
from typing import List

from mitosheet.state import State
from mitosheet.step import Step
from mitosheet.step_performers import EVENT_TYPE_TO_STEP_PERFORMER
from mitosheet.updates import UPDATES
from mitosheet.preprocessing import PREPROCESS_STEPS
from mitosheet.utils import dfs_to_json, get_new_id
from mitosheet.transpiler.transpile import transpile
from mitosheet.user import get_user_field
from mitosheet.data_in_mito import DataTypeInMito, get_data_type_in_mito
from mitosheet.user import (
    UJ_USER_EMAIL, UJ_RECEIVED_TOURS
)


def get_step_indexes_to_skip(step_list: List[Step]):
    """
    Given a list of steps, will collect all of the steps
    from this list that should be skipped.
    """
    step_indexes_to_skip = set()

    for step_index, step in enumerate(step_list):
        step_indexes_to_skip = step_indexes_to_skip.union(
            step.step_indexes_to_skip(step_list[:step_index])
        )
    
    return step_indexes_to_skip

def execute_step_list_from_index(step_list: List[Step], start_index=None):
    """
    Given a list of steps, and a specific index to start from, will assume that 
    the step_list[start_index] is valid, and execute this list of steps from 
    there. See find_last_valid_index to see how the start_index is determined.

    Notably, will _not_ execute the steps that are skipped in this list, which
    means that the returned step list will only have valid prev_state/post_states 
    for the steps that are not skipped.

    If start_index is not given, will start from the initialize step.
    """
    if start_index is None or start_index < 0:
        start_index = 0
    
    # Get the steps to skip, so that we can skip them
    step_indexes_to_skip = get_step_indexes_to_skip(step_list)
    
    # Get the steps that are valid, and the last valid step, so we can execute from there
    new_step_list = step_list[:start_index + 1] 
    last_valid_step = step_list[start_index]


    for partial_index, step in enumerate(step_list[start_index + 1:]):
        step_index = partial_index + start_index + 1
        # If we're skipping a step, add it to the new step list (since we don't
        # want to lose it), but don't reexecute it 
        if step_index in step_indexes_to_skip:
            new_step_list.append(step)
            continue
        
        # Create a new step with the same params
        new_step = Step(
            step.step_type,
            step.step_id,
            step.params
        )

        # Set the previous state of the new step, and then update 
        # what the last valid step is
        new_step.set_prev_state_and_execute(last_valid_step.post_state)
        last_valid_step = new_step

        new_step_list.append(new_step)
    
    return new_step_list

class StepsManager():
    """
    The StepsManager holds the list of the steps, and makes sure 
    they are updated properly when processing new edit and update 
    events.

    To see how this happens, consider the full loop of what happens
    when a new edit event is received.

    1.  The StepsManager receives this new event. It creates a new
        step of the right type, with the params from the new event. 
        This is done in the handle_edit_event function.
    2.  Then, the StepsManager tries to run all the steps that exist
        including this new step _that are not currently skipped_. 
        It does so with the execute_and_update_steps function, which heavily 
        relies on the execute_step_list_from_index helper function above.
    3.  If the new step that is created is a step that does overwrite an
        existing step, then the execute_and_update_steps will detect 
        this, and when running all the steps, will skip running the skipped step. 

    In this way, the StepsManager keeps a list of all the steps that were ever
    valid. Note that some part of these steps is "append-only" in spirit, in 
    that they keep the same step type and params. 

    However, as some steps end up getting skipped, it may contain steps that 
    are now invalid or out of date (e.g. an old filter step that got skipped). 

    Furthermore, the steps objects themselves change, just the step type
    and parameters stay the same and are append-only.
    """

    def __init__(self, args):
        """
        When initalizing the StepsManager, we also do preprocessing
        of the arguments that were passed to the mitosheet. 

        All preprocessing can be found in mitosheet/preprocessing, and each of 
        the transformations are applied before the data is considered imported.
        """
        # We just randomly generate analysis names. 
        # We append a UUID to note that this is not an analysis the user has saved.
        self.analysis_name = 'UUID-' + str(uuid.uuid4())

        # The args are a tuple of dataframes or strings, and we start by making them
        # into a list, and making copies of them for safe keeping
        self.original_args = [
            arg.copy(deep=True) if isinstance(arg, pd.DataFrame) else deepcopy(arg) for arg in args
        ]

        # Then, we go through the process of actually preprocessing the args
        for PREPROCESS_STEP in PREPROCESS_STEPS:
            args = PREPROCESS_STEP['execute'](args)

        # Then we initialize the analysis with just a simple initialize step
        self.steps: List[Step] = [
            Step(
                'initialize',
                'initialize',
                {},
                None,
                State(args),
                {}
            )
        ]

        # We display the state that exists after the curr_step_idx is applied,
        # which means you can never see before the initalize step
        self.curr_step_idx = 0


    @property
    def curr_step(self) -> Step:
        """
        Returns the current step object as a property of the object,
        so reference it with self.curr_step
        """
        return self.steps[self.curr_step_idx]

    @property
    def num_sheets(self) -> int:
        """
        Duh. :)
        """
        return len(self.steps[self.curr_step_idx].dfs)

    @property
    def dfs(self) -> List[pd.DataFrame]:
        return self.steps[self.curr_step_idx].dfs

    @property
    def df_names_json(self) -> str:
        """
        A JSON object containing the names of the dataframes
        """
        return json.dumps({'df_names': self.curr_step.df_names})
    
    @property
    def df_sources_json(self) -> str:
        """
        A JSON object containing the names of the dataframes
        """
        return json.dumps(self.curr_step.df_sources)

    @property
    def sheet_json(self) -> str:
        """
        sheet_json contains a serialized representation of the data
        frames that is then fed into the ag-grid in the front-end. 

        NOTE: we only display the _first_ 2,000 rows of the dataframe
        for speed reasons. This results in way less data getting 
        passed around
        """
        return dfs_to_json(self.curr_step.dfs)
    
    @property
    def df_shape_json(self) -> str:
        """
        Returns the df shape (rows, columns) of each dataframe in the 
        current step!
        """
        return json.dumps([
            {'rows': df.shape[0], 'cols': df.shape[1]}
            for df in self.curr_step.dfs
        ])

    @property
    def column_spreadsheet_code_json(self) -> str:
        """
        column_spreadsheet_code_json is a list of all the spreadsheet
        formulas that users have used, for each sheet they have. 
        """
        return json.dumps(self.curr_step.column_spreadsheet_code)

    @property
    def code_json(self) -> str:
        """
        This code json string is sent to the front-end and is what
        ends up getting displayed in the codeblock. 
        """
        return json.dumps(transpile(self))

    @property
    def column_filters_json(self) -> str:
        """
        This column_filters list is used by the front end to display
        the filtered icons in the UI
        """
        return json.dumps(self.curr_step.column_filters)
    
    @property
    def column_type_json(self) -> str:
        """
        Returns a list of JSON objects that hold the type of each
        data in each column.
        """
        return json.dumps(self.curr_step.column_type)

    @property
    def data_type_in_mito(self) -> DataTypeInMito:
        return get_data_type_in_mito(self.dfs)

    @property
    def user_email(self) -> str:
        """
        Returns the user_email from user.json
        """
        return get_user_field(UJ_USER_EMAIL)

    @property
    def received_tours(self) -> str:
        """
        Returns the tours that the user has received
        """
        return json.dumps(get_user_field(UJ_RECEIVED_TOURS))

    @property
    def step_summaries_list_json(self) -> str:
        """
        Returns a json list of step summaries, not including
        the skipped steps
        """
        step_summaries_list = []
        step_indexes_to_skip = get_step_indexes_to_skip(self.steps)
        for index, step in enumerate(self.steps):
            if step.step_type == 'initialize':
                step_summaries_list.append({
                    'step_id': step.step_id,
                    'step_idx': 0,
                    'step_type': step.step_type,
                    'step_display_name': "Created a mitosheet",
                    'step_description': "Created a new mitosheet"
                })
                continue
                
            if index in step_indexes_to_skip:
                continue

            step_summaries_list.append({
                'step_id': step.step_id,
                'step_idx': index,
                'step_type': step.step_type,
                'step_display_name': step.step_performer.step_display_name(),
                'step_description': step.step_performer.describe(
                    df_names=step.df_names,
                    **step.params,
                )
            })

        return json.dumps(step_summaries_list)

    def handle_edit_event(self, edit_event):
        """
        Updates the widget state with a new step that was created
        by the edit_event. Each edit event creates one new step.

        If there is an error in the creation of the new step, this
        function will not create the new invalid step.
        """
        # NOTE: We ignore any edit if we are in a historical state, for now. This is a result
        # of the fact that we don't allow previous editing currently
        if self.curr_step_idx != len(self.steps) - 1:
            return

        step_performer = EVENT_TYPE_TO_STEP_PERFORMER[edit_event['type']]

        # First, we make a new step
        new_step = Step(
            step_performer.step_type(),
            edit_event['step_id'],
            edit_event['params']
        )

        new_steps = self.steps + [new_step]

        self.execute_and_update_steps(new_steps)

    def handle_update_event(self, update_event):
        """
        Handles any event that isn't caused by an edit, but instead
        other types of new data coming from the frontend (e.g. the df names 
        or some existing steps).
        """
        for update in UPDATES:
            if update_event['type'] == update['event_type']:
                # Get the params for this event
                params = {key: value for key, value in update_event.items() if key in update['params']}
                # Actually execute this event
                update['execute'](self, **params)
                # And then return
                return

        raise Exception(f'{update_event} is not an update event!')

    def find_last_valid_index(self, new_steps: List[Step]):
        """
        Given the new_steps, this function performs some logic to figure
        out what the last valid index in the steps is (that execution can
        then start from).
        """

        # Currently, we only remove steps in an undo
        if len(new_steps) < len(self.steps):
            # If we are removing steps, then we figure out what skipped steps 
            # we are losing, and run from right before where we are no longer
            # skipped steps
            no_longer_skipped_indexes = set()
            for step_index, removed_step in enumerate(self.steps[len(new_steps):]):
                previous_steps = self.steps[:len(new_steps) + step_index]
                no_longer_skipped_indexes = no_longer_skipped_indexes.union(
                    removed_step.step_indexes_to_skip(previous_steps)
                )

            last_valid_index = min(no_longer_skipped_indexes.union({len(new_steps)})) - 1
        else:
            # Otherwise, if we're adding steps, we figure out which skipped steps
            # we're adding, and run from right before the oldest new skipped step

            # Collect anything that is newly skipped
            newly_skipped_indexes = set()
            for step_index, new_step in enumerate(new_steps[len(self.steps):]):
                previous_steps = new_steps[:len(self.steps) + step_index]
                newly_skipped_indexes = newly_skipped_indexes.union(
                    new_step.step_indexes_to_skip(previous_steps)
                )
            
            # The last valid index is the minimum of the newly skipped things - 1
            # or the last valid step (if nothing is skipped)
            # TODO: we can improve this in the future to remember what it executed last time
            # and so do less work!
            last_valid_index = min(newly_skipped_indexes.union({len(self.steps)})) - 1
        return last_valid_index

    def execute_and_update_steps(self, new_steps: List[Step]):
        """
        Given a list of new_steps, runs them from the last valid index,
        based on what is skipped in these new_steps.

        If these steps all result in valid execution, then we make them
        the steps that the step manager stores. E.g. they become
        the steps of the analysis.
        """
        last_valid_index = self.find_last_valid_index(new_steps)
        final_steps = execute_step_list_from_index(new_steps, start_index=last_valid_index)
        self.steps = final_steps
        self.curr_step_idx = len(self.steps) - 1

    def execute_steps_data(self, new_steps_data=None):
        """
        Given steps data (e.g. from a saved analysis), will turn
        this data  into steps and try to run them. If any of them
        fail, will take none of the new steps
        """
        new_steps = copy(self.steps)
        for step_data in new_steps_data:
            new_step = Step(
                step_data['step_type'],
                get_new_id(),
                step_data['params']
            )

            new_steps.append(new_step)

        self.execute_and_update_steps(new_steps)