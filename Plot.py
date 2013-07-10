"""
Module to display plots and images using matplotlib.

Functions
---------
`Figure`: Create a new figure instance.

`img`: Plot a 2D image.

`plot`: Plot a 1D lineplot

`show`: Show the figure.

`save`: Save the figure to file.

"""
import scipy
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

class Figure():
    def __init__(self):
        """
        Create a new Figure instance.

        Returns
        -------
        figure : Figure
            A new figure.

        """
        self.fig = plt.figure()

    def img(self, sig, subplot=111, **kwargs):
        """
        Create a new subplot and draw a 2D image in it.

        Parameters
        ----------
        sig : numpy array
            The data to plot.
        subplot : int
            The coordinates of the subplot

        vmin : float
            The minimum value. Defaults to 0.0001.
        vmax : float
            The maximum value. Defaults to len(sig).
        norm : method
            The normalization function. Defaults to `matplotlib.colors.LogNorm()`.
        origin : string
            The origin of the plot. Defaults to 'lower'.
        aspect : string
            The aspect ratio of the plot. Defaults to 'auto'.
        interpolation : string
            The interpolation method. Defaults to 'nearest'.

        ... : mixed
            All other named arguments accepted
            by `matplotlib.imshow()`.

        Returns
        -------
        subplot : subplot instance
            The newly created subplot, for further manipulation.

        Notes
        -----

        * Only absolute values are plotted.

        """
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
        """
        Create a new subplot and draw a 1D plot in it.

        Parameters
        ----------
        sig : numpy array
            The data to plot.
        subplot : int
            The coordinates of the subplot.

        ... : mixed
            All other named arguments accepted
            by `matplotlib.imshow()`.

        Returns
        -------
        subplot : subplot instance
            The newly created subplot, for further manipulation.

        Notes
        -----

        * Only absolute values are plotted

        """
        ax = self.fig.add_subplot(subplot)
        ax.plot(scipy.real(sig), **kwargs)
        ax.axis('tight')
        ax.set_xlabel('Time')
        ax.set_ylabel('Amplitude')
        return ax

    def show(self, **kwargs):
        """
        Show the figure instance.

        Parameters
        ----------
        ... : mixed
            All other named arguments accepted
            by `matplotlib.show()`.

        """
        kwargs.setdefault('left', 0.04)
        kwargs.setdefault('bottom', 0.05)
        kwargs.setdefault('right', 0.98)
        kwargs.setdefault('top', 0.96)

        plt.subplots_adjust(**kwargs)
        plt.show()

    def save(self, filename, **kwargs):
        """
        Save the figure instance to file.

        Parameters
        ----------
        filename : string
            Output image file.

        ... : mixed
            All other named arguments accepted
            by `matplotlib.savefig()`.

        """
        kwargs.setdefault('bbox_inches', 'tight')
        kwargs.setdefault('dpi', 100)

        self.fig.set_size_inches(16, 9)
        plt.savefig(filename, **kwargs)
