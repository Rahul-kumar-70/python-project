import mysql.connector as sql
def studentview():
    while True:
        try:
            mycon = sql.connect(user="root", password="root", host="localhost", database="student_of_Kvr")
            mycur = mycon.cursor()
            sno = int(input("enter the student Id no:"))
            q = "select * from  student where sno=%d" % (sno)
            mycur.execute(q)
            print("-" * 50)
            for colname in mycur.description:
                print(colname[0],end="\t")
            print()
            print("-"*50)
            record = mycur.fetchall()
            if (len(record) == 0):
                print("this student details does not exist")
            else:
                for rec in record:
                    for val in rec:
                        print("{}\t".format(val),end=" ")
                    print()
            print("-" * 50)
            ch = input("Do you want view to another record [Yes/No]").lower()
            if ch == "no":
                print("Thanks for using this application")
                break
        except sql.DatabaseError as db:
            print("problem in Mysql Db", db)
        except ValueError as db:
            print(db)
def studentviews():
    while True:
        try:
            mycon = sql.connect(user="root", password="root", host="localhost", database="student_of_Kvr")
            mycur = mycon.cursor()
            table =input("enter the table name of student_of_kvr database:")
            q = "select * from %s " % (table)
            mycur.execute(q)
            print("-" * 50)
            for colname in mycur.description:
                print(colname[0], end="\t ")
            print()
            print("-" * 50)
            record = mycur.fetchall()
            if (len(record) == 0):
                print("this student details does not exist")
            else:
                for rec in record:
                    for val in rec:
                        print("{}".format(val), end="\t ")
                    print()
            print("-" * 50)
            ch = input("Do you want view to another record [Yes/No]").lower()
            if ch == "no":
                print("Thanks for using this application")
                break
        except sql.DatabaseError as db:
            print("problem in Mysql Db", db)
        except ValueError as db:
            print(db)