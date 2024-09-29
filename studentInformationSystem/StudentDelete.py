import mysql.connector as sql
def studdelete():
    while True:
        try:
            mycon = sql.connect(user="root", password="root", host="localhost", database="student_of_Kvr")
            mycur = mycon.cursor()
            sno = int(input("enter the student Id no:"))
            q = "delete from  student where sno=%d" %( sno)
            mycur.execute(q)
            mycon.commit()
            if (mycur.rowcount > 0):
                print("{} student Record deleted from student table".format(mycur.rowcount))
            else:
                print("student Record Does not Exist")
            print("-" * 50)
            ch = input("Do you want delete to another record [Yes/No]").lower()
            if ch == "no":
                print("Thanks for using this application")
                break
        except sql.DatabaseError as db:
            print("problem in Mysql Db", db)
        except ValueError as db:
            print(db)