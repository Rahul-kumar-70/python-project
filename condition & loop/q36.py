"""
Write a Python program to check if a triangle is equilateral, isosceles or scalene.
Note :
An equilateral triangle is a triangle in which all three sides are equal.
A scalene triangle is a triangle that has three unequal sides.
An isosceles triangle is a triangle with (at least) two equal sides.
Expected Output:

Input lengths of the triangle sides:
x: 6
y: 8
z: 12
Scalene triangle
"""
x,y,z=float(input("enter the 1st side:")),float(input("enter the 2nd side:")),float(input("enter the 3rd side:"))
if x==y==z:
    print("equilateral triangle")
elif x!=y!=z:
    print("scalene triangle")
else:
    print("isosceles triangle")
