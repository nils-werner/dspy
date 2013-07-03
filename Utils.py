import argparse

def powof2(arg):
    num = int(arg)
    if(not(num != 0 and ((num & (num - 1)) == 0))):
        raise argparse.ArgumentTypeError("%r is not a power of two" % num)
    return value
