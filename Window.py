import numpy

def halfsin(M):
    return numpy.sin(numpy.pi / M * (numpy.arange(0, M) + .5))

def window(sig):
    return sig * halfsin(len(sig))
