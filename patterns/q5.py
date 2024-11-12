""" A B C D E F G H I J
    A B C D E F G H I J
    A B C D E F G H I J
    A B C D E F G H I J
    A B C D E F G H I J
    A B C D E F G H I J
    A B C D E F G H I J
    A B C D E F G H I J
    A B C D E F G H I J
    A B C D E F G H I J"""
n=int(input("enter the no rows:"))
for i in range(n):
    for j in range(n):
        print((chr(65+j))+" ",end="")
    print()
