"""
J I H G F E D C B A
J I H G F E D C B
J I H G F E D C
J I H G F E D
J I H G F E
J I H G F
J I H G
J I H
J I
J
"""
n=int(input("enter the number of rows:"))
for i in range(n+1):
    for j in range(n,i-1,-1):
        s=chr(65+j)+" "
        print(s,end="")
    print()