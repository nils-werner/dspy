import sys
sys.path.append('..')

from lib import Predictor
from lib import Statistic
import scipy, numpy
from pylab import *

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
    coeffs,pe = Predictor.levinson(corr, 4)
    Predictor.predict(outsig, coeffs)
