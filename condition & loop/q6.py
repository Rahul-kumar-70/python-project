"""Write a Python program to count the number of even and odd numbers in a series of numbers
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4"""
n=(1, 2, 3, 4, 5, 6, 7, 8, 9,10,12)
even=0
odd=0
for i in n:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Number of even numbers :",even)
print("Number of odd numbers : ",odd)