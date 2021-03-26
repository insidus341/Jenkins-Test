"""Test the functions.py file."""
import run.core.functions as functions
import pytest

def test_adding_two_positive_numbers():
    """Test two positive numbers against functions.add_two_numbers."""
    assert functions.add_two_numbers(10, 20) == 30

def test_adding_two_negative_numbers():
    """Test two negative numbers against functions.add_two_numbers."""
    assert functions.add_two_numbers(-10, -20) == -30

def test_add_positive_and_negative_numbers():
    """Test one positive and one negative number against functions.add_two_numbers."""
    assert functions.add_two_numbers(-10, 10) == 0

def test_add_letter_and_number():
    """Test adding one letter and one number against functions.add_two_numbers."""
    with pytest.raises(TypeError):
        functions.add_two_numbers("a", 10)

def test_this_test_will_fail():
    """This is a test test, it should fail"""
    assert functions.add_two_numbers(1, 2) == 5
