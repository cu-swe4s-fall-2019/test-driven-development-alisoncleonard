"""Math function library

    * list_mean - returns the mean of a list containing integers and floats
    * list_stdev - returns the population standard deviation of a list
        containing inegers and floats
"""

import math


def list_mean(L):
    """Compute the mean of a list. List must contain only ints and floats.
    Returns None when passed a None list or an empty list.

    Parameters
    -----------
    L: list of ints or floats

    Returns
    --------
    mean = the mean of the values in L
    """

    try:
        if L is None:
            return None
        if L == []:
            return None
        sum = 0
        for item in L:
            # check that values are only ints or floats
            if not isinstance(item, int) and not isinstance(item, float):
                message = 'Unsupported value. List of ints and floats only'
                raise ValueError(message)
            sum += float(item)
        mean = sum / len(L)
        return mean
    except TypeError:
        raise TypeError('Unsupported data type. Must pass a list')


def list_stdev(L):
    """Compute the standard deviation of a list. List must contain only ints
    and floats. Returns None when passed a None list or an empty list.

    Parameters
    -----------
    L: list of ints or floats

    Returns
    --------
     stdev = the population standard deviation of the values in L
    """

    try:
        if L is None:
            return None
        if L == []:
            return None
        # calls list_mean function to calculate mean
        # no additional check for ints and floats needed, done in list_mean
        mean = list_mean(L)
        stdev = math.sqrt(sum([(mean-x)**2 for x in L]) / len(L))
        return stdev
    except TypeError:
        raise TypeError('Unsupported data type. Must pass a list')
