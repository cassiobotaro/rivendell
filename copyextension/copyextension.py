#!/usr/bin/env python
'''
copytext

Small script to copy all files of 'extension' from 'source' to 'destiny'.

usage: copyextension.py [-h] extension source destiny

positional arguments:
  extension   files extension
  source      directory that will be scanned
  destiny     directory where files will be pasted

optional arguments:
  -h, --help  show this help message and exit
'''
import argparse
import shutil
import sys
from pathlib import Path

# argparse is used to provide a better interface and help
parser = argparse.ArgumentParser()
parser.add_argument('extension', help='files extension')
parser.add_argument('source', help='directory that will be scanned')
parser.add_argument('destiny', help='directory where files will be pasted')
args = parser.parse_args()
extension, source, destiny = args.extension, Path(args.source), \
    Path(args.destiny)

# check if source and destiny exists
if not source.is_dir() or not destiny.is_dir():
    print('source or destiny doesn\'t exists.', file=sys.stderr)
    sys.exit(1)

# iterate over source source directory looking for that extension,
# then copy the file
for file in source.glob(f'*.{extension}'):
    print(f'copying {file}...')
    shutil.copy2(file, destiny)

print('Done!')
