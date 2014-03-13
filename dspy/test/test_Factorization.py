import sys
sys.path.append('..')

import numpy
from dspy import Factorization


def test_nmf():
    data = numpy.array([[1.0, 0.0, 2.0], [0.0, 1.0, 1.0]])
    (w, h) = Factorization.nmf(data, iterations=100, num_bases=2)
    assert numpy.allclose(data, numpy.dot(w, h), rtol=1e-01, atol=1e-01)
