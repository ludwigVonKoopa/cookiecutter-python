import argparse


def usage():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-v",
        "--verbose",
        action="store",
        help="verbose",
        choices=["ERROR", "WARNING", "INFO", "DEBUG"],
        default="INFO",
    )
    return parser.parse_args()


def cli():
    args = usage()
    print("one simple command line")
