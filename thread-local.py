import threading
from threading import currentThread
from threading import get_ident
import time


class Foo:
    def __init__(self):
        self.num = 0


f = Foo()


def task(i):
    # print(time.time(), currentThread().name)
    f.num = i
    tid = get_ident()  #获取线程id
    print(tid)
    # print(f.num, time.time(), currentThread().name)
    # time.sleep(1)    # 如果此处不等待，三个线程就会分别打印，0,1,2，3 等待的话，三个进程分别就会打印最终结果，3,3,3,3
    print(f.num, time.time(), currentThread().name)

for a in range(4):
    t = threading.Thread(target=task, args=(a,))
    t.start()


print(f.num)
