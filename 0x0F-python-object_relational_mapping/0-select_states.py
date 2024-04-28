#!/usr/bin/python3

from mysql import connector
from sys import argv

user_n = argv[1]
passwd_ = argv[2]
db_n = argv[3]

if (__name__ == "__main__"):
    mydb = connector.connect(
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
