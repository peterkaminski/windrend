#!/usr/bin/env python

# Windrend v1.0.0 - https://github.com/peterkaminski/windrend

# Copyright 2023 Peter Kaminski. Licensed under MIT license, see accompanying LICENSE file.

import argparse
import os
import requests
import textwrap
import sys
import logging

def summarize(api_url, headers, text):
    try:
        data = {
            "model": "gpt-4",
            "messages": [{
                "role": "system",
                "content": "You are a helpful assistant that summarizes text. Just output a summary, do not refer to the speaker."
            }, {
                "role": "user",
                "content": text
            }],
            "max_tokens": 500  # You may want to adjust this
        }

        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()  # Raises a HTTPError if the response was an HTTP error
    except requests.exceptions.RequestException as err:
        print(f"API request failed: {err}")
        sys.exit(1)

    result = response.json()
    return result['choices'][0]['message']['content']

def main():
    # Set up logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
    
    parser = argparse.ArgumentParser(description="Segment a text file, summarize each segment, then summarize that.")
    parser.add_argument('-i', '--input', required=True, help="The input text file to segment and summarize.")
    args = parser.parse_args()

    # Get API Key
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Please set the 'OPENAI_API_KEY' environment variable")

    # GPT-4 API information
    api_url = "https://api.openai.com/v1/chat/completions"  # Adjust this to the actual GPT-4 API endpoint
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Read the input text file
    try:
        with open(args.input, 'r') as file:
            text = file.read()
    except IOError as err:
        print(f"Failed to open file: {err}")
        sys.exit(1)

    # Segment the text file into smaller pieces
    segment_size = 8192  # Modify this to your needs
    segments = textwrap.wrap(text, segment_size)

    summaries = []

    # Send each piece to the GPT-4 API to be summarized
    for i, segment in enumerate(segments):
        logging.info(f'Processing segment {i+1} of {len(segments)}')
        summary = summarize(api_url, headers, segment)
        summaries.append(summary)

    # Store the summaries
    try:
        with open('summaries.txt', 'w') as file:
            file.write("\n".join(summaries))
    except IOError as err:
        print(f"Failed to write summaries to file: {err}")
        sys.exit(1)

    # Send all the summaries to the GPT-4 API to be summarized
    final_summary = summarize(api_url, headers, "\n".join(summaries))

    # Print the final summary
    print(final_summary)

if __name__ == "__main__":
    main()
