import numpy

def autocorr(x):
    result = numpy.correlate(x, x, mode='full')
    return result[result.size/2:]

def quadraticdiff(a, b):
    return numpy.sum((a - b)**2)
