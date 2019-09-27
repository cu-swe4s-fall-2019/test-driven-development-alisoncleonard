import math_lib as ml
import matplotlib
import matplotlib.pyplot as plt
import sys
import os.path
from os import path
matplotlib.use('Agg')

"""Plotting functions using matplotlib

    * boxplot
    * histogram
    * combo
"""


def boxplot(L, out_file_name):

    """Create a boxplot from an list of data and save the graph to an
    output file

    Parameters
    ___________

    L: list of ints or floats
        data to be graphed

    out_file_name:
        The file name the graph will be saved under. Must use a supported file
        extension, such as .png

    Returns
    _________

    a box plot saved as out_file_name in the current directory

    """

# check that the out file will not write over existing data
    if path.exists(out_file_name):
        raise Exception('Output file already exists. Choose a new name')
        sys.exit(1)

    try:
        out_file = out_file_name

        mean = ml.list_mean(L)
        stdev = ml.list_stdev(L)

        width = 3
        height = 3

        fig = plt.figure(figsize=(width, height), dpi=300)
        ax = fig.add_subplot(1, 1, 1)

        ax.boxplot(L)
        title = 'mean '+str(round(mean, 3))+' stdev: '+str(round(stdev, 3))
        ax.set_title(title)
        ax.set_xlabel('Input List')
        ax.set_ylabel('Distribution of Values')

        plt.savefig(out_file, bbox_inches='tight')

    except ValueError:
        raise ValueError('Can not support file extension. Try .png instead')


def histogram(L, out_file_name):

    """Create a histogram from an list of data and save the graph to an
    output file

    Parameters
    ___________

    L: list of ints or floats
        data to be graphed

    out_file_name:
        The file name the graph will be saved under. Must use a supported file
        extension, such as .png

    Returns
    _________

    a histogram saved as out_file_name in the current directory

    """
    # check that the out file will not write over existing data
    if path.exists(out_file_name):
        raise Exception('Output file already exists. Choose a new name')
        sys.exit(1)

    try:
        out_file = out_file_name

        mean = ml.list_mean(L)
        stdev = ml.list_stdev(L)

        width = 3
        height = 3

        fig = plt.figure(figsize=(width, height), dpi=300)

        ax = fig.add_subplot(1, 1, 1)

        ax.hist(L, 20)
        title = 'mean '+str(round(mean, 3))+' stdev: '+str(round(stdev, 3))
        ax.set_title(title)
        ax.set_xlabel('Value')
        ax.set_ylabel('Frequency')

        plt.savefig(out_file, bbox_inches='tight')

    except ValueError:
        raise ValueError('Can not support file extension. Try .png instead')


def combo(L, out_file_name):

    """Create a combination plot with a boxplot and histogram  from an list of
    data and save the graph to an output file

    Parameters
    ___________

    L: list of ints or floats
    data to be graphed

    out_file_name:
    The file name the graph will be saved under. Must use a supported file
    extension, such as .png

    Returns
    _________

    a combination boxplot and histogram, saved as out_file_name in the
    current directory

    """

    # check that the out file will not write over existing data
    if path.exists(out_file_name):
        raise Exception('Output file already exists. Choose a new name')
        sys.exit(1)

    try:

        out_file = out_file_name

        mean = ml.list_mean(L)
        stdev = ml.list_stdev(L)

        width = 5
        height = 3

        fig = plt.figure(figsize=(width, height), dpi=300)

        ax = fig.add_subplot(1, 1, 1)

        ax.boxplot(L)
        ax.hist(L, 20)
        # combo plot uses same title and axis labels for both plots
        title = 'mean '+str(round(mean, 3))+' stdev: '+str(round(stdev, 3))
        ax.set_title(title)
        ax.set_xlabel('Values')
        ax.set_ylabel('Histogram: frequency; Boxplot: distribution of values')

        plt.savefig(out_file, bbox_inches='tight')

    except ValueError:
        raise ValueError('Can not support file extension. Try .png instead')
