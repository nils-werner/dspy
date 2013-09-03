import sys
sys.path.append('..')

from lib import Window
import scipy, numpy
from pylab import *

def test_halfsin():
    a = Window.halfsin(11)

    assert a[5] == a.max()
    assert a[0] == a.min() or a[-1] == a.min()
    assert numpy.allclose(a[0], a[-1])

    b = Window.halfsin(10)

    assert b[4] == b.max() or b[5] == b.max()
    assert numpy.allclose(b[4], b[5])
    assert b[0] == b.min() or b[-1] == b.min()
    assert numpy.allclose(b[0], b[-1])

def test_window():
    b = Window.window(numpy.ones((10)))

    assert b[4] == b.max() or b[5] == b.max()
    assert numpy.allclose(b[4], b[5])
    assert b[0] == b.min() or b[-1] == b.min()
    assert numpy.allclose(b[0], b[-1])
