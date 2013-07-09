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



def spectrogram(x, framelength=1024, overlap=2, **kwargs):

    values = list(enumerate(range(0, len(x)-framelength, framelength//overlap)))
    for j,i in values:
        sig = stft(x[i:i+framelength], **kwargs) / (overlap//2)

        if(i == 0):
            output = numpy.zeros((len(values), sig.shape[0]), dtype=sig.dtype)

        output[j,:] = sig

    return output

def ispectrogram(x, framelength=1024, overlap=2, **kwargs):

    i = 0
    values = range(0, x.shape[0])
    for j in values:
        sig = istft(x[j,:], **kwargs)

        if(i == 0):
            output = numpy.zeros(framelength + (len(values) - 1) * framelength//overlap, dtype=sig.dtype)

        output[i:i+framelength] += sig

        i += framelength//overlap

    return output



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
