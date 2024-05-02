#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import subprocess
import signal
import sys

total_file_size = 0
status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)


def print_statistics():

    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")
    print("")


signal.signal(signal.SIGINT, signal_handler)


def generate_input():
    process = subprocess.Popen(
        ["python3", "0-generator.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    for line in process.stdout:
        yield line.decode("utf-8").strip()


line_count = 0
for line in generate_input():
    parts = line.split()
    if len(parts) >= 10 and parts[5].isdigit():
        file_size = int(parts[9])
        total_file_size += file_size
        status_code = int(parts[8])
        if status_code in status_code_count:
            status_code_count[status_code] += 1
        line_count += 1

        if line_count % 10 == 0:
            print_statistics()

if __name__ == "__main__":
    print_statistics()
