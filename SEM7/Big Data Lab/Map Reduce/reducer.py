#!/usr/bin/env python3
import sys

def main():
    current_key = None
    current_count = 0

    # Read the sorted intermediate key-value pairs from stdin
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
            
        # Split key and value
        try:
            key, count = line.split("\t", 1)
            count = int(count)
        except ValueError:
            continue

        # Aggregate counts for the same key
        if current_key == key:
            current_count += count
        else:
            if current_key:
                print(f"{current_key}\t{current_count}")

            current_key = key
            current_count = count

    # Print the last key-value pair
    if current_key:
        print(f"{current_key}\t{current_count}")

if __name__ == "__main__":
    main()
