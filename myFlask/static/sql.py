'''
Descripttion: 
Author: lishaogang
version: 
Date: 2021-11-18 16:43:57
LastEditors: lishaogang
LastEditTime: 2021-11-18 16:57:36
'''
import pymysql

def sql4login(user, pwd):
    conn = pymysql.connect(
        host='localhost',
        user='root',password='lishao123',
        database='systest',
        charset='utf8')
 
    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    # 得到一个可以执行SQL语句并且将结果作为字典返回的游标
    #cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    

    # 执行SQL语句
    sql="select * from users where account=%s and password=%s" #%s需要去掉引号，pymysql会自动加上
    
    res=cursor.execute(sql,[user,pwd])
    #使用fetall()获取全部数据
    # data = cursor.fetchall()
    # 关闭光标对象
    cursor.close()
    
    # 关闭数据库连接
    conn.close()
    return res#, data

if __name__ == '__main__':
    res = sql4login('lishao','12345')
    print(res)