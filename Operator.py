import numpy

def teager(x):
    e = x[1:-1]**2 - x[2:]*x[:-2]
    return numpy.hstack((e[0], e, e[-1]))
