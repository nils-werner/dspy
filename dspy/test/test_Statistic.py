from __future__ import absolute_import

from .. import Statistic
import numpy


def test_quadraticdiff():
    diff = Statistic.quadraticdiff(
        numpy.array([0, 0, -2, 3, 0]), numpy.array([0, 0, 0, 1, 0])
    )

    assert diff == 8


def test_autocorr():
    outsig = numpy.random.uniform(0, 1, 1024)
    Statistic.autocorr(outsig)
