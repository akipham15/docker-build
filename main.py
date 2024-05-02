#!/usr/bin/env python3
import sys
from logzero import logger

if len(sys.argv) > 1:
    arg = sys.argv[1]
    logger.info("This is a simple helloworld! Hello {}".format(arg))
else:
    arg = None
    logger.info("This is a simple helloworld! You did not pass an arg")


def main():
    with open("helloxxx.txt", "w") as f:
        f.write(f"Hello World, {arg}!\n")

if __name__ == "__main__":
    main()
