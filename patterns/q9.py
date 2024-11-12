""" J I H G F E D C B A
    J I H G F E D C B A
    J I H G F E D C B A
    J I H G F E D C B A
    J I H G F E D C B A
    J I H G F E D C B A
    J I H G F E D C B A
    J I H G F E D C B A
    J I H G F E D C B A
    J I H G F E D C B A"""
n=int(input("enter the no of rows:"))
for i in range(n):
    for j in range(n,-1,-1):
        print((chr(65+j))+" ",end="")
    print()