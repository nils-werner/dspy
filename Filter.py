import scipy.signal
import numpy
import Transform

def lowpass(x, cutoff, fs, coeffs=61):
	taps = scipy.signal.firwin(coeffs, cutoff/(float(fs)/2), window='hanning')
	return scipy.signal.lfilter(taps, 1.0, x)

def medianlimiter(x, size=11):
	return numpy.minimum(x, numpy.median(Transform.slidingwindow(x, size=size), axis=1))
