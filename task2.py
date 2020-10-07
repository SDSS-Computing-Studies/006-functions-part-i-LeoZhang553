#!python3
"""
##### Task 2
Create a function called largest.
The input is a list.
The return value is the largest value in the list
(2 points)
"""

def largest(List):
    List.sort()
    L=List[-1]
    return L
print(largest([3,1,4,7,13,9]))
print(largest([5,1,12.3]))