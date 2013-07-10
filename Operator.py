import numpy

def teager(x):
    e = x[1:-1]**2 - x[2:]*x[:-2]
    return numpy.hstack((e[0], e, e[-1]))

def frequency(x):
    return numpy.arccos( 1 - ( teager(x[2:]-x[:-2]) / 2*teager(x[1:-1]) ) ) / 2

def amplitude(x):
    return 2*teager(x[1:-1]) / numpy.sqrt(teager(x[2:]-x[:-2]))
