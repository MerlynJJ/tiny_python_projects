#!/usr/bin/env python3
# Purpose: Say hello

import argparse

parser = argparse.ArgumentParser(description='Say hello')
parser.add_argument('name', help='Name to greet')
## parse module provide us with the help message
args = parser.parse_args()
print('Hello, ' + args.name + '!')
