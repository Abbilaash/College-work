#!/usr/bin/env python3
import sys

def main():
    # Read from standard input line by line (Hadoop streams data via stdin)
    for line in sys.stdin:
        # 1. Line count: emit 1 for each line read
        print("lines\t1")
        
        # 2. Word count: split line by whitespace, count words, and emit the total
        words = line.split()
        print(f"words\t{len(words)}")
        
        # 3. Character count: get length of the line and emit the total
        print(f"characters\t{len(line)}")

if __name__ == "__main__":
    main()
