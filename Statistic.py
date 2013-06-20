import numpy
import Transform

def autocorr(x):
	result = numpy.correlate(x, x, mode='full')
	return result[result.size/2:]

def medianlimiter(x, size=11):
	return numpy.minimum(x, numpy.median(Transform.slidingwindow(x, size=size), axis=1))

def quadraticdiff(a, b):
	return numpy.sum((a - b)**2)
