import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from karatsuba import karatsuba
from naive_multiplication import naive_multiplication
import pytest
import time

def test_karatsuba_short():
    s = time.perf_counter()
    num1 = 123
    num2 = 123
    res = num1*num2
    assert karatsuba(num1, num2) == res
    print(f'Runtime: {(time.perf_counter()-s)*1000*1000:.4f} us')

def test_naive_short():
    s = time.perf_counter()
    num1 = 123
    num2 = 123
    res = num1*num2
    assert naive_multiplication(num1, num2) == res
    print(f'Runtime: {(time.perf_counter()-s)*1000*1000:.4f} us')

def test_karatsuba_medium():
    s = time.perf_counter()
    num1 = 12343322
    num2 = 12341322
    res = num1*num2
    assert karatsuba(num1, num2) == res
    print(f'Runtime: {(time.perf_counter()-s)*1000*1000:.4f} us')

def test_naive_medium():
    s = time.perf_counter()
    num1 = 12343322
    num2 = 12341322
    res = num1*num2
    assert naive_multiplication(num1, num2) == res
    print(f'Runtime: {(time.perf_counter()-s)*1000*1000:.4f} us')

def test_karatsuba_long():
    s = time.perf_counter()
    num1 = 123433221908908
    num2 = 123433221908908
    res = num1*num2
    assert karatsuba(num1, num2) == res
    print(f'Runtime: {(time.perf_counter()-s)*1000*1000:.4f} us')

def test_naive_long():
    s = time.perf_counter()
    num1 = 123433221908908
    num2 = 123433221908908
    res = num1*num2
    assert naive_multiplication(num1, num2) == res
    print(f'Runtime: {(time.perf_counter()-s)*1000*1000:.4f} us')

def test_karatsuba_large():
    s = time.perf_counter()
    num1 = 90890123478013927401892341123412341234123412341234123412341234123412341234123412341234123412341234123412341234
    num2 = 90890123478013927401892341123412341234123412341234123412341234123412341234123412341234123412341234123412341234
    res = num1*num2
    assert karatsuba(num1, num2) == res
    print(f'Runtime: {(time.perf_counter()-s)*1000*1000:.4f} us')

def test_naive_large():
    s = time.perf_counter()
    num1 = 90890123478013927401892341123412341234123412341234123412341234123412341234123412341234123412341234123412341234
    num2 = 90890123478013927401892341123412341234123412341234123412341234123412341234123412341234123412341234123412341234
    res = num1*num2
    assert naive_multiplication(num1, num2) == res
    print(f'Runtime: {(time.perf_counter()-s)*1000*1000:.4f} us')

def test_python_large():
    s = time.perf_counter()
    num1 = 90890123478013927401892341123412341234123412341234123412341234123412341234123412341234123412341234123412341234
    num2 = 90890123478013927401892341123412341234123412341234123412341234123412341234123412341234123412341234123412341234
    res = num1*num2
    assert num1*num2 == res
    print(f'Runtime: {(time.perf_counter()-s)*1000*1000:.4f} us')