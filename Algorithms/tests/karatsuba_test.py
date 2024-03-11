import sys
sys.path.append("./")
from karatsuba import karatsuba
import pytest

def test_same_length_odd():
    num1 = 123
    num2 = 123
    res = num1*num2
    assert karatsuba(num1, num2) == res

def test_diff_length():
    num1 = 1234
    num2 = 12
    res = num1*num2
    assert karatsuba(num1, num2) == res

def test_same_length_even():
    num1 = 1234
    num2 = 1234
    res = num1*num2
    assert karatsuba(num1, num2) == res

def test_same_length_power_of_2():
    num1 = 12343322
    num2 = 12341322
    res = num1*num2
    assert karatsuba(num1, num2) == res

def test_zero1():
    num1 = 0
    num2 = 123
    res = num1*num2
    assert karatsuba(num1, num2) == res

def test_zero2():
    num1 = 123
    num2 = 0
    res = num1*num2
    assert karatsuba(num1, num2) == res

def test_zero3():
    num1 = 0
    num2 = 0
    res = num1*num2
    assert karatsuba(num1, num2) == res

def test_negative_odd():
    num1 = -123
    num2 = -321
    res = num1*num2
    assert karatsuba(num1, num2) == res

def test_negative_even():
    num1 = -1230
    num2 = -3211
    res = num1*num2
    assert karatsuba(num1, num2) == res

def test_negative_and_positive():
    num1 = -12312
    num2 = 321
    res = num1*num2
    assert karatsuba(num1, num2) == res

def test_positive_and_negative():
    num1 = 321
    num2 = -123431
    res = num1*num2
    assert karatsuba(num1, num2) == res

def test_large_numbers():
    num1 = 90890123478013927401892341
    num2 = 90890123478013927401892344
    res = num1*num2
    assert karatsuba(num1, num2) == res

def test_digit_increase_third_term():
    num1 = 9999
    num2 = 9999
    res = num1*num2
    assert karatsuba(num1, num2) == res

def test_diff_size_third_term():
    num1 = 9999
    num2 = 1111
    res = num1*num2
    assert karatsuba(num1, num2) == res

def test_large_af_numbers():
    num1 = 90890123478013927401892341123412341234123412341234123412341234123412341234123412341234123412341234123412341234
    num2 = 90890123478013927401892341123412341234123412341234123412341234123412341234123412341234123412341234123412341234
    res = num1*num2
    assert karatsuba(num1, num2) == res