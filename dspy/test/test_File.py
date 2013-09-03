import sys
sys.path.append('..')

import tempfile
import os
from dspy import File
import scipy, numpy
from pylab import *

def test_wavread_range():
    fs,original = File.wavread('dspy/test/v.wav')

    assert 0 < original.max() <= 1
    assert -1 <= original.min() < 0
    assert -0.001 < numpy.average(original) < 0.001

def test_wavwrite_read():
    outfs = 44100
    outsig = numpy.random.uniform(0, 1, 1024)
    try:
        fd, tmpfile = tempfile.mkstemp(suffix='.wav')
        os.close(fd)
        File.wavwrite(tmpfile, outfs, outsig)
        assert os.path.exists(tmpfile)
        infs,insig = File.wavread(tmpfile)
    finally:
        os.remove(tmpfile)

    assert outfs == infs
    assert numpy.allclose(outsig, insig, rtol=1e-04, atol=1e-04)
