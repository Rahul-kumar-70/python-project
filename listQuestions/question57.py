#Write a Python program to check if all items of a given list of strings is equal to a given string.
lst=['green','blue','red','white','black']
lst1=['green','green','green','green']
def checkItem():
    for i in lst:
        if lst[0]!=i:
            res=False
        else:
            res=True
    print(res)
    for i in lst1:
        if lst1[0]!=i:
            res=False
        else:
            res=True
    print(res)
print(lst,"\n",lst1)
checkItem()

