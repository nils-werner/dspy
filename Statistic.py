import numpy

def autocorr(x):
	result = numpy.correlate(x, x, mode='full')
	return result[result.size/2:]

def medianlimiter(x, size=11):
	if(size%2 == 0):
		size += 1
	halfsize = numpy.floor(size/2)
	tmp = numpy.hstack(( x[halfsize-1::-1], x, x[:-halfsize-1:-1]))

	strides = (tmp.itemsize, tmp.itemsize)
	shape = (1 + (tmp.nbytes - size*tmp.itemsize)/strides[0], size)

	return numpy.minimum(x, numpy.median(numpy.lib.stride_tricks.as_strided(tmp, shape=shape, strides=strides), axis=1))

def quadraticdiff(a, b):
	return numpy.sum((a - b)**2)
