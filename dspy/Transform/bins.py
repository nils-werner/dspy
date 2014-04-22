"""
Module to calculate FFT binsizes

"""
import numpy


def extent(framelength, rate, halved=True):
    """
    Calculate a vector containing the frequencies for the bins of an
    fft transform for a certain framelength

    Parameters
    ----------
    framelength : int
        Desired framelength
    rate : int
        Signal sampling rate

    Returns
    -------
    data : numpy array
        The frequencies for each bin of an fft transform

    """
    if(halved):
        return numpy.arange(0, framelength / 2 + 1) * rate / framelength
    else:
        return numpy.hstack(
            (
                numpy.arange(0, framelength / 2 + 1),
                numpy.arange(framelength / 2 + 1, 0, -1)
            )
        ) * rate / framelength


def width(frequency, rate):
    """
    Calculate the framelength required for a certain frequency bin width

    Parameters
    ----------
    frequency : int
        Desired binwidth
    rate : int
        Signal sampling rate

    Returns
    -------
    framelength : int
        The resulting framelength

    """
    return rate / frequency


def number(number):
    """
    Calculate the framelength required for a certain number of frequency bins

    Parameters
    ----------
    number : int
        Desired number of bins

    Returns
    -------
    framelength : int
        The resulting framelength

    """
    return number
