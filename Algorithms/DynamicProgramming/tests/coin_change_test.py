import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from coin_change import coin_change_bottom_up, coin_change_top_down
import pytest
import math

def test_no_coins():
    coins = []
    amount = 1
    assert coin_change_bottom_up(coins, amount) == (-1, -1)
    assert coin_change_top_down(coins, amount) == (-1, -1)

def test_zero_amount():
    coins = [1]
    amount = 0
    assert coin_change_bottom_up(coins, amount) == (0, [])
    assert coin_change_top_down(coins, amount) == (0, [])

def test_basic():
    coins = [1]
    amount = 123
    assert coin_change_bottom_up(coins, amount) == (123, [1]*123)
    assert coin_change_top_down(coins, amount) == (123, [1]*123)

def test_multiple_coins():
    coins = [1, 2, 5, 10, 20, 50, 100]
    amount = 113
    assert coin_change_bottom_up(coins, amount) == (4, [1, 2, 10, 100])
    assert coin_change_top_down(coins, amount) == (4, [1, 2, 10, 100])

def test_not_possible():
    coins = [2]
    amount = 5
    assert coin_change_bottom_up(coins, amount) == (-1, -1)
    assert coin_change_top_down(coins, amount) == (-1, -1)