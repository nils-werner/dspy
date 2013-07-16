import sys
sys.path.append('..')

import os
from lib import File
import scipy, numpy
from pylab import *

def test_wavread_range():
    fs,original = File.wavread('../wav/cv.wav')

    assert 0 < original.max() <= 1
    assert -1 <= original.min() < 0
    assert -0.001 < numpy.average(original) < 0.001

def test_wavwrite_read():
    outfs = 44100
    outsig = numpy.random.uniform(0, 1, 1024)
    File.wavwrite('./test.wav', outfs, outsig)
    infs,insig = File.wavread('./test.wav')
    os.remove('./test.wav')

    assert outfs == infs
    assert numpy.allclose(outsig, insig, rtol=1e-04, atol=1e-04)
