import pytest

def fun(x):
    return x + 1

def test_fun():
    assert fun(3) == 4
