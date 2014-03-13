from __future__ import absolute_import

from .. import Predictor
from .. import Statistic
import scipy
import numpy
import scipy.signal


def test_levinson():
    outsig = numpy.random.uniform(0, 1, 1024)
    corr = Statistic.autocorr(outsig)
    Predictor.levinson(corr, 4)


def test_burg():
    outsig = numpy.random.uniform(0, 1, 1024)
    corr = Statistic.autocorr(outsig)
    Predictor.levinson(corr, 4)


def test_prediction():
    outsig = numpy.random.uniform(0, 1, 1024)
    corr = Statistic.autocorr(outsig)
    coeffs, pe = Predictor.levinson(corr, 4)
    Predictor.predict(outsig, coeffs)


def test_rls():
    s = 50000
    x = numpy.random.randn(s)
    b = scipy.signal.firwin(32, 0.5)
    n = 0.1 * numpy.random.randn(s)
    d = scipy.signal.lfilter(b, 1, x) + n
    lam = 0.99
    w, e, y = Predictor.rls(x, d, 32, lam)
    assert numpy.allclose(b, w, rtol=1e-01, atol=1e-01)
