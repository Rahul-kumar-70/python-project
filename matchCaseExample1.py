#arthematics operator use in match case
print("*"*50)
print("\tarthematic operator")
print("*"*50)
print("\t\t1.Addition")
print("\t\t2.subtraction")
print("\t\t3.Multiplication")
print("\t\t4.Division")
print("\t\t5.Modulo Division")
print("\t\t6.exponational")
print("\t\t7.Exit")
print("*"*50)
ch=int(input("enter your choice:"))
match(ch):
    case 1:
        a,b=float(input("enter the 1st number:")),float(input("enter the 2nd number:"))
        print("Addition of ({},{})={}".format(a,b,a+b))
    case 2:
        a, b = float(input("enter the 1st number:")), float(input("enter the 2nd number:"))
        print("Subtraction of ({},{})={}".format(a, b, a-b))
    case 3:
        a, b = float(input("enter the 1st number:")), float(input("enter the 2nd number:"))
        print("Multiplication of ({},{})={}".format(a, b,a*b))
    case 4:
        a, b = float(input("enter the 1st number:")), float(input("enter the 2nd number:"))
        print("division of ({},{})={}".format(a, b, a/b))
        print("floor division of ({},{})={}".format(a, b, a//b))
    case 5:
        a, b = float(input("enter the 1st number:")), float(input("enter the 2nd number:"))
        print("Modulo Division of ({},{})={}".format(a, b,a%b))
    case 6:
        a, b = float(input("enter the base:")), float(input("enter the power:"))
        print("exponational of ({},{})={}".format(a, b,a**b))
    case 7:
        print("Thanx for using this program")
    case _:
        print(" your are pressing wrong input Please enter your valid input. ")
print("progarm executation end...")