import sys
sys.path.append('..')

import os
from lib import Play
import scipy, numpy
from pylab import *

def test_play():
    outfs = 44100
    outsig = numpy.random.uniform(0, 1, (2,outfs/2))
    outsig[1,:] = 0
    Play.play(0*outsig, outfs)
