import scipy.io.wavfile as wav
import numpy
import warnings

def wavread(filename):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        fs,x = wav.read(filename)
    maxv = numpy.iinfo(x.dtype).max
    return (fs,x.astype('float') / maxv)

def wavwrite(filename, fs, x):
    maxv = numpy.iinfo(numpy.int16).max
    wav.write(filename, fs, (x * maxv).astype('int16'))
