"""
Tests for temporary.math module
"""

from temporary import *
import pytest
import numpy as np

@pytest.fixture()
def num_list_3():
    return [1,2,3,4,5]

@pytest.mark.parametrize("num_list, expected_mean", [
    ([1,2,3,4,5], 3),
    ([0,2,4,6], 3),
    ([1,2,3,4], 2.5),
    (list(range(1,10000)), 10000/2)
    ]) 
def test_many(num_list, expected_mean):
#     assert mean(num_list) == expected_mean
    assert np.isclose(mean(num_list), expected_mean, 1e-6)
 
@pytest.mark.skipif(False, reason='comment')
def test_mean():
    num_list = [1,2,3,4,5]
    observed = mean(num_list)
    expected = 3
    assert observed == expected, 'Mean test failed'

@pytest.mark.my_easy_tests
def test_list_type():
    num_tuple = (1,2,3,4,5)
    with pytest.raises(TypeError):
        mean(num_tuple)
    
    test_var = 8
    with pytest.raises(TypeError):
        mean(test_var)
        
    num_list = [1,2,3,'a','b','c']
    with pytest.raises(TypeError):
        mean(num_list)
    
def test_empty_list():
    num_list = []
    with pytest.raises(ZeroDivisionError):
        mean(num_list)    
        
def test_mean_fixture(num_list_3):
    assert mean(num_list_3) == 3

@pytest.mark.parametrize("x", [0,1])
@pytest.mark.parametrize("y", [2,3])
def test_foo(x,y):
    pass