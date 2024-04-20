import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from edit_distance import edit_distance
import pytest

def test_empty_strings():
    s1 = ""
    s2 = ""

    assert edit_distance(s1, s2) == 0

def test_matching():
    s1 = "abcdefg"
    s2 = "abcdefg"

    assert edit_distance(s1, s2) == 0

def test_replace():
    s1 = "abzdefg"
    s2 = "abcdefg"

    assert edit_distance(s1, s2) == 1

def test_replace_two():
    s1 = "abzzefg"
    s2 = "abcdefg"

    assert edit_distance(s1, s2) == 2


def test_remove():
    s1 = "abcddefg"
    s2 = "abcdefg"

    assert edit_distance(s1, s2) == 1

def test_remove_two():
    s1 = "abcddefgz"
    s2 = "abcdefg"

    assert edit_distance(s1, s2) == 2

def test_insert():
    s1 = "abcefg"
    s2 = "abcdefg"

    assert edit_distance(s1, s2) == 1

def test_insert_two():
    s1 = "bcefg"
    s2 = "abcdefg"

    assert edit_distance(s1, s2) == 2