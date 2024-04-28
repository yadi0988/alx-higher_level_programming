#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa."""


import MySQLdb
from sys import argv

user_n = argv[1]
passwd_ = argv[2]
db_n = argv[3]

if (__name__ == "__main__"):
    mydb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user_n,
        passwd=passwd_,
        db=db_n
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM states ORDER BY id")

    result = mycursor.fetchall()
    for row in result:
        print(row)

    mycursor.close()
    mydb.close()
