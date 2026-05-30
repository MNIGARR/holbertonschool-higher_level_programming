#!/usr/bin/python3
"""Module that parses a log file from stdin and prints statistics."""
import sys


def print_stats(total_size, status_counts):
    """
    Prints the accumulated log statistics.
    
    Args:
        total_size (int): The total accumulated file size.
        status_counts (dict): A dictionary containing counts of status codes.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


if __name__ == "__main__":
    total_size = 0
    status_counts = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            if len(parts) >= 2:
                # Attempt to extract and add the file size (last element)
                try:
                    total_size += int(parts[-1])
                except ValueError:
                    pass
                
                # Check if the status code (second-to-last element) is valid
                status = parts[-2]
                if status in status_counts:
                    status_counts[status] += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

        # Print statistics at the end of the file/stream
        print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        # Print statistics upon a keyboard interruption
        print_stats(total_size, status_counts)
        raise
