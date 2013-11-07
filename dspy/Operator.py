import numpy

def teager(x):
    if numpy.iscomplex(x).any():
        e = teager(numpy.real(x)) + teager(numpy.imag(x))
    else:
        e = x[1:-1]**2 - x[2:]*x[:-2]
    return numpy.hstack((e[0], e, e[-1]))
