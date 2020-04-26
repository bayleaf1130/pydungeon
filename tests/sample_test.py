import pytest

""" Sample Test """


# Pytest discovers this and runs
def test_method_one():
    x = 5
    y = 6
    assert x + 1 == y, "Test Failed"


# Pytest discovers this when run and tests the methods inside
def TestClass():
    def test_one(self):
        x = "this"
        assert 'h' in x
    
    def test_two(self):
        x = 'hello'
        assert 'n' in h