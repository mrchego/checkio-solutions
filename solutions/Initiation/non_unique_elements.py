#!/usr/bin/env checkio --domain=py run non-unique-elements

# If you have 50 different plug types, appliances wouldn't be available and would be very        expensive. But once an electric outlet becomes standardized, many companies can design        appliances, and competition ensues, creating variety and better prices for consumers.
# -- Bill Gates
# 
# You are given a non-empty sequence of integers.    For this task, you should returnIterableconsisting of only the non-unique elements from the initial sequence. To do so you will need to remove all unique elements (elements which are contained in a given sequence only once). When solving this task, do not change the order of the elements. Example: in[1, 2, 3, 1, 3]elements1, 3are non-unique and result will be[1, 3, 1, 3].
# 
# 
# 
# Input:Listof integers(int).
# 
# Output:Listor anotherIterable(tuple,iterator,genetor) of integers(int).
# 
# 
# How it is used:This mission will help you to understand how to manipulate sequences, something that is the basis for solving more complex tasks. The concept can be easily generalized for real world tasks. For example: if you need to clarify statistics by removing low frequency elements (noise).
# 
# You can find out more about Python lists inone of our articles featuring lists, tuples, array.array and numpy.array.
# 
# Precondition:
# 0 < len(data) < 1000
# 
# 
# 
# END_DESC

from collections.abc import Iterable


def checkio(data: list[int]) -> Iterable[int]:
    # your code here
    return []


print("Example:")
print(list(checkio([1, 2, 3, 1, 3])))

# These "asserts" are used for self-checking
assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3]
assert list(checkio([1, 2, 3, 4, 5])) == []
assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5]
assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9]
assert list(checkio([2, 2, 3, 2, 2])) == [2, 2, 2, 2]
assert list(checkio([10, 20, 30, 10])) == [10, 10]
assert list(checkio([7])) == []
assert list(checkio([0, 1, 2, 3, 4, 0, 1, 2, 4])) == [0, 1, 2, 4, 0, 1, 2, 4]
assert list(checkio([99, 98, 99])) == [99, 99]
assert list(checkio([0, 0, 0, 1, 1, 100])) == [0, 0, 0, 1, 1]
assert list(checkio([0, 0, 0, -1, -1, 100])) == [0, 0, 0, -1, -1]

print("The mission is done! Click 'Check Solution' to earn rewards!")