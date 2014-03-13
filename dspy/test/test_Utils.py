from __future__ import absolute_import

from .. import Utils
import argparse


def test_defaultopts():
    argv = ['-n', 'filename.wav']
    parser = argparse.ArgumentParser()
    Utils.defaultopts(parser)
    args = parser.parse_args(argv)


def test_powof2():
    assert Utils.powof2(16)
    try:
        Utils.powof2(17)
        assert False
    except:
        assert True
