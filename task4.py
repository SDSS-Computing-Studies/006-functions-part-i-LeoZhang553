#! python3
"""
Create a function called isInteger()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)
"""

def isInteger(a):
    a=float(a)
    if float(a)==int(a):
        return True
    else:
        return False
print(isInteger(9.5))
print(isInteger(-2))


    