"""
5 5 5 5 5
  4 4 4 4
    3 3 3
      2 2
        1
"""
n=int(input("enter the number:"))
for i in range(n,0,-1):
    print("  " * (n - i),end="")
    for j in range(i):
        print(str(i)+" ",end="")
    print()
