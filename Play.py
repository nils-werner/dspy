"""
Module to play audio signals using portaudio

Functions
---------
`play`: Play a signal.

"""
import pyaudio
import numpy
import contextlib
import sys
import os
from ctypes import *

ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)

def py_error_handler(filename, line, function, err, fmt):
    pass

c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

@contextlib.contextmanager
def noalsaerr():
    """
    A context manager that suppresses ALSA Warnings

    """
    asound = cdll.LoadLibrary('libasound.so')
    asound.snd_lib_error_set_handler(c_error_handler)
    yield
    asound.snd_lib_error_set_handler(None)

def play(sig, rate=44100):
    """
    Play a signal.

    Parameters
    ----------
    sig : numpy array
        Input signal.
    rate : int
        Sampling rate. Defaults to 44100.

    Notes
    -----

     * The Input signal is assumed to be a matrix where each row
       represents one output channel and each column one sample.
     * The input signal is assumed to be normalized between -1 and 1.

    """
    with noalsaerr():
        p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=sig.shape[0], rate=rate, output=1)
    stream.write(numpy.reshape(sig.T, (1,-1)).astype(numpy.float32).tostring())
    stream.close()
    p.terminate()