#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""
import math
def hypotenuse(a,b,c):
    if c==True:
        d=math.sqrt(a**2 + b**2)
        return int(d)
    elif c==False:
        if a>b:
            d=math.sqrt(a**2 - b**2)
            return int(d)
        else:
            d=math.sqrt(b**2 - a**2)
            return int(d)
print(hypotenuse(3,4,True))
print(hypotenuse(13,5,False))
        