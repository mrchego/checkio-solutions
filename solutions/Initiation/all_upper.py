#!/usr/bin/env checkio --domain=py run all-upper

# Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - function should returnTrue.
# 
# 
# 
# Input:A string(str).
# 
# Output:A logic value(bool).
# 
# Precondition:a-z, A-Z, 1-9 and spaces
# 
# 
# END_DESC

def is_all_upper(text: str) -> bool:
    # your code here
    return False


print("Example:")
print(is_all_upper("ALL UPPER"))

# These "asserts" are used for self-checking
assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == True
assert is_all_upper("444") == True
assert is_all_upper("55 55 5 ") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")