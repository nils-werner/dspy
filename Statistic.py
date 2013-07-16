"""
Module to calculate statistic information from a signal

Functions
---------
`autocorr`: Calculate the autocorrelation function of a signal

`quadraticdiff`: Calculate the quadratic difference between two signals

"""
import numpy

def autocorr(x, **kwargs):
    """
    Return the autocorrelation function of a signal

    Parameters
    ----------
    signal : numpy array
        The signal to be calculated.

    ... : mixed
        All other named arguments accepted
        by `numpy.correlate()`.

    Returns
    -------
    data : numpy array
        The autocorrelation function

    """
    kwargs.setdefault('mode', 'full')

    result = numpy.correlate(x, x, **kwargs)
    return result[result.size/2:]

def quadraticdiff(a, b):
    """
    Return the quadratic difference of two signals

    Parameters
    ----------
    a : numpy array
        The first signal.
    b : numpy array
        The second signal.

    Returns
    -------
    data : numpy array
        The quadratic difference between the two signals

    """
    return numpy.sum((a - b)**2)
