import sys
sys.path.append('..')

from dspy import Transform
from dspy.Transform import bins
from dspy import File
import scipy, numpy
from pylab import *


def fft_identity(framelength, overlap, padding):
    fs,original = File.wavread('dspy/test/v.wav')

    padlength = (len(original)%framelength) * overlap * 2
    original = numpy.hstack((numpy.zeros((padlength//2,)), original, numpy.zeros((padlength//2,))))

    output = scipy.zeros_like(original)

    values = range(0, len(original)-framelength, framelength//overlap)
    for i in values:
        spectrum = Transform.stft(original[i:i+framelength], padding=padding) / (overlap//2)
        output[i:i+framelength] += Transform.istft(spectrum, padding=padding)

    assert(len(original) - len(output) < framelength)
    print(numpy.max(original - output))
    assert numpy.allclose(original[padlength//2:-padlength//2], output[padlength//2:-padlength//2], rtol=1e-03, atol=1e-03)


def spectrogram_identity(framelength, overlap, padding):
    fs,original = File.wavread('dspy/test/v.wav')

    padlength = (len(original)%framelength) * overlap * 2
    original = numpy.hstack((numpy.zeros((padlength//2,)), original, numpy.zeros((padlength//2,))))

    output = Transform.ispectrogram(
            Transform.spectrogram(original, framelength=framelength, overlap=overlap, padding=padding),
        framelength=framelength, overlap=overlap, padding=padding)

    assert(len(original) - len(output) < framelength)

    original = numpy.resize(original, output.shape)
    print(numpy.max(original - output))
    assert numpy.allclose(original[padlength//2:-padlength//2], output[padlength//2:-padlength//2], rtol=1e-03, atol=1e-03)

def test_logspace_identity():
    fs,original = File.wavread('dspy/test/v.wav')

    linspec = Transform.spectrogram(original)
    logspec = Transform.logscale(linspec)
    result = Transform.expscale(logspec)

def test_fft_identity():
    for i in [512, 1024, 2048]:
        for j in [2, 4, 8]:
            for k in [0, 1, 2]:
                yield fft_identity, i, j, k

def test_spectrogram_identity():
    for i in [512, 1024, 2048]:
        for j in [2, 4, 8]:
            for k in [0, 1, 2]:
                yield spectrogram_identity, i, j, k


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