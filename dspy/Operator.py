"""
General purpose operations such as RMS, db, SNR, teager etc.

"""
import numpy


def delay(data, delay):
    """
    Shift a signal as written in mathematical notation.

    Parameters
    ----------
    data : numpy array
        The signal
    delay : int
        The delay to be applied.

    Returns
    -------
    data : numpy array
        The delayed signal

    Notes
    -----

    Math formulation examples:

     - x(k+1) equates to Operator.delay(x, 1)
     - x(k-1) equates to Operator.delay(x, -1)

    The output signal is padded to be of same shape as input signal.

    """
    if delay == 0:
        return data
    elif delay > 0:
        return numpy.lib.pad(data, (0, delay), 'edge')[delay:]
    else:
        return numpy.lib.pad(data, (-delay, 0), 'edge')[:delay]


def teager(x):
    """
    Calculate the Teager operator of a signal.

    Parameters
    ----------
    data : numpy array
        The signal

    Returns
    -------
    data : numpy array
        The teager operator signal

    Notes
    -----

    Output data is padded to be of same shape as input data

    """
    if numpy.iscomplex(x).any():
        e = teager(numpy.real(x)) + teager(numpy.imag(x))
    else:
        e = x[1:-1] ** 2 - x[2:] * x[:-2]
    return numpy.hstack((e[0], e, e[-1]))


def rms(x, axis=None):
    """
    Calculate root mean square of signal

    Parameters
    ----------
    data : numpy array
        The signal

    Returns
    -------
    data : float
        The RMS value

    """
    return numpy.sqrt(numpy.mean(x ** 2, axis=axis))


def snr(signal, noise):
    """
    Calculate the Signal to Noise ratio of two signals

    Parameters
    ----------
    signal : numpy array
        The signal
    noise : numpy array
        The noise

    Returns
    -------
    data : float
        The SNR value in dB

    """
    return db(rms(signal) / rms(noise), energy=True)


def db(x, energy=False):
    """
    Calculate the dB value of a ratio

    Parameters
    ----------
    x : float
        The ratio to be transformed
    energy : boolean
        Treat input value as measurement of energy

    Returns
    -------
    x : float
        The dB value corresponding to the given ratio

    """
    if energy is False:
        return 10.0 * numpy.log10(x)
    else:
        return 20.0 * numpy.log10(x)


def idb(x, energy=False):
    """
    Calculate the original ratio of a dB value

    Parameters
    ----------
    x : float
        The dB value to be transformed
    energy : boolean
        Treat input value as measurement of energy

    Returns
    -------
    x : float
        The ratio corresponding to the given dB value

    """
    if energy is False:
        return 10.0 ** (x / 10.0)
    else:
        return 10.0 ** (x / 20.0)
