import scipy, numpy

def extent(data, rate, halved=True):
    if(halved):
        return numpy.arange(0,data.size/2+1) * rate/data.size
    else:
        return numpy.hstack((numpy.arange(0,data.size/2+1), numpy.arange(data.size/2+1,0,-1))) * rate/data.size

def frequency(frequency, rate):
    return float(rate)/float(frequency)

def number(number, rate):
    return bin_frequency((rate//2)/number, rate)