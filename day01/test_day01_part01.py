#import pytest

from day01_part01 import day01_part01
from day01_part01 import num_generator

# Use the sample data on the AoC question as test data:

# For example (see sample_input.txt):
#
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet

# In this example, the calibration values of these four lines are:
# 12, 38, 15, and 77. 

# Adding these together produces 142.

def test_sample_input_when_adding_together_then_sum_is_142():
    sum = day01_part01('sample_input.txt')
    assert sum == 142

def test_sample_input_then_calibration_values_are_12_38_15_and_77():
    expected_values = (12, 38, 15, 77)

    #fred = [ sum(x) for x in zip(expected_values, num_generator('sample_input.txt') )]
    #print(f'fred: {fred}')
   
    mypairs = [ p for p in zip(expected_values, num_generator('sample_input.txt') )]
    print(f'mypairs: {mypairs}')

    for p in mypairs:
        assert p[0] == p[1]
    
