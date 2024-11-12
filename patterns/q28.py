"""
        A
       B B
      C C C
     D D D D
    E E E E E
   F F F F F F
  G G G G G G G
 H H H H H H H H
"""
n=int(input("enter the number of u want print alphabet:"))
for i in range(1,n+1):
    if chr(65+i)!=chr(n):
        print(" "*(n-i),(chr(64+i)+" ")*i,end=" ")
    else:
        print((chr(65+i)+" ")*i)
    print()