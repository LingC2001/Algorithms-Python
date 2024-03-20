import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from naive_multiplication import naive_multiplication
import pytest

def test_same_length():
    num1 = 123
    num2 = 123
    res = num1*num2
    assert naive_multiplication(num1, num2) == res

def test_diff_length():
    num1 = 1234
    num2 = 12
    res = num1*num2
    assert naive_multiplication(num1, num2) == res

def test_zero1():
    num1 = 0
    num2 = 123
    res = num1*num2
    assert naive_multiplication(num1, num2) == res

def test_zero2():
    num1 = 123
    num2 = 0
    res = num1*num2
    assert naive_multiplication(num1, num2) == res

def test_zero3():
    num1 = 0
    num2 = 0
    res = num1*num2
    assert naive_multiplication(num1, num2) == res

def test_negative():
    num1 = -123
    num2 = -321
    res = num1*num2
    assert naive_multiplication(num1, num2) == res

def test_negative_and_positive():
    num1 = -123
    num2 = 321
    res = num1*num2
    assert naive_multiplication(num1, num2) == res

def test_positive_and_negative():
    num1 = 321
    num2 = -123
    res = num1*num2
    assert naive_multiplication(num1, num2) == res

def test_large_numbers():
    num1 = 9089012347801392740189234
    num2 = 9089012347801392740189234
    res = num1*num2
    assert naive_multiplication(num1, num2) == res