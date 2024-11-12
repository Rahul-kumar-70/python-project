"""
1 2 3 4 5
  1 2 3 4
    1 2 3
      1 2
        1
"""
n=int(input("enter the number:"))
for i in range(n):
    print("  "*(i),end="")
    for j in range(1,n-i+1):
        print(str(j)+" ",end="")
    print()