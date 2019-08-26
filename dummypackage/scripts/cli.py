import argparse


def do_something(word):
    return word.upper()

def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("echo")
    args = parser.parse_args()
    print(
        do_something(args.echo)
    )
