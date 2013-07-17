import sys
sys.path.append('..')

from lib import Transform
from lib.Transform import bins
from lib import File
import scipy, numpy
from pylab import *


def fft_identity(framelength, overlap):
    print(framelength, overlap)
    fs,original = File.wavread('../wav/cv.wav')

    padlength = (len(original)%framelength) * overlap * 2
    original = numpy.hstack((numpy.zeros((padlength//2,)), original, numpy.zeros((padlength//2,))))

    output = scipy.zeros_like(original)

    values = range(0, len(original)-framelength, framelength//overlap)
    for i in values:
        spectrum = Transform.stft(original[i:i+framelength]) / (overlap//2)
        output[i:i+framelength] += Transform.istft(spectrum)

    assert(len(original) - len(output) < framelength)
    print(numpy.max(original - output))
    assert numpy.allclose(original[padlength//2:-padlength//2], output[padlength//2:-padlength//2], rtol=1e-03, atol=1e-03)


def spectrogram_identity(framelength, overlap):
    print(framelength, overlap)
    fs,original = File.wavread('../wav/cv.wav')

    padlength = (len(original)%framelength) * overlap * 2
    original = numpy.hstack((numpy.zeros((padlength//2,)), original, numpy.zeros((padlength//2,))))

    output = Transform.ispectrogram(Transform.spectrogram(original, framelength=framelength, overlap=overlap), framelength=framelength, overlap=overlap)

    assert(len(original) - len(output) < framelength)

    original = numpy.resize(original, output.shape)
    print(numpy.max(original - output))
    assert numpy.allclose(original[padlength//2:-padlength//2], output[padlength//2:-padlength//2], rtol=1e-03, atol=1e-03)

def test_fft_identity():
    for i in [512, 1024, 2048]:
        for j in [2, 4, 8]:
            yield fft_identity, i, j

def test_spectrogram_identity():
    for i in [512, 1024, 2048]:
        for j in [2, 4, 8]:
            yield spectrogram_identity, i, j


def test_slidingwindow():
    outsig = numpy.random.uniform(0, 1, 1024)
    Transform.slidingwindow(outsig)


def test_bins_extent():
    fs = 44100
    output = Transform.bins.extent(4410000, fs)

    assert(output[0] == 0)
    assert(output[-1] == fs/2)

def test_bins_extent_short():
    fs = 44100
    output = Transform.bins.extent(256, fs)

    assert(output[0] == 0)
    assert(output[-1] == fs/2)

def test_bins_number():
    assert Transform.bins.number(10) == 10

def test_bins_width():
    assert Transform.bins.width(10, 44100) == 4410
    assert Transform.bins.width(100, 48000) == 480