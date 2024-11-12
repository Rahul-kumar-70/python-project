""" A A A A A A A A A A
    B B B B B B B B B B
    C C C C C C C C C C
    D D D D D D D D D D
    E E E E E E E E E E
    F F F F F F F F F F
    G G G G G G G G G G
    H H H H H H H H H H
    I I I I I I I I I I
    J J J J J J J J J J
"""
"""n=int(input("enter the no of rows:"))
for i in range(n):
    s=chr(65+i)+" "
    print(s*n)"""
n=int(input("enter the no of rows:"))
for i in range(n):
    for j in range(n):
        print((chr(65+i)+" "),end="")
    print()