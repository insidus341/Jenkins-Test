import run.core.functions as functions

def test_adding_two_positive_numbers():
    assert functions.add_two_numbers(10, 20) == 30

def test_adding_two_negative_numbers():
    assert functions.add_two_numbers(-10, -20) == -30

def test_add_positive_and_negative_numbers():
    assert functions.add_two_numbers(-10, 10) == 0