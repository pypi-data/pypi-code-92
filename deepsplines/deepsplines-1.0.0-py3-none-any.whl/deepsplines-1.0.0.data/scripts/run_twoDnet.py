#!python
'''
This script reproduces the results for twoDnet
on an s-shape or circle 2D dataset.

See https://ieeexplore.ieee.org/document/9264754.
'''

import os
import argparse
import copy
import torch

from deepsplines.main import main_prog
from deepsplines.datasets import generate_save_dataset


def run_twoDnet(args):
    """
    Args:
        args: verified arguments from arparser
    """
    if not os.path.isdir(args.log_dir):
        print(f'\nLog directory {args.log_dir} not found. Creating it.')
        os.makedirs(args.log_dir)

    if not os.path.isdir(os.path.join(args.data_dir, args.dataset_name)):
        generate_save_dataset(args.dataset_name, args.data_dir)

    device = "cuda:0" if torch.cuda.is_available() else "cpu"

    if args.activation_type == 'deepspline':
        activation_type = 'deepBspline'
    else:
        activation_type = 'relu'

    params = {
        'net': 'twoDnet',
        'device': device,
        'log_dir': args.log_dir,
        'num_epochs': 500,
        'milestones': [440, 480],
        'activation_type': activation_type,
        'spline_init': 'leaky_relu',
        'spline_size': 21,
        'spline_range': 1,
        'save_memory': False,
        'lipschitz': False,
        'lmbda': 1e-5,
        'optimizer': ['Adam'],
        'lr': 1e-3,
        'weight_decay': 1e-5,
        'log_step': None,  # At every epoch
        'valid_log_step': None,  # at halfway and end of training
        'test_as_valid': True,  # print test loss at validation
        'dataset_name': args.dataset_name,
        'batch_size': 10,  # small batch size to avoid local minima
        'plot_imgs': False,
        'verbose': False
    }

    params['model_name'] = f'{params["net"]}_{params["activation_type"]}_' + \
        'lambda_{:.1E}'.format(params["lmbda"])

    params['mode'] = 'train'
    main_prog(copy.deepcopy(params))

    # params['mode'] = 'test'
    # main_prog(copy.deepcopy(params))

    # Note:
    # After training, we can run sparsify_with_optimal_knot_threshold.py
    # on the last saved checkpoint to sparsify the activations of the model.


if __name__ == "__main__":

    # parse arguments
    parser = argparse.ArgumentParser(
        description='Run twoDnet on an s_shape or circle 2D dataset.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    dataset_choices = {'s_shape', 'circle'}
    parser.add_argument('dataset_name',
                        metavar='dataset_name [STR]',
                        choices=dataset_choices,
                        type=str,
                        help=f'{dataset_choices}')
    parser.add_argument('--data_dir',
                        metavar='[STR]',
                        type=str,
                        default='./data',
                        help='Directory where twoD dataset (generated by '
                        'generate_save_twoD_dataset.py) is located. '
                        'Otherwise, if it does not exist, generate it and '
                        'save it in this directory. (default: %(default)s)')
    parser.add_argument('--log_dir',
                        metavar='[STR]',
                        type=str,
                        default='./ckpt',
                        help='Model log directory.')
    parser.add_argument('--activation_type',
                        choices=['deepspline', 'relu'],
                        type=str,
                        default='deepspline',
                        help=' ')

    args = parser.parse_args()

    run_twoDnet(args)
