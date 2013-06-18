import scipy.io.wavfile as wav
import numpy
import warnings

def wavread(filename):
	with warnings.catch_warnings():
		warnings.simplefilter("ignore")
		fs,x = wav.read(filename)
	x = x.astype('float')
	maxv = numpy.max(numpy.abs(x),axis=0);
	x = x / maxv * 2
	x -= 1;
	return (fs,x,maxv)

def wavwrite(filename, fs, x, maxv=1):
	x /= numpy.max(numpy.abs(x),axis=0);
	x += 1;
	x *= maxv / 2;
	x = x.astype('int16')
	wav.write(filename, fs, x)