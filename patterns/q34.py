"""
A B C D E
  A B C D
    A B C
      A B
        A
"""
n=int(input("enter the number:"))
for i in range(n):
    print("  "*(i),end="")
    for j in range(n-i):
        print(chr(65+j)+" ",end="")
    print()

