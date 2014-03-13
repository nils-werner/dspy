import sys
sys.path.append('..')

from dspy import Play
import numpy


def test_play():
    outfs = 44100
    outsig = numpy.random.uniform(0, 1, (2, outfs / 2))
    outsig[1, :] = 0
    Play.play(0 * outsig, outfs)
