""" J J J J J J J J J J
    I I I I I I I I I I
    H H H H H H H H H H
    G G G G G G G G G G
    F F F F F F F F F F
    E E E E E E E E E E
    D D D D D D D D D D
    C C C C C C C C C C
    B B B B B B B B B B
    A A A A A A A A A A"""
n=int(input("enter of the no of rows:"))
for i in range(n,-1,-1):
    s=(chr(65+i))+" "
    print(s*n)