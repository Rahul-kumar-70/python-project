"""
A B C D E F G H I J
A B C D E F G H I
A B C D E F G H
A B C D E F G
A B C D E F
A B C D E
A B C D
A B C
A B
A
"""
n=int(input("enter the number of rows:"))
for i in range(n):
    for j in range(0,n-i):
        print((chr(65+j))+" ",end="")
    print()