import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con = connector.connect(
            host='localhost',
            user='root',
            password='tiger',
            database='pythontest'
        )
        query="""create table if not exists user(id int primary key, name varchar(50),phone varchar(12))"""
        cur=self.con.cursor()
        cur.execute(query)
        print("created")

    def insert_user(self,id,name,phone):
        query="""insert into user(id,name,phone) values(%s,%s,%s)"""
        print(query)
        cur=self.con.cursor()
        cur.execute(query, (id, name, phone))
        self.con.commit()
        print("user saved to dbms")


Helper=DBHelper()
Helper.insert_user(1,'khush','123456676')
Helper.insert_user(2,'kavya','12345669870')
Helper.insert_user(3,'ravneet','123455890')
Helper.insert_user(4,'ritika','8787567890')
Helper.insert_user(5,'natasha','887656787')
Helper.insert_user(6,'palak','1234567890')