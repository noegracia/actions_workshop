"This module aim to run some unit test"

def increment(num):
    """Increments the given number by 1."""
    return num + 1

def test_inc():
    """Run a unit test of the increment function"""
    assert increment(4) == 5
