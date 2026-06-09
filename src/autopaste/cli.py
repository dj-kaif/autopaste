"""
MIT License

Copyright (c) 2026 DJ KAIF

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sys
import argparse
from importlib.metadata import version, PackageNotFoundError
from autopaste.upload import upload

def get_version():
    try:
        return version("autopaste")
    except PackageNotFoundError:
        return "1.0.0"

def main():
    parser = argparse.ArgumentParser(
        description="A minimalist CLI tool to upload text and files to paste.c-net.org"
    )
    parser.add_argument(
        "filepath", 
        nargs="?", 
        help="Optional path to the file you want to upload"
    )

    parser.add_argument(
        "-v", "--version", 
        action="version", 
        version=f"autopaste {get_version()}"
    )

    args = parser.parse_args()

    content = ""

    if args.filepath:
        try:
            with open(args.filepath, "r", encoding="utf-8") as f:
                content = f.read()
        except FileNotFoundError:
            print(f"Error: '{args.filepath}' doesn't exist!")
            return

    elif not sys.stdin.isatty():
        content = sys.stdin.read()

    else:
        content = input("Paste or Write: ")

    if not content.strip():
        print("Error: Content cannot be empty!")
        return


    link = upload(content)
    print(f"Your pastebin url is: {link}")
