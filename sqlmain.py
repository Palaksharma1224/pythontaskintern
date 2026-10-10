import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="tiger",   
    database="students",
    port=3306
)