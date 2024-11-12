"""
Write a Python program to calculate a dog's age in dog years.
Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
Expected Output:

Input a dog's age in human years: 15
The dog's age in dog's years is 73
"""
h=int(input("Input a dog's age in human years: "))
if h>2:
    a=h-2
    d=a*4+2*10.5
    print("The dog's age in dog's years is :",d)
else:
    print("The dog's age in dog's years is:",h*10.5)