"""
Module to read / write wav files using numpy arrays

Functions
---------
`wavread`: Return the sample rate (in samples/sec) and data from a WAV file.

`wavwrite`: Write a numpy array as a WAV file.

"""
import scipy.io.wavfile as wav
import numpy
import warnings

def wavread(filename):
    """
    Return the sample rate (in samples/sec) and data from a WAV file

    Parameters
    ----------
    filename : string
        Input wav file.

    Returns
    -------
    rate : int
        Sample rate of wav file
    data : numpy array
        Data read from wav file

    Notes
    -----

    * The returned sample rate is a Python integer
    * The data is returned as a numpy array of
      floats, normalized between -1 and 1.

    """
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        rate,data = wav.read(filename)
    maxv = numpy.iinfo(data.dtype).max
    return (rate,data.astype('float') / maxv)

def wavwrite(filename, rate, data):
    """
    Return the sample rate (in samples/sec) and data from a WAV file

    Parameters
    ----------
    filename : string
        Input wav file.
    rate : int
        Sample rate.
    data : numpy array
        Signal

    Notes
    -----

    * The data is assumed to be a numpy array of
      floats, normalized between -1 and 1.

    """
    maxv = numpy.iinfo(numpy.int16).max
    wav.write(filename, rate, (data * maxv).astype('int16'))
