import argparse
import dummypackage

def cli():
    """Echo a value `N` number of times"""
    parser = argparse.ArgumentParser()
    parser.add_argument('count', type=int, metavar='N')
    args = parser.parse_args()
    for i in range(args.count):
        print(dummypackage.has_legs)
