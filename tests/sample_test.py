import pytest

""" Sample Test """


# Pytest discovers this and runs
def test_method_one():
    x = 5
    y = 6
    assert (x + 1) == y, "Test Failed"