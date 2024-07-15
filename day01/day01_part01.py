#!/usr/bin/env python3

import sys
import re
from pathlib import Path

def day01_part01(datafile):
    sum = 0
    for num in num_generator(datafile):
        # print(f"num: {num}")
        sum += num
    
    print(f"sum: {sum}")
    return sum
   
def num_generator(datafile):

    datafilepath = Path(__file__).parent/datafile
    print("Opening file: %s" % datafilepath)
    
    sum = 0.0
    for row in open(datafilepath, 'r'):
        # print(f"row: {row}")
        num = get_num(row)
        yield num
    
    print(f"digit_generator is now empty")
    return

# 
# A row of data might have just 1 digit, or 2 or more. 
# The row might contain 2 or more consecutive digits too, e.g. 34
# We want exactly TWO digits, the FIRST and the LAST digit in the string, which could be the same
# digit if there is only 1. If there is only 1 digit, that is the first and the last!
#
def get_num(row):
    alldigits = re.findall("[0-9]", row)
    d1 = alldigits[0]
    d2 = alldigits[-1]
    
    # Alternatively we could unpack as follows:
    # *x, last = alldigits # unpack - there will be at least 1 digit
    # print(f"last: {last}")
    
    twodigits = d1 + d2
    num = int(twodigits)
    return num

if __name__ == '__main__':
    print("We've been called directly, not imported.")
    datafile ="input.txt"
    if len(sys.argv) > 1:
        datafile = sys.argv[1]
    print("datafile: %s" % datafile)
    
    the_sum = day01_part01(datafile)
    #print(f"Answer = %d" % the_sum)
    print(f"Answer = {the_sum}")
    #print(f"Answer = {the_sum:.5f}")
    

