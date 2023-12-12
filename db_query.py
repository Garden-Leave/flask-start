from threading import Thread
from sqlhelper import db


sql = 'select * from f1.f1'

ret = db.fetchall(sql)
print(ret)


