# marksheet of student
while(True):
    id=input("enter the id of student:")
    if id.isdigit() and 100<=int(id)<=200:
       break
    else:
        print("{} is invalid id plz try again..".format(id))
while(True):
    name = input("enter the student name:")
    if name.replace(" ","").isalpha():
       break
    else:
        print("{} is invalid name plz try again..".format(name))
while (True):
    while (True):
        cm=input("enter the student c marks:")
        cmarks=int(cm)
        if cm.isdigit() and 100>=cmarks>0:
            break
        else:
            print("{} is invalid marks".format(cmarks))
    while (True):
        cppm = input("enter the student c++ marks:")
        cppmarks=int(cppm)
        if cppm.isdigit() and 100>=cppmarks>0:
           break
        else:
            print("{} is invalid marks".format(cppmarks))
    while (True):
        pym = input("enter the student python marks:")
        pymarks=int(pym)
        if pym.isdigit() and 100>=pymarks>0:
            break
        else:
            print("{} is invalid marks".format(pymarks))
    break
total=cmarks+cppmarks+pymarks
per=(total/300)*100
if cmarks<40 or cppmarks<40 or pymarks<40:
    grade="Fail"
else:
    if (total in range(250,301)):
        grade="DISTINCTION"
    elif (total>=200):
        grade="FIRST"
    elif (total >=150):
        grade="SECOND"
    elif (total in range(120,150)):
        grade="THIRD"
print("="*50)
print("\tS T U D E N T  R E P O R T  C A R D")
print("="*50)
print("\tRoll no of Student:",id)
print("\tName of student:",name)
print("\tMarks of c language:",cmarks)
print("\tMarks of c++ language:",cppmarks)
print("\tMarks of python language:",pymarks)
print("="*50)
print("\tGrade of student:",grade)
print("*"*50)

