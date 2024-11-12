"""
A A A A A A A A A A
B B B B B B B B B
C C C C C C C C
D D D D D D D
E E E E E E
F F F F F
G G G G
H H H
I I
J
"""
n=int(input("enter the number of rows:"))
for i in range(n):
    s=chr(65+i)+" "
    print(s*(n-i))
