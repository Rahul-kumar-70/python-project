"""
Write a Python program to sum two integers. However, if the sum is between 15 and 20 it will return 20.
"""
def sumNum():
    a=int(input("enter the 1st no:"))
    b = int(input("enter the 2nd no:"))
    sum=a+b
    if 15<=sum<=20:
        return 20
    else:
        print("not between 15 and 20")
res=sumNum()
print(res)