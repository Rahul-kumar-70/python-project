# perimeter of rectangle,circle,square,triangle by using match case
print("*"*50)
print("\tPerimeter")
print("*"*50)
print("\t\tC. circle")
print("\t\tR. Rectangle")
print("\t\tS. Square")
print("\t\tT. Triangle")
print("\t\tE. Exit")
print("*"*50)
ch=input("enter the choice:").upper()
match(ch):
    case "C" :
        r=float(input("enter the radius:"))
        print("Perimeter of Circle={}".format(2*(22/7)*r**2))
    case "R" :
        L,B=float(input("enter the lenght:")),float(input("enter the breadth:"))
        print("Perimeter of Rectangle={}".format(2*(L+B)))
    case "S":
        s=float(input("enter the side:"))
        print("Perimeter of square={}".format(4*s))
    case "T":
        b,h=float(input("enter the base:")),float(input("enter the height:"))
        print("Perimeter of Triangle={}".format(1/2*b*h))
    case "E":
        print("Thanks for using this application")
    case _:
        print("you are pressing wrong input please type valid input.")
print("progrm execution end...")