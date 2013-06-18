import numpy

def autocorr(x):
	result = numpy.correlate(x, x, mode='full')
	return result[result.size/2:]

def medianlimiter(x, size=10):
	halfsize = numpy.floor(size/2)
	tmp = numpy.hstack(( x[halfsize+1::-1], x, x[:-halfsize-1:-1]))
	for i in range(0, len(x)):
		med = numpy.median(numpy.abs(tmp[i:i+size]))
		x[i] = x[i] / numpy.abs(x[i]) * min(numpy.abs(x[i]), med)
	return x