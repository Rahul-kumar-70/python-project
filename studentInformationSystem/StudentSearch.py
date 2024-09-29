import mysql.connector as sql
def search():
    while True:
        try:
            mycon = sql.connect(user="root", password="root", host="localhost", database="student_of_Kvr")
            mycur = mycon.cursor()
            sno = int(input("enter the student Id no:"))
            q = "select * from  student where sno=%d" % ( sno)
            mycur.execute(q)
            print("-"*50)
            record=mycur.fetchone()
            if (record==None):
                print("this student details does not exist")
            else:
                print("student Id:{}".format(record[0]))
                print("Student name:{}".format(record[1]))
                print("student's Marks:{}".format(record[2]))
                print("student's College Name:{}".format(record[3]))
            print("-" * 50)
            ch = input("Do you want view to another record [Yes/No]").lower()
            if ch == "no":
                print("Thanks for using this application")
                break
        except sql.DatabaseError as db:
            print("problem in Mysql Db", db)
        except ValueError as db:
            print(db)
