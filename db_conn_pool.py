
import pymysql
from dbutils.pooled_db import PooledDB
from threading import Thread

pool = PooledDB(
    creator=pymysql,
    maxconnections=30,
    mincached=2,
    blocking=True,
    ping=0,
    host='127.0.0.1',
    port=3306,
    user='root',
    password='111',
    database='f1',
    # charset='utf-8'
)

# 取一个连接　
#
# sql = 'select * from f1'
# conn = pool.connection()   # 从连接池拿到一个连接
# cursor = conn.cursor()    # 获取游标
# cursor.execute(sql)      # 执行一个sql
# ret = cursor.fetchall()     # 从游标取结果
# cursor.close()       # 关闭游标
# print(ret)
# conn.close()    # 将连接返还到连接池中

# 用多线程模拟请求，发现每次最多同时创建的连接是定义的6个


def task(num):
    sql = 'select * from f1.f1'
    conn = pool.connection()  # 从连接池拿到一个连接
    cursor = conn.cursor()  # 获取游标
    cursor.execute(sql)  # 执行一个sql
    ret = cursor.fetchall()  # 从游标取结果
    cursor.close()  # 关闭游标

    conn.close()  # 将连接返还到连接池中
    print( ret)

#
# for i in range(20):
#     t = Thread(target=task, args=(i,))   # i 会作为参数传到target=task
#     t.start()

task(1)