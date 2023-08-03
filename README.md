# Windrend - simple summarizer for arbitrary-length text

Windrend is a quick and dirty (currently) command-line Python script that interacts with the OpenAI Chat Completion API, the API version of ChatGPT.

Windrend was first created by Peter Kaminski and ChatGPT (GPT-4) on 2023-08-01.

Comments and bug reports are welcome at <https://github.com/peterkaminski/windrend/issues>, and I'm happy to review pull requests.

## Requirements

- Python 3.6 or higher
- `requests` library

## Installation

1. Clone this repository or download the `windrend.py` file.
2. Install the `requests` library (recommended: activate a Python virtual environment first):

```bash
pip install requests
```

## Usage

Set the OPENAI_API_KEY environment variable to your OpenAI API key:

```bash
export OPENAI_API_KEY="your_openai_api_key_here"
```

You can copy `env.sh-template` to `env.sh`, add your API key to it, and then use `source env.sh` to add your API key to the environment.

Run the program with the input text file:

```bash
python windrend.py --input input.txt
```

Or you can change directory to where `windrend.py` is located and run it as an executable:

```bash
./windrend.py --input input.txt
```

Output currently goes to STDOUT, and the intermediate summary files are stored to `summaries.txt`. This behaviour could be improved by parameterizing the summary and summary-of-summaries output files.

## UnWebVTT

A similarly quick and dirty utility is included to read a friendly-structured WebVTT file, strip the timestamps, and output just text. It does _not_ handle full-blown WebVTT format; it does not dedupe, for one thing.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
