"""
Module for several utility methods

Functions
---------
`defaultopts`: Attaches regularily used command line options to an ArgParser instance

`powof2`: Checks if a number is a power of two

"""
import argparse

def defaultopts(parser):
    """
    Attach regularily used command line options to an ArgParser instance

    Parameters
    ----------
    parser : ArgParser instance
        The ArgParser instance to add the arguments to

    """
    parser.add_argument('filename', help='The audio file to be processed')
    parser.add_argument('-n', action="store_false", help="Disable graph output", dest="display")
    parser.add_argument('-d', '--figure', metavar="FILENAME", help="Save figure to file")
    parser.add_argument('-g', '--order', type=int, default=17, metavar="ORDER", help="Set order of median filter, defaults to 17")

    parser.add_argument('-f', '--framelength', type=powof2, default=1024, metavar="SAMPLES", help="Set FFT framelength")
    parser.add_argument('--overlap', type=powof2, default=2, metavar="FRAMELENGTH/X", help="Set relative FFT frame overlap")


def powof2(num):
    """
    Check if a number is a power of two

    Parameters
    ----------
    num : int
        The number to be checked

    Returns
    -------
    num : int
        The number to be checked

    Notes
    -----

     * Raises an argparse.ArgumentTypeError when the number is not a power of two.

    """
    num = int(num)
    if(not(num != 0 and ((num & (num - 1)) == 0))):
        raise argparse.ArgumentTypeError("%r is not a power of two" % num)
    return num
