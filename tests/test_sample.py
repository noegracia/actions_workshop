"This module aim to run some unit test"

from ..main import increment

def test_inc():
    """Run a unit test of the increment function"""
    assert increment(4) == 5
