'''Write a Python program to extend a list without append.
	Sample data: [10, 20, 30]
	[40, 50, 60]
	Expected output : [40, 50, 60, 10, 20, 30]'''
lst=[10, 20, 30]
lst1=[40, 50, 60]
lst1.extend(lst)
print(lst1)