"""
Module to filter audio signals using numpy arrays

Functions
---------
`lowpass`: Filter a given signal using a lowpass filter.

`medianlimiter`: Find the minimum between a sliding median value and a sample.

"""
import scipy.signal
import numpy
from . import Transform

def lowpass(data, cutoff, fs, coeffs=61, window='hanning', unshift=False):
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
    unshift : boolean
        Unshift result by filter delay. Defaults to false.

    Returns
    -------
    data : numpy array
        The filtered signal

    """
    taps = scipy.signal.firwin(coeffs, cutoff/(float(fs)/2.0), window=window)
    data = scipy.signal.lfilter(taps, 1.0, data)

    if unshift is True:
        return numpy.roll(data, -coeffs // 2)
    else:
        return data

def highpass(data, cutoff, fs, coeffs=61, window='hanning', unshift=False):
    """
    Filter a signal with a highpass

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
    unshift : boolean
        Unshift result by filter delay. Defaults to false.

    Returns
    -------
    data : numpy array
        The filtered signal

    """
    taps = scipy.signal.firwin(coeffs, cutoff/(float(fs)/2.0), window=window)
    taps = -taps
    taps[coeffs/2] = taps[coeffs/2] + 1
    data = scipy.signal.lfilter(taps, 1.0, data)

    if unshift is True:
        return numpy.roll(data, -coeffs // 2)
    else:
        return data

def bandpass(data, cutoff_low, cutoff_high, fs, order=9, **kwargs):
    """
    Filter a signal with a bandpass

    Parameters
    ----------
    data : numpy array
        Input signal.
    cutoff_low : int
        Lower end cutoff frequency.
    cutoff_high : int
        Upper end cutoff frequency.
    fs : int
        Sampling rate.
    order : int
        Order of filter. Defaults to 9.
    window : string
        Filter window to be used. Defaults to 'hanning'.
    unshift : boolean
        Unshift result by filter delay. Defaults to false.

    Returns
    -------
    data : numpy array
        The filtered signal

    """
    b,a = scipy.signal.butter(order, [cutoff_low/(float(fs)/2.0), cutoff_high/(float(fs)/2.0)], btype='band')
    return scipy.signal.lfilter(b,a,data)

def medianlimiter(data, size=11, weight=1):
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
    return data / numpy.abs(data) * numpy.minimum(numpy.abs(data), weight*numpy.median(Transform.slidingwindow(numpy.abs(data), size=size), axis=1))

def localaveragecompensation(data, size=11):
    """
    Compensate local average of a signal.

    To calculate the output signal, a sliding average value is calculated
    for each sample in the signal. This average is then being subtracted
    from the input signal.

    Parameters
    ----------
    data : numpy array
        Input signal.
    size : int
        Size of the sliding window. Defaults to 11.

    Returns
    -------
    data : numpy array
        The filtered signal.

    """
    return data - numpy.average(Transform.slidingwindow(numpy.abs(data), size=size), axis=1)
