#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value.
    Args:
        a_dictionary: The dictionary containing string keys and integer values.
    Returns:
        The key with the maximum value, or None if no score is found.
    """
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
