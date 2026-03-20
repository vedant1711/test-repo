"""Data processing module."""


def filter_even_numbers(numbers):
    """Return only even numbers from the list."""
    return [n for n in numbers if n % 2 == 0]


def calculate_average(numbers):
    """Calculate the average of a list of numbers.

    BUG: Does not handle empty list!
    """
    return sum(numbers) / len(numbers)


def flatten_list(nested_list):
    """Flatten a nested list into a single list."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


def find_duplicates(items):
    """Find duplicate items in a list."""
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)


def sort_by_key(data, key):
    """Sort a list of dictionaries by a given key.

    BUG: Crashes if key doesn't exist in a dictionary!
    """
    return sorted(data, key=lambda x: x[key])
