"""
Module to calculate several operators from a signal

Functions
---------
`teager`: Calculate teager operator from signal

`frequency`: Calculate something from some paper

`amplitude`: Calculate something from some paper

"""
import numpy
from numpy import logical_and, average, diff
from matplotlib.mlab import find

def teager(data):
    """
    Return the teager values for a signal

    Parameters
    ----------
    data : numpy array
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
    .. [1] J. F. Kaiser, "On a simple algorithm to calculate the 'energy' of
           a signal", IEEE (1990).

    """
    e = data[1:-1]**2 - data[2:]*data[:-2]
    return numpy.hstack((e[0], e, e[-1]))

def frequency(data):
    """
    Return the teager values for a signal

    Parameters
    ----------
    data : numpy array
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
    .. [1] Y. Litvin et al., "Monoaural speech/music source separation using
           discrete energy separation algorithm", Signal Processing 90 (2010).

    """
    return numpy.arccos( 1 - ( teager(data[2:]-data[:-2]) / 2*teager(data[1:-1]) ) ) / 2

def amplitude(data):
    """
    Return the teager values for a signal

    Parameters
    ----------
    data : numpy array
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
    .. [2] Y. Litvin et al., "Monoaural speech/music source separation using
           discrete energy separation algorithm", Signal Processing 90 (2010).

    """
    return 2*teager(data[1:-1]) / numpy.sqrt(teager(data[2:]-data[:-2]))

def freq_from_crossings(sig, fs):
    """
    Estimate frequency by counting zero crossings

    Parameters
    ----------
    data : numpy array
        Input signal
    fs : int
        Sampling frequency

    Returns
    -------
    data : int
        Estimated frequency

    Notes
    -----

    * Doesn't work if there are multiple zero crossings per cycle.

    References
    ----------
    .. [3] https://gist.github.com/endolith/129445

    """

    indices = find(logical_and(sig[1:] >= 0, sig[:-1] < 0))

    # Linear interpolation to find truer zero crossings
    crossings = [i - sig[i] / (sig[i+1] - sig[i]) for i in indices]

    return fs / average(diff(crossings))