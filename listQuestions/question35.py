'''Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
	Sample list : ['p', 'q']
	n =5
	Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']'''
n=int(input("enter the number how many you want to print concatenating of string and number:"))
lst=['p','q']
for i in range(1,n+1):
    for j in lst:
        print(j+str(i),end=" ")

