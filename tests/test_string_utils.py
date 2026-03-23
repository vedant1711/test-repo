"""Tests for string utility functions."""
from src.string_utils import (
    reverse_string,
    reverse_words,
    capitalize_words,
    count_vowels,
    is_palindrome,
)


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""


def test_reverse_words():
    assert reverse_words("hello world") == "world hello"
    assert reverse_words("one") == "one"
    assert reverse_words("") == ""
    assert reverse_words(" ") == ""


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"


def test_count_vowels():
    assert count_vowels("hello") == 2
    # This will FAIL because count_vowels doesn't handle uppercase
    assert count_vowels("HELLO") == 2


def test_is_palindrome():
    assert is_palindrome("racecar") == True
    # This will FAIL because is_palindrome is case-sensitive
    assert is_palindrome("Racecar") == True
