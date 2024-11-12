"""
A
B B
C C C
D D D D
E E E E E
F F F F F F
G G G G G G G
H H H H H H H H
I I I I I I I I I
J J J J J J J J J J"""
n=int(input("enter the number of rows:"))
for i in range(0,n+1):
    for j in range(0,i+1):
        print((chr(65+i))+" ",end="")
    print()
