"""
Module to filter audio signals using numpy arrays

Functions
---------
`lowpass`: Filter a given signal using a lowpass filter.

`medianlimiter`: Find the minimum between a sliding median value and a sample.

"""
import scipy.signal
import numpy
import Transform

def lowpass(x, cutoff, fs, coeffs=61, window='hanning'):
    """
    Filter a signal with a lowpass

    Parameters
    ----------
    data : numpy array
        Input signal.
    cutoff : int
        Cutoff frequency.
    fs : int
        Sampling rate.
    coeffs : int
        Coefficients. Defaults to 61.
    window : string
        Filter window to be used. Defaults to 'hanning'.

    Returns
    -------
    data : numpy array
        The filtered signal

    """
    taps = scipy.signal.firwin(coeffs, cutoff/(float(fs)/2), window=window)
    return scipy.signal.lfilter(taps, 1.0, x)

def medianlimiter(x, size=11, weight=1):
    """
    Limit a signal with a sliding median window.

    To calculate the output signal, a sliding median value is calculated
    for each sample in the signal. This median value is then being compared
    to the current sample and the minimum of the two is chosen.

    Parameters
    ----------
    data : numpy array
        Input signal.
    size : int
        Size of the sliding window. Defaults to 11.
    weight : int
        Weighting coefficient for the median window. Defaults to 1.

    Returns
    -------
    data : numpy array
        The filtered signal.

    """
    return x / numpy.abs(x) * numpy.minimum(numpy.abs(x), weight*numpy.median(Transform.slidingwindow(numpy.abs(x), size=size), axis=1))
