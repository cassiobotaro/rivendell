#!/usr/bin/env python
'''
xlsx2csv

Convert xlsx to csv.

usage: xlsx2csv.py [-h] [--sheet SHEET] filename

positional arguments:
  filename       name of xlsx file

optional arguments:
  -h, --help     show this help message and exit
  --sheet SHEET  name of the sheet
'''
import argparse
import csv
import sys

import openpyxl

# Define command line interface
parser = argparse.ArgumentParser()
parser.add_argument('filename', help='name of xlsx file')
parser.add_argument('--sheet', required=False, help='name of the sheet')
args = parser.parse_args()

# load file, but don't convert fields
workbook = openpyxl.load_workbook(filename=args.filename, guess_types=False)
# get first sheet or use name passed as parameter
sheet_name, *_ = workbook.sheetnames
if args.sheet:
    sheet_name = args.sheet

# get sheet by it's name
sheet = workbook[sheet_name]

csv_writer = csv.writer(sys.stdout, quoting=csv.QUOTE_ALL, lineterminator='\n')
# write each csv line in stdout
for row in sheet.rows:
    csv_writer.writerow(column.value or '' for column in row)
