"""
Module to transform signals

Functions
---------
`stft`: Calculate the short time fourier transform of a signal chunk

`istft`: Calculate the inverse short time fourier transform of a spectrogram line

`spectrogram`: Calculate the complete spectrogram of a signal

`ispectrogram`: Calculate the signal of a complete spectrogram

"""
import Window
import scipy, numpy

def bin_extent(data, rate, halved=True):
    if(halved):
        return numpy.arange(0,data.size/2+1) * rate/data.size
    else:
        return numpy.hstack((numpy.arange(0,data.size/2+1), numpy.arange(data.size/2+1,0,-1))) * rate/data.size

def bin_frequency(frequency, rate):
    return float(rate)/float(frequency)

def bin_number(number, rate):
    return bin_frequency((rate//2)/number, rate)

def stft(data, windowed=True, halved=True):
    """
    Calculate the short time fourier transform of a signal

    Parameters
    ----------
    data : numpy array
        The signal to be calculated.
    windowed : boolean
        Switch for turning on signal windowing. Defaults to True.
    halved : boolean
        Switch for turning on signal truncation. By default,
        the fourier transform returns a symmetrically mirrored
        spectrum. This additional data is not needed and can be
        removed. Defaults to True.

    Returns
    -------
    data : numpy array
        The spectrum

    """
    if(windowed):
        result = scipy.fft(Window.window(data))
    else:
        result = scipy.fft(data)
    if(halved):
        result = result[0:result.size/2+1]
    return result

def istft(data, windowed=True, halved=True):
    """
    Calculate the inverse short time fourier transform of a spectrum

    Parameters
    ----------
    data : numpy array
        The spectrum to be calculated.
    windowed : boolean
        Switch for turning on signal windowing. Defaults to True.
    halved : boolean
        Switch for turning on signal truncation. By default,
        the inverse fourier transform consumes a symmetrically
        mirrored spectrum. This additional data is not needed
        and can be removed. Defaults to True.

    Returns
    -------
    data : numpy array
        The signal

    """
    if(halved):
        data = numpy.hstack((data, data[-2:0:-1].conjugate()))
    if(windowed):
        return scipy.real(Window.window(scipy.ifft(data)))
    else:
        return scipy.real(scipy.ifft(data))


def spectrogram(data, framelength=1024, overlap=2, **kwargs):
    """
    Calculate the spectrogram of a signal

    Parameters
    ----------
    data : numpy array
        The signal to be calculated.
    framelength : int
        The signal frame length. Defaults to 1024.
    overlap : int
        The signal frame overlap coefficient. Value x means
        1/x overlap. Defaults to 2.
    windowed : boolean
        Switch for turning on signal windowing. Defaults to True.
    halved : boolean
        Switch for turning on signal truncation. By default,
        the fourier transform returns a symmetrically mirrored
        spectrum. This additional data is not needed and can be
        removed. Defaults to True.

    Returns
    -------
    data : numpy array
        The spectrogram

    """
    values = list(enumerate(range(0, len(data)-framelength, framelength//overlap)))
    for j,i in values:
        sig = stft(data[i:i+framelength], **kwargs) / (overlap//2)

        if(i == 0):
            output = numpy.zeros((len(values), sig.shape[0]), dtype=sig.dtype)

        output[j,:] = sig

    return output

def ispectrogram(data, framelength=1024, overlap=2, **kwargs):
    """
    Calculate the inverse spectrogram of a signal

    Parameters
    ----------
    data : numpy array
        The spectrogram to be calculated.
    framelength : int
        The signal frame length. Defaults to 1024.
    overlap : int
        The signal frame overlap coefficient. Value x means
        1/x overlap. Defaults to 2.
    windowed : boolean
        Switch for turning on signal windowing. Defaults to True.
    halved : boolean
        Switch for turning on signal truncation. By default,
        the fourier transform returns a symmetrically mirrored
        spectrum. This additional data is not needed and can be
        removed. Defaults to True.

    Returns
    -------
    data : numpy array
        The signal

    """
    i = 0
    values = range(0, data.shape[0])
    for j in values:
        sig = istft(data[j,:], **kwargs)

        if(i == 0):
            output = numpy.zeros(framelength + (len(values) - 1) * framelength//overlap, dtype=sig.dtype)

        output[i:i+framelength] += sig

        i += framelength//overlap

    return output


def slidingwindow(data, size=11, padded=True):
    """
    Calculate a sliding window over a signal

    Parameters
    ----------
    data : numpy array
        The spectrogram to be calculated.
    size : int
        The sliding window size
    padding : boolear
        Switch for turning on signal padding by mirroring 
        on either side. Defaults to True.

    Returns
    -------
    data : numpy array
        A matrix where each line consists of one instance
        of the sliding window.

    Notes
    -----

    a = numpy.array([1, 2, 3, 4])
    slidingwindow(a, size=3)
    >>> numpy.array([1, 1, 2],
                    [1, 2, 3],
                    [2, 3, 4],
                    [3, 4, 4])

    """
    if(size%2 == 0):
        size += 1
    halfsize = numpy.floor(size/2)
    if(padded == True):
        tmp = numpy.hstack(( data[halfsize-1::-1], data, data[:-halfsize-1:-1]))
    else:
        tmp = data

    strides = (tmp.itemsize, tmp.itemsize)
    shape = (1 + (tmp.nbytes - size*tmp.itemsize)/strides[0], size)

    return numpy.lib.stride_tricks.as_strided(tmp, shape=shape, strides=strides)
