from lib import File
from lib import Plot
from lib import Statistic
from lib import Transform
from lib import Window
from lib import Predictor
from lib import Filter
from lib import Utils

import argparse
import scipy

class Framework(object):
    def __init__(self):
        parser = argparse.ArgumentParser(description='Separate mix signal into harmonic and percussive parts.')
        parser.add_argument('filename', help='The audio file to be processed')
        parser.add_argument('-n', action="store_false", help="Disable graph output", dest="display")
        parser.add_argument('-d', '--figure', metavar="FILENAME", help="Save figure to file")

        parser.add_argument('-f', '--framelength', type=Utils.powof2, default=1024, metavar="SAMPLES", help="Set FFT framelength")
        parser.add_argument('--overlap', type=Utils.powof2, default=2, metavar="FRAMELENGTH/X", help="Set relative FFT frame overlap")

        parser.add_argument('-o', '--original', metavar="FILENAME", help="Save original signal to file")
        parser.add_argument('-p', '--prediction', metavar="FILENAME", help="Save predicted signal to file")
        parser.add_argument('-e', '--error', metavar="FILENAME", help="Save error signal to file")

        self.arguments(parser)

        self.args = parser.parse_args()

        fs,x = File.wavread(self.args.filename)

        self.signals = {};
        self.signals['original'] = scipy.zeros_like(x)
        self.signals['prediction'] = scipy.zeros_like(x)
        self.signals['error'] = scipy.zeros_like(x)

        self.process(x, fs)

        if(self.args.prediction != None):
            File.wavwrite(self.args.prediction, fs, signals['prediction'])
        if(self.args.error != None):
            File.wavwrite(self.args.error, fs, signals['error'])
        if(self.args.original != None):
            File.wavwrite(self.args.original, fs, signals['original'])

        if(self.args.display):
            fig = Plot.Figure()

            self.plot(fig)

            if(self.args.figure != None):
                fig.save(self.args.figure)
            else:
                fig.show()

    def arguments(self, parser):
        pass

    def process(self, signal, fs):
        pass

    def plot(self, fig):
        pass