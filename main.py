#!/usr/bin/env python3
import sys
from logzero import logger
import os

if len(sys.argv) > 1:
    arg = sys.argv[1]
    logger.info("This is a simple helloworld! Hello {}".format(arg))
else:
    arg = None
    logger.info("This is a simple helloworld! You did not pass an arg")


def main():
    file_suffix = os.getenv("FILE_SUFFIX")
    output_path = f"/tmp/hello{file_suffix}.txt"

    with open(output_path, "w") as file:
        file.write(f"Hello {arg}, this is your script!")


if __name__ == "__main__":
    main()
