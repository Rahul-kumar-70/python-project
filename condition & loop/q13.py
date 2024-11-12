""" Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its input.
 The program will print the numbers that are divisible by 5 in a comma separated sequence.
Sample Data : 0100,0011,1010,1001,1100,1001
Expected Output : 1010"""
b=input("enter the only binary number(0 and 1):")
for i in b.split(','):
    
    if int(i)%5==0:
        print(i)