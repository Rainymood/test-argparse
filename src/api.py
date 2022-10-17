import argparse
import copy
import sys

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--name",
        type=str,
        default="John Doe",
    )
    args, _ = parser.parse_known_args(sys.argv[1:])
    args_dict = copy.copy(vars(args))

    print(f"Hello, {args_dict['name']}")
