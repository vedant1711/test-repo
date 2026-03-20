"""Tests for the data processor module."""
from src.data_processor import (
    filter_even_numbers,
    calculate_average,
    flatten_list,
    find_duplicates,
    sort_by_key,
)


def test_filter_even_numbers():
    assert filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert filter_even_numbers([1, 3, 5]) == []


def test_calculate_average():
    assert calculate_average([10, 20, 30]) == 20.0


def test_calculate_average_empty():
    """This will FAIL — calculate_average doesn't handle empty lists."""
    try:
        result = calculate_average([])
        assert result == 0
    except ZeroDivisionError:
        assert False, "calculate_average should handle empty lists gracefully"


def test_flatten_list():
    assert flatten_list([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]
    assert flatten_list([]) == []


def test_find_duplicates():
    result = find_duplicates([1, 2, 3, 2, 4, 3])
    assert set(result) == {2, 3}


def test_sort_by_key():
    data = [{"name": "Charlie"}, {"name": "Alice"}, {"name": "Bob"}]
    result = sort_by_key(data, "name")
    assert result[0]["name"] == "Alice"


def test_sort_by_key_missing():
    """This will FAIL — sort_by_key doesn't handle missing keys."""
    data = [{"name": "Alice"}, {"age": 25}]
    try:
        sort_by_key(data, "name")
        assert False, "Should have raised an error for missing key"
    except KeyError:
        pass
