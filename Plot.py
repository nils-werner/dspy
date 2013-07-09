import scipy
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

class Figure():
    def __init__(self):
        self.fig = plt.figure()

    def img(self, sig, subplot=111, vmin=None, vmax=None):
        ax = self.fig.add_subplot(subplot)
        ax.imshow(scipy.absolute(sig), norm=LogNorm(), vmin=vmin, vmax=vmax, origin='lower', aspect='auto', interpolation='nearest')
        ax.axis('tight')
        ax.set_xlabel('Time')
        ax.set_ylabel('Frequency')
        return ax

    def plot(self, sig, subplot=111):
        ax = self.fig.add_subplot(subplot)
        ax.plot(scipy.absolute(sig))
        ax.axis('tight')
        ax.set_xlabel('Time')
        ax.set_ylabel('Amplitude')
        return ax

    def show(self):
        plt.subplots_adjust(left=0.04, bottom=0.05, right=0.98, top=0.96)
        plt.show()

    def save(self, filename):
        self.fig.set_size_inches(16, 9)
        plt.savefig(filename, bbox_inches='tight', dpi=100)
