import sys
sys.path.append('..')

import os
from dspy import Filter
import scipy, numpy
from pylab import *

def test_medianlimiter():
    original = numpy.array([ 3, 4, 1+1j, 1, 8, 7, 1, 2, 6, 1, 1])
    output   = numpy.array([ 3, 3, 1+1j, 1, 7, 7, 1, 2, 2, 1,1])

    filtered = Filter.medianlimiter(output, 3)

    assert numpy.array_equal(output, filtered)


def test_lowpass():
    outsig = numpy.random.uniform(0, 1, 1024)
    Filter.lowpass(outsig, 100, 44100)
