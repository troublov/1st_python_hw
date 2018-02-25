# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 16:04:52 2018

@author: Orlov
"""

import argparse

cl_parser=argparse.ArgumentParser(description='Test mini argparse programm for 1st GitHub publishing. \
                                  Powers 1st number in the 2nd value')
cl_parser.add_argument('-n', '--number', help='number to be powered', type=float)
cl_parser.add_argument('-p', '--power', help='power value', type=float)

args=cl_parser.parse_args()
num=args.number
power=args.power

print(num**power)


