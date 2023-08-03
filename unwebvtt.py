#!/usr/bin/env python

# UnWebVTT v1.0.0 - https://github.com/peterkaminski/unwebvtt

# Copyright 2023 Peter Kaminski. Licensed under MIT license, see accompanying LICENSE file.

import sys
import argparse
import re

def process_file(input_file, output_file):
    for line in input_file:
        # Skip empty lines
        if line.strip() == "":
            continue
        # Skip lines with timestamps
        if re.match(r'^\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}$', line.strip()):
            continue
        # Write non-empty, non-timestamp lines to output
        output_file.write(line)

def main():
    parser = argparse.ArgumentParser(description='Convert WebVTT to plain text.')
    parser.add_argument('--input', metavar='in', type=str, help='the input file path')
    parser.add_argument('--output', metavar='out', type=str, help='the output file path')
    args = parser.parse_args()

    # Use standard in/out if no file specified
    input_file = open(args.input, 'r') if args.input else sys.stdin
    output_file = open(args.output, 'w') if args.output else sys.stdout

    try:
        process_file(input_file, output_file)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
    finally:
        # Close files if they were actually files
        if args.input:
            input_file.close()
        if args.output:
            output_file.close()

if __name__ == "__main__":
    main()
