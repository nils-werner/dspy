import sys
sys.path.append('..')

from dspy import Operator
import numpy


def tests_teager():
    original = numpy.arange(10)
    energy = Operator.teager(original)

    assert original.shape == energy.shape
    assert numpy.allclose(energy, numpy.ones(10))
