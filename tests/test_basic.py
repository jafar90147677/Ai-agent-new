"""
Basic tests for automated pytest testing.
These tests will run automatically when you push code to GitHub.
"""

import pytest


def test_basic_functionality():
    """Test basic Python functionality."""
    assert True


def test_arithmetic():
    """Test basic arithmetic operations."""
    assert 2 + 2 == 4
    assert 10 - 5 == 5
    assert 3 * 4 == 12
    assert 8 / 2 == 4


def test_string_operations():
    """Test string operations."""
    text = "Hello World"
    assert len(text) == 11
    assert text.upper() == "HELLO WORLD"
    assert text.lower() == "hello world"
    assert "World" in text


def test_list_operations():
    """Test list operations."""
    my_list = [1, 2, 3, 4, 5]
    assert len(my_list) == 5
    assert 3 in my_list
    assert my_list[0] == 1
    assert my_list[-1] == 5


def test_dictionary_operations():
    """Test dictionary operations."""
    my_dict = {"name": "test", "value": 42}
    assert "name" in my_dict
    assert my_dict["name"] == "test"
    assert my_dict["value"] == 42


def test_conditional_logic():
    """Test conditional logic."""
    x = 10
    y = 5
    
    assert x > y
    assert x >= y
    assert y < x
    assert y <= x
    assert x != y


@pytest.mark.slow
def test_slow_operation():
    """Test marked as slow - will be skipped in fast runs."""
    import time
    time.sleep(0.1)  # Simulate slow operation
    assert True


def test_exception_handling():
    """Test exception handling."""
    with pytest.raises(ValueError):
        int("not_a_number")
    
    with pytest.raises(IndexError):
        my_list = [1, 2, 3]
        my_list[10]


def test_file_operations():
    """Test file operations."""
    import tempfile
    import os
    
    # Test creating and writing to a temporary file
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write("test content")
        temp_file = f.name
    
    # Verify file exists and has content
    assert os.path.exists(temp_file)
    with open(temp_file, 'r') as f:
        content = f.read()
        assert content == "test content"
    
    # Clean up
    os.unlink(temp_file)
