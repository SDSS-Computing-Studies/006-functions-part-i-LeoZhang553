#!python3
"""
NOTE:
If you complete this extension, call your teacher over to have it assessed


Create a program to determine the solutions for a quadratic equation
in the format ax^2 + bx + c = 0
A key is the discriminant: b^2 - 4 * a * c
If the discriminant is negative, there are no solutions
If the discriminant is zero, there is only 1 solution
If the discriminant is positive, there are 2 solutions

If the discriminant is a perfect square, then the equation can
be factored

If the discriminant is non zero, the solutions are:
x = (-b + sqrt(b^2 - 4 * a * c)) / 2a
x = (-b - sqrt(b^2 - 4 * a * c)) / 2a

Assignment criteria:
Create a program that inputs 3 float values: a, b, c
function numSolutions(a,b,c) returns an integer with the number of solutions
function solutions(a,b,c) returns a tuple with the solutions (note that if 1 solution,
then both solutions will be the same)

If there are no solutions:
output is: "There are no real solutions"

If there is one solution:
output is "There is 1 solution, x=??"

If there are two solutions:
output is: "The solutions are x=?? and x=??"
"""
import math
def numSolutions(a,b,c):
    # inputs:
    # float a
    # float b
    # float c
    # Description:
    #
    # return 0, 1 or 2
    d=b**2 - 4*a*c
    if d < 0:
        return 0
    elif d == 0:
        return 1
    else:
        return 2
    

def solutions(a,b,c):
    #inputs:
    # float a
    # float b
    # float c
    # Desription:
    #
    # return tuple of float solution1 and float solution2
    ListX=[]
    x=numSolutions(a,b,c)
    if x == 0:
        return 0
    elif x == 1:
        x1 = (-b + math.sqrt(b*2 - 4 * a * c)) / (2*a)
        x2 = (-b - math.sqrt(b*2 - 4 * a * c)) / (2*a)
        ListX.append(x1)
        ListX.append(x2)
        return ListX[0]
    elif x == 2:
        x1 = (-b + math.sqrt(b*2 - 4 * a * c)) / (2*a)
        x2 = (-b - math.sqrt(b*2 - 4 * a * c)) / (2*a)
        ListX.append(x1)
        ListX.append(x2)
        return ListX[0], ListX[1]

def title(a,b,c):
    # inputs none
    # return str of All the title and instructions on one line
    x=numSolutions(a,b,c)
    if x == 0:
        a='There are no real solutions'
    elif x == 1:
        a='There is 1 solution, x='
    elif x == 2:
        a="The solutions are"
    return a

def main():
    # Display Title and Instructions
    print( title(1,2,1) )
    # Your code and function calls should go here
    # do input 3 numbers
    # check the number of solutions

    # if solutions is > 0
    # find the solutions
    # display results
    if x == 0:
        print('There are no real solutions')
    elif x == 1:
        a=('There is 1 solution, x='
    elif x == 2:
        a="The solutions are"
    return a

main()