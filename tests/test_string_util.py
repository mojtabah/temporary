"""
Tests for temporary.string_util module
"""

from temporary import *
import pytest

@pytest.fixture()
def str_3():
    return "tItle TiTlE"

@pytest.mark.parametrize("s, expected_title", [
    ("dUmmy tiTle", "Dummy Title"),
    ("ANOTHER title", "Another Title")
    ])
def test_many(s, expected_title):
    assert title_string(s) == expected_title
 
@pytest.mark.skipif(False, reason='comment')
def test_title():
    s = "dUmmy tiTle"
    observed = title_string(s)
    expected = "Dummy Title"
    assert observed == expected, 'title_string test failed'

@pytest.mark.my_easy_tests
def test_str_type():
    str_tuple = ('a','b')
    with pytest.raises(TypeError):
        title_string(str_tuple)
    
    test_var = 8
    with pytest.raises(TypeError):
        title_string(test_var)
        
    num_list = [1,2,3,'a','b','c']
    with pytest.raises(TypeError):
        title_string(num_list)
    
def test_empty_string():
    num_list = ""
    with pytest.raises(Exception):
        mean(num_list)    
        
def test_mean_fixture(str_3):
    assert title_string(str_3) == "Title Title"

# @pytest.mark.parametrize("x", [0,1])
# @pytest.mark.parametrize("y", [2,3])
# def test_foo(x,y):
#     pass