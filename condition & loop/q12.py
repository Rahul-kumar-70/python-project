""" Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints
the lines as output (all characters in lower case)."""
lst=[]
while True:
    s=input("enter the string:")
    if s:
        lst.append(s.upper())
    else:
        break
for ch in lst:
    print(ch)
