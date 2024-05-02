#!/usr/bin/python3
"""A script for parsing HTTP request logs.
"""
import sys
import signal

total_file_size = 0
status_code_count = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }


def signal_handler(sig, frame):
    """Signal handler for SIGINT (Ctrl+C)"""
    print_stats()
    sys.exit(0)


def print_stats(total_file_size, status_code_count):
    """Function to print the statistics"""
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")


signal.signal(signal.SIGINT, signal_handler)

line_count = 0
for line in sys.stdin:
    line = line.strip()
    parts = line.split()
    if len(parts) >= 10 and parts[5].isdigit():
        file_size = int(parts[9])
        total_file_size += file_size
        status_code = int(parts[8])
        if status_code in status_code_count:
            status_code_count[status_code] += 1
        line_count += 1

        if line_count % 10 == 0:
            print_stats()

if __name__ == "__main__":
    print_stats()
