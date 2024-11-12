# Write a Python function that takes two lists and returns True if they have at least one common member.
lst1=['python','guido','van',1,4,7]
lst2=['roussom',1,4,6,8]
def checklist(lst1,lst2):
    for i in lst1:
        for i in lst2:
            return True
            break
        return False
ress=checklist(lst1,lst2)
print(ress)
