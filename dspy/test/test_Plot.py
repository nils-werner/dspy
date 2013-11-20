import sys
sys.path.append('..')

from dspy import Plot
import scipy, numpy
from pylab import *

def test_plot():
    fig = Plot.Figure()

    subfigure = fig.plot(numpy.random.uniform(0, 1, 1024), 211)
    subfigure.set_title('Random number')

    subfigure = fig.plot(numpy.random.uniform(0, 1, 1024), 212)
    subfigure.set_title('Residual Energy')
    subfigure.set_ylabel('Energy Quotient')

def test_img():
    fig = Plot.Figure()

    subfigure = fig.img(numpy.random.uniform(0, 1, (1024, 1024)), 211, vmin=0.0001, vmax=1024)
    subfigure.set_title('Spectrum')

    subfigure = fig.img(numpy.random.uniform(0, 1, (1024, 1024)) + 1j*numpy.random.uniform(0, 1, (1024, 1024)), 212)
    subfigure.set_title('Autocorrelation')