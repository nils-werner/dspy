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
        return scipy.real(Window.window(scipy.ifft(x)))
    else:
        return scipy.real(scipy.ifft(x))

def slidingwindow(x, size=11, padded=True):
    if(size%2 == 0):
        size += 1
    halfsize = numpy.floor(size/2)
    if(padded == True):
        tmp = numpy.hstack(( x[halfsize-1::-1], x, x[:-halfsize-1:-1]))
    else:
        tmp = x

    strides = (tmp.itemsize, tmp.itemsize)
    shape = (1 + (tmp.nbytes - size*tmp.itemsize)/strides[0], size)

    return numpy.lib.stride_tricks.as_strided(tmp, shape=shape, strides=strides)
