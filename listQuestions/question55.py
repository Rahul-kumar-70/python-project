#Write a Python program to remove key values pairs from a list of dictionaries.
lst=[{1:'python',2:'html'},{3:'css',4:'js'}]
for i in range(0,len(lst)):
    print(lst[i].remove(i[0]),end=" ")


