from hypothesis import given
from hypothesis.strategies import integers, lists


def mysort(unsorted_array):
    return unsorted_array

# test
@given(lists(integers()))
def test_mysort(unsorted_array):
    assert(mysort(unsorted_array) == sorted(unsorted_array))
