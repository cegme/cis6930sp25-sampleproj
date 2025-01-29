

import argparse
import json
import sys


def main(url):
    print(f"{url=}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--url", type=str, help="some URL")

    args = parser.parse_args()

    if args.url:
        main(url=args.url)
    else:
        parser.print_help(sys.stderr)
