"""
E E E E E
  D D D D
    C C C
      B B
        A
"""
n=int(input("enter the number:"))
for i in range(n,0,-1):
    print("  "*(n-i),end="")
    for j in range(n-i,n):
        print(chr(64+i)+" ",end="")
    print()