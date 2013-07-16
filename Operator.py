"""
Module to calculate several operators from a signal

Functions
---------
`teager`: Calculate teager operator from signal

`frequency`: Calculate something from some paper

`amplitude`: Calculate something from some paper

"""
import numpy

def teager(x):
    """
    Return the teager values for a signal

    Parameters
    ----------
    signal : numpy array
        Input signal

    Returns
    -------
    data : numpy array
        Teager values

    Notes
    -----

    * Maximum frequency of the signal should be
      1/4 of the Niquyst frequency
    * The result is padded on each side to match the
      size of the input signal.

    References
    ----------
    .. [1] @TODO

    """
    e = x[1:-1]**2 - x[2:]*x[:-2]
    return numpy.hstack((e[0], e, e[-1]))

def frequency(x):
    """
    Return the teager values for a signal

    Parameters
    ----------
    signal : numpy array
        Input signal

    Returns
    -------
    data : numpy array
        Teager values

    Notes
    -----

    * Maximum frequency of the signal should be
      1/4 of the Niquyst frequency
    * The result is padded on each side to match the
      size of the input signal.

    References
    ----------
    .. [1] @TODO

    """
    return numpy.arccos( 1 - ( teager(x[2:]-x[:-2]) / 2*teager(x[1:-1]) ) ) / 2

def amplitude(x):
    """
    Return the teager values for a signal

    Parameters
    ----------
    signal : numpy array
        Input signal

    Returns
    -------
    data : numpy array
        Teager values

    Notes
    -----

    * Maximum frequency of the signal should be
      1/4 of the Niquyst frequency
    * The result is padded on each side to match the
      size of the input signal.

    References
    ----------
    .. [1] @TODO

    """
    return 2*teager(x[1:-1]) / numpy.sqrt(teager(x[2:]-x[:-2]))
