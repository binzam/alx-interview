#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import re
import sys


def extract_input(input_line):
    """Extracts sections of a line of an HTTP request log."""
    pattern = (
        r'\s*(?P<ip>\S+)\s* - \[(?P<date>.*?)\] "(?P<request>.*?)" '
        r'(?P<status_code>\d+) (?P<file_size>\d+)'
    )
    match = re.match(pattern, input_line)
    if match:
        return {
            "status_code": int(match.group("status_code")),
            "file_size": int(match.group("file_size")),
        }
    return None


def print_statistics(total_file_size, status_code_count):
    """Prints the accumulated statistics of the HTTP request log."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")


def run():
    """Starts the log parser."""
    total_file_size = 0
    status_code_count = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0,
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            line_info = extract_input(line)
            if line_info:
                total_file_size += line_info["file_size"]
                status_code = line_info["status_code"]
                if status_code in status_code_count:
                    status_code_count[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_statistics(total_file_size, status_code_count)

    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_code_count)


if __name__ == "__main__":
    run()
