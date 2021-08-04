

from mitosheet.step_performers.step_performer import StepPerformer
from mitosheet.step_performers.column_steps.set_column_formula import SetColumnFormulaStepPerformer
from mitosheet.step_performers.filter import FilterStepPerformer
from typing import Any, Dict, List, Optional

from mitosheet.state import State
from mitosheet.step_performers import STEP_TYPE_TO_STEP_PERFORMER


class Step:
    """
    A step is a container around a specific data transformation.

    A step has parameters - e.g. which sheet it touches, which column
    it edits.

    It then is linked to a StepPerformer class via the step_type. 
    The Step uses a mapping from its step_type to the StepPerformer 
    to figure out the correct step generator to use at any given time. 

    This StepPerformer is responsible for "executing" this step, which 
    functionally means taking the prev_state that this step starts at,
    and using the step's parameters to create a new post_state that 
    is up to date.

    This also stores execution_data from that execution - which makes
    for easy transpiling of the step! For example, a simple import
    stores what the delimeters used in the files it read in are, so
    that it can transpile this easily.
    """

    def __init__(
        self, 
        step_type: str, 
        step_id: str, 
        params: Dict[str, Any],
        prev_state: Optional[State] = None,
        post_state: Optional[State] = None,
        execution_data: Optional[Dict[str, Any]] = None,
    ):
        # The type of the step, one for each type of transformation
        self.step_type = step_type
        # The id of the step, so that steps can overwrite eachother by id
        self.step_id = step_id
        # The parameters that the step takes as input - which in turn are used
        # in execution, transpilation, and in describing the step
        # NOTE: these must be saturated before they can be used!
        self.params = params

        # The state at the start of this step; is None only for the initialize step
        self.prev_state = prev_state
        # The state you get from executing the prev_state with the passed params
        self.post_state = post_state
        # execution_data is data from the execution of the data transformation that
        # is useful for the transpiler - that means the transpiler can do way less
        # work if it has already been done. See simple_import for an example
        self.execution_data = execution_data

    @property
    def dfs(self):
        return self.post_state.dfs

    @property
    def df_names(self):
        return self.post_state.df_names

    @property
    def df_sources(self):
        return self.post_state.df_sources

    @property
    def column_metatype(self):
        return self.post_state.column_metatype

    @property
    def column_type(self):
        return self.post_state.column_type
    
    @property
    def column_spreadsheet_code(self):
        return self.post_state.column_spreadsheet_code

    @property
    def column_evaluation_graph(self):
        return self.post_state.column_evaluation_graph

    @property
    def column_python_code(self):
        return self.post_state.column_python_code
    
    @property
    def column_filters(self):
        return self.post_state.column_filters

    @property
    def step_performer(self) -> StepPerformer:
        """
        A helper function to return the step performer class
        that is associated with this step, based on step type.

        This is useful for other pieces of the codebase
        that need the step performer.
        """
        step_performer = STEP_TYPE_TO_STEP_PERFORMER[self.step_type]
        return step_performer


    def set_prev_state_and_execute(self, new_prev_state):
        """
        Changes the prev_state of this step, which in turns triggers
        a reexecution with the same parameters. 

        If successful, will update the step in-place. If it fails, 
        this will not update the step.

        NOTE: this is the only function you should use to get a step
        to execute!
        """        
        # Saturate the event to get up to date parameters
        params = self.step_performer.saturate(new_prev_state, self.params)

        # Actually execute the data transformation
        post_state_and_execution_data = self.step_performer.execute(new_prev_state, **params)

        if post_state_and_execution_data is not None:
            # 
            (new_post_state, execution_data) = post_state_and_execution_data
        else:
            # Sometimes step execution returns None, which functionally means that 
            # nothing changed in the step (but we need not error). In this case, we
            # just don't change anything in the state
            new_post_state, execution_data = new_prev_state, []
        
        # Update the relevant state variables
        self.prev_state = new_prev_state
        self.post_state = new_post_state
        self.execution_data = execution_data
        self.params = params
    

    def step_indexes_to_skip(self, all_steps_before_this_step):
        """
        Given the steps that come before it, any step has the ability
        to skip these steps. 

        Currently, a step only skips the steps before it if:
        1. This step is a filter step that is trying to replace an older filter step
        2. This step has the same id as any step before it (like for pivot tables)
        3. This step is a formula step overwriting the step that came just before it
        """

        step_indexes_to_skip = set()

        for step_index, step in enumerate(all_steps_before_this_step):
            step: Step = step
            # Check (1)
            if step.step_type == FilterStepPerformer.step_type() and self.step_type == FilterStepPerformer.step_type():
                if step.params['sheet_index'] == self.params['sheet_index'] \
                    and step.params['column_header'] == self.params['column_header']:
                   step_indexes_to_skip.add(step_index) 
            
            # Check (2)
            elif step.step_id == self.step_id:
                step_indexes_to_skip.add(step_index)

        if len(all_steps_before_this_step) > 0:
            previous_step: Step = all_steps_before_this_step[-1]
            
            
            # Check (3)
            if self.step_type == SetColumnFormulaStepPerformer.step_type():
                if self.step_type == previous_step.step_type \
                    and self.params['sheet_index'] == previous_step.params['sheet_index'] \
                    and self.params['column_header'] == previous_step.params['column_header']:
                    step_indexes_to_skip.add(len(all_steps_before_this_step) - 1)

        return step_indexes_to_skip


