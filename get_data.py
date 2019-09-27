"""get_data.py contains functions to import data

    * read_stdin_col(col_num) - read columns of data from the standard in
    and output the desired column into a list
"""

import sys

def read_stdin_col(col_num):
    """ Read data from stdin. Expects columns of numerical data.

    Parameters
    -----------
    col_num : the column of data from stdin to collect

    Returns
    --------
    L : a list containing the specified column of data from stdin

    """

    L = []

    # stdin may come from gen_data.sh
    for l in sys.stdin:
        A = l.rstrip().split()
        L.append(float(A[col_num]))
    return L
