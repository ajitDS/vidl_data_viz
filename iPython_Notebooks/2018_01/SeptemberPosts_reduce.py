#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Victor Calderon
# Created      : 01/25/2018
# Last Modified: 01/25/2018
# Vanderbilt University
from __future__ import print_function, division, absolute_import
__author__     =['Victor Calderon']
__copyright__  =["Copyright 2017 Victor Calderon, "]
__email__      =['victor.calderon@vanderbilt.edu']
__maintainer__ =['Victor Calderon']
"""

"""
# Path to Custom Utilities folder
import os
import sys

# Importing Modules
import numpy as num
import os
import sys
import pandas as pd


# Extra-modules
import argparse
from argparse import ArgumentParser
from argparse import HelpFormatter
from operator import attrgetter

## Functions
class SortingHelpFormatter(HelpFormatter):
    def add_arguments(self, actions):
        """
        Modifier for `argparse` help parameters, that sorts them alphabetically
        """
        actions = sorted(actions, key=attrgetter('option_strings'))
        super(SortingHelpFormatter, self).add_arguments(actions)

def get_parser():
    """
    Get parser object for `eco_mocks_create.py` script.

    Returns
    -------
    args: 
        input arguments to the script
    """
    ## Define parser object
    description_msg = 'Description of Script'
    parser = ArgumentParser(description=description_msg,
                            formatter_class=SortingHelpFormatter,)
    ## 
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    ##
    ## Input file
    parser.add_argument('-f', '--filepath',
                        dest='filepath',
                        help='Path to the input file',
                        default='SeptemberPosts.csv')
    ##
    ## Fraction of the file to reduce
    parser.add_argument('-frac',
                        dest='frac_file',
                        help='Fraction used to reduce size of file',
                        type=float,
                        default=0.1)
    ## Parsing Objects
    args = parser.parse_args()

    return args

def param_vals_test(param_dict):
    """
    Checks if values are consistent with each other.

    Parameters
    -----------
    param_dict: python dictionary
        dictionary with `project` variables

    Raises
    -----------
    ValueError: Error
        This function raises a `ValueError` error if one or more of the 
        required criteria are not met
    """
    ##
    ## Checking that input file exists
    try:
        assert(os.path.exists(param_dict['filepath']))
    except:
        msg = 'Input file ({}) not found!'.format(param_dict['filepath'])
        raise ValueError(msg)


def file_reduce(param_dict):
    """
    Reduces the size/length of the Pandas DataFrame

    Parameters
    ----------
    param_dict: python dictionary
        dictionary with varialbes used throughout this project
    """
    dirname_abs   = os.path.dirname(os.path.abspath(param_dict['filepath']))
    (   basename,
        ext     ) = os.path.basename(param_dict['filepath']).split('.')
    # Reduced filename
    filepath_red  = os.path.join(   dirname_abs,
                                    '{0}_reduced.{1}'.format(basename, ext))
    ##
    ## Reading in input file
    data     = pd.read_csv(param_dict['filepath'])
    data_red = data.sample(frac=param_dict['frac_file']).reset_index()
    data_red.to_csv(filepath_red)
    os.path.exists(filepath_red)
    ##
    print('>>> New file (reduced): {0}\n'.format(filepath_red))


def main(args):
    """

    """
    ## Reading all elements and converting to python dictionary
    param_dict = vars(args)
    ## Checking for correct input
    param_vals_test(param_dict)
    ##
    ## Reducing input file
    file_reduce(param_dict)



# Main function
if __name__=='__main__':
    ## Input arguments
    args = get_parser()
    # Main Function
    main(args)
