"""This script uses the modules get_data.py and data_viz.py to read data
    from stdin and produce graphs showing the mean and standard deviation.
"""

import get_data
import data_viz
import sys
import argparse


def main():
    """
    Read numerical data from the standard input, calculate the mean and
    standard deviation, and save data as a box plot or histogram

    Parameters
    -----------

    --out_file : the desired name of the saved plot, with the png extension

    --plot_type : the type of plot to produce. Choices are histogram, boxplot,
    or combo.

    Returns
    --------

    A plot saved as --out_file

    """
    parser = argparse.ArgumentParser(description='produce a plot of data from '
                                     'stdin', prog='viz')

    parser.add_argument('--out_file', type=str,
                        help='Name of output file', required=True)

    parser.add_argument('--plot_type', type=str,
                        help='The plot type, lowercase', required=True)

    args = parser.parse_args()

    out_file_name = args.out_file
    plot = args.plot_type

    # hardcoding the columns output from gen_data.sh
    # output of read_stdin_col is a list
    col_1 = get_data.read_stdin_col(0)
    col_2 = get_data.read_stdin_col(1)

    # merge both lists into one for graphing
    L = []
    for i in col_1:
        L.append(i)
    for j in col_2:
        L.append(j)

    data_viz.histogram(L, out_file_name)

    # try:
    #    if plot == histogram:
    #        data_viz.histogram(L, out_file_name)
    #    if plot == boxplot:
    #        data_viz.boxplot(L, out_file_name)
    #    if plot == combo:
    #        data_viz.combo(L, out_file_name)

    # except NameError:
    #    print('Plot type not available. Check help for available types')
    #    sys.exit(1)


if __name__ == '__main__':
    main()
