"""
Module to do several scale transformations

"""

import scipy
import numpy
import scipy.interpolate


def log(data, bins=None, axis=0):
    """
    Interpolates a spectrum or any image to be represented
    on a logarithmic scale

    Parameters
    ----------
    data : numpy array
        The image to be transformed.
    bins : int
        Number of bins to interpolate to. Defaults to number of
        bins in input signal.
    axis : int
        The axis to rescale. Defaults to 0.

    Returns
    -------
    data : numpy array
        The transformed image.

    """

    if bins is None:
        bins = data.shape[axis]

    x = numpy.linspace(0, data.shape[axis] - 1, num=data.shape[axis])
    f = scipy.interpolate.interp1d(x, data, axis=axis, kind='linear')
    xnew = numpy.logspace(0, 1, num=bins, base=data.shape[axis]) - 1
    return f(xnew)


def exp(data, bins=None, axis=0):
    """
    Interpolates a spectrum or any image to be represented
    on an exponential scale

    Parameters
    ----------
    data : numpy array
        The image to be transformed.
    bins : int
        Number of bins to interpolate to. Defaults to number of
        bins in input signal.
    axis : int
        The axis to rescale. Defaults to 0.

    Returns
    -------
    data : numpy array
        The transformed image.

    """

    if bins is None:
        bins = data.shape[axis]

    x = numpy.logspace(0, 1, num=data.shape[axis], base=data.shape[axis]) - 1
    f = scipy.interpolate.interp1d(x, data, axis=axis, kind='linear')
    xnew = numpy.linspace(0, data.shape[axis] - 1, num=bins)
    return f(xnew)


def linear(data, bins=None, axis=0):
    """
    Interpolates a spectrum or any image to be represented
    on another linear scale

    Parameters
    ----------
    data : numpy array
        The image to be transformed.
    bins : int
        Number of bins to interpolate to. Defaults to number of
        bins in input signal.
    axis : int
        The axis to rescale. Defaults to 0.

    Returns
    -------
    data : numpy array
        The transformed image.

    """

    if bins is None:
        bins = data.shape[axis]

    x = numpy.linspace(0, data.shape[axis] - 1, num=data.shape[axis])
    f = scipy.interpolate.interp1d(x, data, axis=axis, kind='linear')
    xnew = numpy.linspace(0, data.shape[axis] - 1, num=bins)
    return f(xnew)

lin = linear
