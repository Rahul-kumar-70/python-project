from studentMenu import menu
from StudentInsert import insertRecord
from StudentUpdate import studupdate
from StudentDelete import studdelete
from StudentViews import studentviews,studentview
from StudentSearch import search

while True:
    menu()
    try:
        ch = int(input("choose your choice:"))
        match (ch):
            case 1:
                insertRecord()
            case 2:
                studentview()
            case 3:
                studentviews()
            case 4:
                search()
            case 5:
                studupdate()
            case 6:
                studdelete()
            case 7:
                print("Thanx for using this application")
                break
            case _:
                print("Please enter the valid option")
    except ValueError as v:
        print(v)
