import sys
sys.path.append('..')

import os
from dspy import Operator
import scipy, numpy
from pylab import *

def tests_teager():
    original = numpy.arange(10)
    energy = Operator.teager(original)

    assert original.shape == energy.shape
    assert numpy.allclose(energy, numpy.ones(10))
