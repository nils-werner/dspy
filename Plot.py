import scipy
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

def figure():
	return plt.figure()

def img(sig, fig, subplot=None, vmin=None, vmax=None):
	if(subplot != None):
		ax = fig.add_subplot(subplot)
	else:
		ax = fig
	ax.imshow(scipy.absolute(sig), norm=LogNorm(), vmin=vmin, vmax=vmax, origin='lower', aspect='auto', interpolation='nearest')
	ax.set_xlabel('Time')
	ax.set_ylabel('Frequency')
	return ax

def plot(sig, fig, subplot=None):
	if(subplot != None):
		ax = fig.add_subplot(subplot)
	else:
		ax = fig
	ax.plot(scipy.absolute(sig))
	ax.set_xlabel('Time')
	ax.set_ylabel('Amplitude')
	return ax

def show():
	plt.subplots_adjust(left=0.04, bottom=0.05, right=0.98, top=0.96)
	plt.show()

def save(filename):
	plt.savefig(filename, bbox_inches=0)
