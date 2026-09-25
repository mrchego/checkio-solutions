#!/usr/bin/env checkio --domain=py run sort-array-by-element-frequency

# Sort the given list so that its    elements should be grouped and those groups end up in the decreasing frequency order, that is, the number of    times element appears in list. If two elements have the same frequency, their groups    should end up in the same order as the first appearance of element in the list.
# 
# 
# 
# If you want to practice more with the similar case, tryFrequency Sortingmission.
# 
# Input:List
# 
# Output:List or another Iterable (tuple, iterator, generator)
# 
# Precondition:elements can be ints or strings
# 
# The mission was taken from Python CCPS 109 Fall 2018. It's being taught for    Ryerson Chang School of Continuing Education byIlkka Kokkarinen
# 
# 
# END_DESC

from collections.abc import Iterable


def frequency_sort(items: list[str | int]) -> Iterable[str | int]:
    # your code here
    return items


print("Example:")
print(list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])))

# These "asserts" are used for self-checking
assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
assert list(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 2, 2, 2, 6, 6]
assert list(frequency_sort(["bob", "bob", "carl", "alex", "bob"])) == [
    "bob",
    "bob",
    "bob",
    "carl",
    "alex",
]
assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
assert list(frequency_sort([])) == []
assert list(frequency_sort([1])) == [1]

print("The mission is done! Click 'Check Solution' to earn rewards!")