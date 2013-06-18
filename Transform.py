import Window
import scipy, numpy

def stft(x, windowed=True, halved=True):
	if(windowed):
		result = scipy.fft(Window.window(x))
	else:
		result = scipy.fft(x)
	if(halved):
		result = result[0:result.size/2+1]
	return result

def istft(x, windowed=True, halved=True):
	if(halved):
		x = numpy.hstack((x, x[-2:0:-1].conjugate()))
	if(windowed):
		return scipy.real(scipy.ifft(Window.window(x)))
	else:
		return scipy.real(scipy.ifft(x))