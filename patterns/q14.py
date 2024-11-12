"""
A
A B
A B C
A B C D
A B C D E
A B C D E F
A B C D E F G
A B C D E F G H
A B C D E F G H I
A B C D E F G H I J"""
n=int(input("enter the number of rows:"))
for i in range(0,n+1):
    for j in range(0,i+1):
        print((chr(65+j)),end=" ")
    print()