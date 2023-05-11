#!/usr/bin/env python3

'''A script that reads stdin line by line and computes metris'''

import sys

total_file_size = 0
status_code_counts = {}

try:
    for i, line in enumerate(sys.stdin, 1):
        # Parse the input line based on the specified format
        parts = line.split()
        if len(parts) >= 7:
            ip_address = parts[0]
            status_code = parts[-2]
            file_size = int(parts[-1])

            # Update the total file size
            total_file_size += file_size

            # Update the status code counts
            if status_code.isdigit():
                status_code = int(status_code)
                status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1

        # Print statistics after every 10 lines
        if i % 10 == 0:
            print(f"File size: {total_file_size}")
            for code in sorted(status_code_counts):
                count = status_code_counts[code]
                print(f"{code}: {count}")

except KeyboardInterrupt:
    pass

# Print final statistics
print(f"File size: {total_file_size}")
for code in sorted(status_code_counts):
    count = status_code_counts[code]
    print(f"{code}: {count}")

