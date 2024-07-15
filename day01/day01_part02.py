#!/usr/bin/env python3

import sys
import re
from pathlib import Path

def day01_part02(datafile):
    sum = 0
    for num in num_generator(datafile):
        sum += num
    
    print(f"sum: {sum}")
    return sum
   
def num_generator(datafile):
    datafilepath = Path(__file__).parent/datafile
    print("Opening file: %s" % datafilepath)
    
    sum = 0.0
    for row in open(datafilepath, 'r'):
        num = get_num(row)
        yield num
    
    print(f"digit_generator is now empty")
    return

# 
#
def get_num(row):
    two_digits = get_two_digits(row)
    mynum = ''.join(two_digits)
    num = int(mynum)
    return num

#
# A row of data might have just 1 digit, or 2 or more. 
# The row might contain 2 or more consecutive digits too, e.g. 34
# We want exactly TWO digits, the FIRST and the LAST digit in the string, which could be the same
# digit if there is only 1. If there is only 1 digit, that is the first and the last!
# get digits 0-9 and  string "one", "two", ... "nine"
#
def get_two_digits(row):
    valid_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
                    'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' ]
    
    pseudo_digits = re.findall(r"(?=("+'|'.join(valid_digits)+r"))", row) # works
    
    # Need to convert 'one' to '1' etc for the first and last digits only
    two_pseudo_digits = [pseudo_digits[i] for i in (0, -1)]
    digits = [convert_word_to_digit(x) for x in two_pseudo_digits]
    return digits

def convert_word_to_digit(word):
    if word == 'one':
        return '1'
    elif word == 'two':
        return '2'
    elif word == 'three':
        return '3'
    elif word == 'four':
        return '4'
    elif word == 'five':
        return '5'
    elif word == 'six':
        return '6'
    elif word == 'seven':
        return '7'
    elif word == 'eight':
        return '8'
    elif word == 'nine':
        return '9'
    else: 
        return word
                

if __name__ == '__main__':
    print("Part 02 has been called directly, not imported.")
    datafile ="input.txt"
    if len(sys.argv) > 1:
        datafile = sys.argv[1]
    print("datafile: %s" % datafile)
    
    the_sum = day01_part02(datafile)
    print(f"Answer = {the_sum}")
    

