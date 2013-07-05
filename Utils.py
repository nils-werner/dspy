import argparse

def defaultopts(parser):
    parser.add_argument('filename', help='The audio file to be processed')
    parser.add_argument('-n', action="store_false", help="Disable graph output", dest="display")
    parser.add_argument('-d', '--figure', metavar="FILENAME", help="Save figure to file")
    parser.add_argument('-g', '--order', type=int, default=17, metavar="ORDER", help="Set order of median filter, defaults to 17")

    parser.add_argument('-f', '--framelength', type=powof2, default=1024, metavar="SAMPLES", help="Set FFT framelength")
    parser.add_argument('--overlap', type=powof2, default=2, metavar="FRAMELENGTH/X", help="Set relative FFT frame overlap")

    parser.add_argument('-o', '--original', metavar="FILENAME", help="Save original signal to file")
    parser.add_argument('-e', '--harmonic', metavar="FILENAME", help="Save harmonic signal to file")
    parser.add_argument('-p', '--percussive', metavar="FILENAME", help="Save percussive signal to file")

def powof2(arg):
    num = int(arg)
    if(not(num != 0 and ((num & (num - 1)) == 0))):
        raise argparse.ArgumentTypeError("%r is not a power of two" % num)
    return num
