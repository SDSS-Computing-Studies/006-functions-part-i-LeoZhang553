#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""
import math
def distance(tuple1,tuple2):
    L1=tuple1[0] - tuple2[0]
    L2=tuple1[1] - tuple2[1]
    L3=math.sqrt(L1**2 + L2**2)
    return L3
print(round(distance( (2,4) , (6,3)),3) )
print(round(distance( (-3,2.2) , (1,2)) , 3 ))