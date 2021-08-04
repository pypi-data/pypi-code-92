#!/usr/bin/env python3

"""Module containing the Undersampling class and the command line interface."""
import argparse
import pandas as pd
import numpy as np
from collections import defaultdict
import random
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_common.command_wrapper import cmd_wrapper
from biobb_ml.utils.common import *


class Undersampling():
    """Undersamples a given dataset.

    Args:
        input_dataset_path (str): Path to the input dataset. File type: input. `Sample file <>`_. Accepted formats: csv.
        output_dataset_path (str): Path to the output dataset. File type: output. `Sample file <>`_. Accepted formats: csv.
        properties (dic):
            * **divisions** (*int*) - (25000) Numer of divisions.
            * **top_points** (*int*) - (-1000) Pick top points.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
    """

    def __init__(self, input_dataset_path, 
                 output_dataset_path, properties=None, **kwargs) -> None:
        properties = properties or {}

        # Input/Output files
        self.io_dict = { 
            "in": { "input_dataset_path": input_dataset_path }, 
            "out": { "output_dataset_path": output_dataset_path } 
        }

        # Properties specific for BB
        self.divisions = properties.get('divisions', 25000)
        self.top_points = properties.get('top_points', -1000)
        self.properties = properties

        # Properties common in all BB
        self.can_write_console_log = properties.get('can_write_console_log', True)
        self.global_log = properties.get('global_log', None)
        self.prefix = properties.get('prefix', None)
        self.step = properties.get('step', None)
        self.path = properties.get('path', '')
        self.remove_tmp = properties.get('remove_tmp', True)
        self.restart = properties.get('restart', False)

    def check_data_params(self, out_log, err_log):
        """ Checks all the input/output paths and parameters """
        self.io_dict["in"]["input_dataset_path"] = check_input_path(self.io_dict["in"]["input_dataset_path"], "input_dataset_path", out_log, self.__class__.__name__)
        self.io_dict["out"]["output_dataset_path"] = check_output_path(self.io_dict["out"]["output_dataset_path"],"output_dataset_path", False, out_log, self.__class__.__name__)


    @launchlogger
    def launch(self) -> int:
        """Launches the execution of the Undersampling module."""

        # Get local loggers from launchlogger decorator
        out_log = getattr(self, 'out_log', None)
        err_log = getattr(self, 'err_log', None)

        # check input/output paths and parameters
        self.check_data_params(out_log, err_log)

        # Check the properties
        fu.check_properties(self, self.properties)

        if self.restart:
            output_file_list = [self.io_dict["out"]["output_dataset_path"]]
            if fu.check_complete_files(output_file_list):
                fu.log('Restart is enabled, this step: %s will the skipped' % self.step, out_log, self.global_log)
                return 0

        # load dataset
        fu.log('Getting dataset from %s' % self.io_dict["in"]["input_dataset_path"], out_log, self.global_log)
        data = pd.read_csv(self.io_dict["in"]["input_dataset_path"], sep="\s+|;|:|,|\t", engine="python")

        strings = list(data["ID_REF"])
        values = list(data["VALUE"])
        weights = list(data["WEIGHTEDSCORE"])  # pick either WEIGHT or WEIGHTEDSCORE

        # TODO NEW UTIL SCALE PASSING IT COLUMNS TO SCALE
        #scale
        values = [(value-min(values))/(max(values)-min(values)) for value in values]

        # creates dictionaries with normalized values and seq.strings / weights
        dictionary = dict(zip(values, strings))
        weight_dict = dict(zip(values, weights))

        # affinitiy boundaries
        sort_aff = sorted(values)
        # pick top points ~ proportion 1:500 before undersampling i.e. we pick 50 top points not to undersample
        upper_bound = sort_aff[self.top_points]

        # interval dictionary -- maybe it is not the best option? idk it works for now...
        interval_dict = defaultdict(list)
        for value in values:
            interval_dict[int(value*self.divisions)].append(value)

        # creates a matrix of values: we pick one value for the intervals where i<self.divisions/2
        # and up to two for i>self.divisions/2

        training_ordered = []
        start = 1 # i.e. starts picking values larger than start/self.divisions from the normalized affinites

        for i in np.arange(start,self.divisions+1):
            if len(interval_dict[i])>0:
                if i <= self.divisions*upper_bound:
                    random_values = [random.choice(interval_dict[i]) for j in np.arange(0,20)]
                    random_values = set(random_values)
                    value = random.choice(interval_dict[i])
                    training_ordered.append([dictionary[value], value, weight_dict[value]])
                if i > self.divisions*upper_bound:
                    for value in interval_dict[i]:
                        training_ordered.append([dictionary[value], value, weight_dict[value]])

        # writes the randomized file ready for training
        np.random.shuffle(training_ordered)

        fu.log('Saving output dataset to %s' % self.io_dict["out"]["output_dataset_path"], out_log, self.global_log)

        with open(self.io_dict["out"]["output_dataset_path"],'w') as file:
            file.write('ID_REF,VALUE,WEIGHT\n')
            
        with open(self.io_dict["out"]["output_dataset_path"],'a') as file:
            for vector in training_ordered:
                file.write("%s," % vector[0])
                file.write("%s," % vector[1])
                file.write("%s\n" % vector[2])

        return 0

def main():
    parser = argparse.ArgumentParser(description="Generates a Undersampling from a given dataset", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')

    # Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_dataset_path', required=True, help='Path to the input dataset. Accepted formats: csv.')
    required_args.add_argument('--output_dataset_path', required=True, help='Path to the output dataset. Accepted formats: csv.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config).get_prop_dic()

    # Specific call of each building block
    Undersampling(input_dataset_path=args.input_dataset_path,
                   output_dataset_path=args.output_dataset_path,
                   properties=properties).launch()

if __name__ == '__main__':
    main()

