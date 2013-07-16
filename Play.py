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
    asound = cdll.LoadLibrary('libasound.so')
    asound.snd_lib_error_set_handler(c_error_handler)
    yield
    asound.snd_lib_error_set_handler(None)

def play(sig, rate=44100):
    with noalsaerr():
        p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=sig.shape[0], rate=44100, output=1)
    stream.write(numpy.reshape(sig.T, (1,-1)).astype(numpy.float32).tostring())
    stream.close()
    p.terminate()
