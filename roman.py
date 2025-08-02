def roman_to_int(s: str) -> int:
    """
    Converts a Roman numeral string to its integer equivalent.

    Args:
        s: The Roman numeral string (e.g., "MCMXCIV").

    Returns:
        The integer equivalent of the Roman numeral.
    """
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0  # To store the value of the previous Roman numeral

    # Iterate through the Roman numeral string from right to left
    for char in reversed(s):
        current_value = roman_values[char]

        # Apply subtractive or additive principle
        if current_value >= prev_value:
            total += current_value
        else:
            total -= current_value

        prev_value = current_value

    return total

roman_numeral1 = "III"
print(f"The integer value of {roman_numeral1} is: {roman_to_int(roman_numeral1)}")

roman_numeral2 = "XXV"
print(f"The integer value of {roman_numeral2} is: {roman_to_int(roman_numeral2)}")

roman_numeral3 = "MDC"
print(f"The integer value of {roman_numeral3} is: {roman_to_int(roman_numeral3)}")

        