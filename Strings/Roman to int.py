def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000}

    total = 0
    prev = 0

    for ch in reversed(s):
        if roman[ch] < prev:
            total -= roman[ch]
        else:
            total += roman[ch]
        prev = roman[ch]

    return total


s = input("Enter Roman numeral: ")

print("Integer:", roman_to_int(s))
