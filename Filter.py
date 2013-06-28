import scipy.signal
import numpy
import Transform

def lowpass(x, cutoff, fs, coeffs=61):
    taps = scipy.signal.firwin(coeffs, cutoff/(float(fs)/2), window='hanning')
    return scipy.signal.lfilter(taps, 1.0, x)

def medianlimiter(x, size=11, weight=1):
    return x / numpy.abs(x) * numpy.minimum(numpy.abs(x), weight*numpy.median(Transform.slidingwindow(numpy.abs(x), size=size), axis=1))
