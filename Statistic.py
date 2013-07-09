import numpy

def autocorr(x, **kwargs):
    kwargs.setdefault('mode', 'full')

    result = numpy.correlate(x, x, **kwargs)
    return result[result.size/2:]

def quadraticdiff(a, b):
    return numpy.sum((a - b)**2)
