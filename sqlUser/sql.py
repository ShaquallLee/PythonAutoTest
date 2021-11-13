'''
Descripttion: pymysql库的使用
Author: lishaogang
version: 
Date: 2021-11-09 12:13:33
LastEditors: lishaogang
LastEditTime: 2021-11-09 14:15:33
'''

import pymysql

link = pymysql.connect(host="localhost", user="root",
                       passwd="lishao123", database="test")

cursor = link.cursor()

cursor.execute(
    "insert into students(id, name,cid) values(13,'jone', 2);"
)
link.commit()

res_len = cursor.execute(
    "select * from students;"
)

for i in range(res_len):
    print(cursor.fetchone())

link.close()
print("end")
