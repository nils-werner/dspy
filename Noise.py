"""
Module to add noise to numpy arrays

Functions
---------
`white`: Add white noise.

`brown`: Add brown noise.

`pepper`: Add salt/pepper noise.

"""

import numpy
import numpy.random

def pepper(data, probability=0.1, minv=None, maxv=None):
    """
    Add salt and pepper noise to signal.

    Parameters
    ----------
    data : numpy array
        Input signal.
    probability : float
        Probability of a single cell being either salt or pepper
    minv : mixed
        Minimum value. Defaults to the data type minimum.
    maxv : mixed
        Maximum value. Defaults to the data type maximum.

    Returns
    -------
    data : numpy array
        Output signal

    """
    if maxv is None:
        try:
            maxv = numpy.finfo(data.dtype).max
        except:
            maxv = numpy.iinfo(data.dtype).max

    if minv is None:
        try:
            minv = numpy.finfo(data.dtype).min
        except:
            minv = numpy.iinfo(data.dtype).min

    mask = numpy.random.randint(0, 2/probability+1, size=data.shape)
    data[mask == 0] = minv
    data[mask == 2/probability] = maxv
    return data