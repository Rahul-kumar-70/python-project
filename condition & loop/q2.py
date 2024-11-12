""" Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius"""
c=float(input("enter the celsius degree:"))
f=(c*9/5)-32
print(c,chr(176),"is {} in fahrenheit".format(f))
f=float(input("enter the fahrenheit degree:"))
c=(5/9)*(f-32)
print(f,chr(176),"is {} in celsius".format(c))