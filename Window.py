"""
Module to weigh a signal with a windowing function

Functions
---------
`halfsin`: Returns a simple halfsin window

`window`: Weighs a signal with the halfsin window

"""
import numpy

def halfsin(M):
    """
    Gernerate a halfsin/halfcosine window of given length

    Parameters
    ----------
    M : int
        Length of the window.

    Returns
    -------
    data : numpy array
        The window function

    """
    return numpy.sin(numpy.pi / M * (numpy.arange(0, M) + .5))

def window(sig):
    """
    Weigh a signal with the halfsin window function

    Parameters
    ----------
    signal : numpy array
        The input signal.

    Returns
    -------
    data : numpy array
        The weighted input signal.

    """
    return sig * halfsin(len(sig))
