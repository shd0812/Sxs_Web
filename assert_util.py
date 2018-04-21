"""
Built-in dependent functions used in YAML/JSON testcases.
"""


import re
import string
import time




def sleep(sec):
    """ sleep specified seconds
    """
    time.sleep(sec)


""" built-in comparators
"""


def equals(check_value, expect_value):
    assert check_value == expect_value


def less_than(check_value, expect_value):
    assert check_value < expect_value


def less_than_or_equals(check_value, expect_value):
    assert check_value <= expect_value

def greater_than(check_value, expect_value):
    assert check_value > expect_value


def greater_than_or_equals(check_value, expect_value):
    assert check_value >= expect_value


def not_equals(check_value, expect_value):
    assert check_value != expect_value


def string_equals(check_value, expect_value):
    assert str(check_value) == str(expect_value)

#结果的长度 是否 等于 预期的数 
def length_equals(check_value, expect_value):
    assert isinstance(expect_value, int)
    assert len(check_value) == expect_value


def length_greater_than(check_value, expect_value):
    assert isinstance(expect_value, int)
    assert len(check_value) > expect_value


def length_greater_than_or_equals(check_value, expect_value):
    assert isinstance(expect_value, int)
    assert len(check_value) >= expect_value


def length_less_than(check_value, expect_value):
    assert isinstance(expect_value, int)
    assert len(check_value) < expect_value

#结果的长度 是否 小于等于 预期的数 
def length_less_than_or_equals(check_value, expect_value):
    assert isinstance(expect_value, int)
    assert len(check_value) <= expect_value

	
	

def contains(check_value, expect_value):
    
    assert expect_value in check_value

#判断 结果是否在预期结果内
def contained_by(check_value, expect_value):
  
    assert check_value in expect_value







