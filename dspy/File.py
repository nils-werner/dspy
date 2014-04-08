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
import sys


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
        rate, data = wav.read(filename)

    try:
        maxv = numpy.finfo(data.dtype).max
    except:
        maxv = numpy.iinfo(data.dtype).max

    return (rate, data.astype('float') / maxv)


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


import types
from scikits.audiolab import Format, Sndfile

class File(object):

    def __init__(self, filename, mode='r', rate=None, channels=None):
        if filename is sys.stdin:
            filename = '-'

        if mode == 'w' and (rate is None or channels is None):
            raise ValueError('You must provide sampling rate and number of channels for writing file.')

        if mode not in ('r','w'):
            raise ValueError('You must provide mode w for writing or r for reading file.')

        if mode == 'r':
            self.f = Sndfile(filename, 'r')

            self.channels = self.f.channels
            self.rate = self.f.samplerate

        else:
            format = Format('wav')
            self.f = Sndfile(filename, 'w', format, channels, rate)

            self.channels = channels
            self.rate = rate

    def write(self, data):
        if isinstance(data, types.GeneratorType):
            for i in data:
                self.f.write_frames(i)

            self.close()

        else:
            self.f.write_frames(data)

    def read(self, framesize=1024):
        while True:
            try:
                yield self.f.read_frames(framesize, dtype=numpy.float32)
            except RuntimeError:
                self.close()
                raise StopIteration

    def close(self):
        self.f.close()
