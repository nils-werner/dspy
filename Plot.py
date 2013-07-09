import scipy
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

class Figure():
    def __init__(self):
        self.fig = plt.figure()

    def img(self, sig, subplot=111, **kwargs):
        kwargs.setdefault('vmin', 0.0001)
        kwargs.setdefault('vmax', len(sig))
        kwargs.setdefault('norm', LogNorm())
        kwargs.setdefault('origin', 'lower')
        kwargs.setdefault('aspect', 'auto')
        kwargs.setdefault('interpolation', 'nearest')

        ax = self.fig.add_subplot(subplot)
        ax.imshow(scipy.absolute(sig), **kwargs)
        ax.axis('tight')
        ax.set_xlabel('Time')
        ax.set_ylabel('Frequency')
        return ax

    def plot(self, sig, subplot=111, **kwargs):
        ax = self.fig.add_subplot(subplot)
        ax.plot(scipy.absolute(sig), **kwargs)
        ax.axis('tight')
        ax.set_xlabel('Time')
        ax.set_ylabel('Amplitude')
        return ax

    def show(self, **kwargs):
        kwargs.setdefault('left', 0.04)
        kwargs.setdefault('bottom', 0.05)
        kwargs.setdefault('right', 0.98)
        kwargs.setdefault('top', 0.96)

        plt.subplots_adjust(**kwargs)
        plt.show()

    def save(self, filename, **kwargs):
        kwargs.setdefault('bbox_inches', 'tight')
        kwargs.setdefault('dpi', 100)

        self.fig.set_size_inches(16, 9)
        plt.savefig(filename, **kwargs)
