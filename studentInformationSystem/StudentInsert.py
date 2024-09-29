import mysql.connector as sql
def insertRecord():
    while True:
        try:
            mycon=sql.connect(user="root",password="root",host="localhost",database="student_of_Kvr")
            mycur=mycon.cursor()
            sno=int(input("enter the student Id no:"))
            name=input("enter the student name:")
            marks=float(input("enter the marks of student:"))
            colname=input("enter the college name:")
            q="insert into student values(%d,'%s',%f,'%s')"%(sno,name,marks,colname)
            mycur.execute(q)
            mycon.commit()
            print("-"*50)
            print("{} row record saved".format(mycur.rowcount))
            print("-" * 50)
            ch=input("Do you want insert to another record [Yes/No]").lower()
            if ch=="no":
                print("Thanks for using this application")
                break
        except sql.DatabaseError as  db:
            print("problem in Mysql Db",db)
        except ValueError as db:
            print(db)
