import argparse


def read_user_cli_args():
    """Handle the CLI arguments and options."""
    parser = argparse.ArgumentParser(
        prog="tvKanChk", description="check the availability of websites"
    )
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="enter one or more website URLs",
    )
    parser.add_argument(
        "-f",
        "--input-file",
        metavar="FILE",
        type=str,
        default="",
        help="read URLs from a file",
    )
    parser.add_argument(
        "-p",
        "--pls",
        metavar="FILE.m3u8",
        nargs="+",
        type=str,
        default=[],
        help="Check playlist status is online",
    )
    return parser.parse_args()


def display_check_result(result, url, error=""):
    """Display the result of a connectivity check."""
    print(f'The status of "{url}" is:', end=" ")
    if result:
        print('Online')
    else:
        print(f'"Offline?"\n  Error: "{error}"')
