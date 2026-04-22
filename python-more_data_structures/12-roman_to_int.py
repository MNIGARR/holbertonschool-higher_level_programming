#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer.
    Args:
        roman_string: The string representing a Roman numeral.
    Returns:
        The integer value of the numeral, or 0 if invalid input.
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
        
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    length = len(roman_string)
    
    for i in range(length):
        current_val = roman_dict.get(roman_string[i], 0)
        
        # If there is a next character and the current value is less than the next,
        # it means we are in a subtraction scenario (e.g., IV or IX)
        if i + 1 < length and current_val < roman_dict.get(roman_string[i + 1], 0):
            total -= current_val
        else:
            total += current_val
            
    return total
