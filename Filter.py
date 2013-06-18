import scipy.signal

def lowpass(x, cutoff, fs, coeffs=61):
	taps = scipy.signal.firwin(coeffs, cutoff/(float(fs)/2), window='hanning')
	return scipy.signal.lfilter(taps, 1.0, x)
	