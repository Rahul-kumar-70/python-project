''' Write a Python program to check whether all dictionaries in a list are empty or not.
	Sample list : [{},{},{}]
	Return value : True
	Sample list : [{1,2},{},{}]
	Return value : False'''
def empty_dict_list(lst):
    for j in lst:
       if len(j)!=0:
           return False
    return True
lst1=[{},{},{}]
lst2=[{1,2},{},{}]
print(empty_dict_list(lst1))
print(empty_dict_list(lst2))
