import pymysql
conn=pymysql.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="student"
)

c=conn.cursor()

c.execute("INSERT INTO STUDENT"
          "(name) values(%s)",("palak"))

conn.commit()
conn.close()
print("inserted")