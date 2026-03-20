"""String utility functions with intentional edge case bugs."""


def reverse_string(s):
    """Reverse a string."""
    return s[::-1]


def reverse_words(sentence):
    """Reverse the order of words in a sentence.

    BUG: Crashes on empty string input!
    """
    if not sentence:
        return ""
    words = sentence.split(" ")
    return " ".join(words[::-1])


def capitalize_words(sentence):
    """Capitalize the first letter of each word."""
    return " ".join(word.capitalize() for word in sentence.split())


def count_vowels(s):
    """Count the number of vowels in a string.

    BUG: Only counts lowercase vowels!
    """
    vowels = "aeiou"
    return sum(1 for char in s if char in vowels)


def is_palindrome(s):
    """Check if a string is a palindrome.

    BUG: Case-sensitive comparison — 'Racecar' returns False!
    """
    return s == s[::-1]
