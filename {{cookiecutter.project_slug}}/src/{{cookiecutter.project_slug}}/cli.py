import argparse

import {{ cookiecutter.project_slug }}.log  # noqa: F401

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


def app():
    args = usage()
    {{ cookiecutter.project_slug }}.log.create_logger(level="DEBUG")

    print("one simple command line")
