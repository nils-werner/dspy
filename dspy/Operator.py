import numpy

def teager(x):
    if numpy.iscomplex(x).any():
        e = teager(numpy.real(x)) + teager(numpy.imag(x))
    else:
        e = x[1:-1]**2 - x[2:]*x[:-2]
    return numpy.hstack((e[0], e, e[-1]))

def rms(x, axis=None):
    return numpy.sqrt(numpy.mean(x**2, axis=axis))

def db(x, energy=False):
    if energy is False:
        return 10.0*numpy.log10(x)
    else:
        return 20.0*numpy.log10(x)

def idb(x, energy=False):
    if energy is False:
        return 10.0 ** (x / 10.0)
    else:
        return 10.0 ** (x / 20.0)
