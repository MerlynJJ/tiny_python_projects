#!/usr/bin/env python3
# Purpose: Say hello

import argparse

parser = argparse.ArgumentParser(description='Say hello')
parser.add_argument('-n', '--name', metavar='name',
                    default='World', help='Name to greet')
## the positional argument now is optional
## the defaul value = World, i.e. running the program with no arguments
## will print Hello, World!
args = parser.parse_args()
print('Hello, ' + args.name + '!')
