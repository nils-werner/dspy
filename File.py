import scipy.io.wavfile as wav
import numpy
import warnings

def wavread(filename):
	with warnings.catch_warnings():
		warnings.simplefilter("ignore")
		fs,x = wav.read(filename)
	maxv = numpy.iinfo(x.dtype).max
	x = x.astype('float')
	x = x / maxv * 2
	x -= 1;
	return (fs,x)

def wavwrite(filename, fs, x):
	maxv = numpy.iinfo(numpy.int16).max
	x /= numpy.max(numpy.abs(x),axis=0);
	x += 1;
	x *= maxv / 2;
	x = x.astype('int16')
	wav.write(filename, fs, x)