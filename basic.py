# a = [('a1', 'b1'), ('a2', 'b2')]
# conn, cur = a.pop()
# print(conn, cur)


'''单例模式下线程数据隔离,，不用自带的local(), 自定义一个local类 '''
from threading import get_ident, Thread
import time
from typing import TypeVar,Generic,List, Optional, Union

# 泛型理解
T = TypeVar('T', int, List)  # 定义类型变量，指定允许的三种类型
Z = Optional[str]   #意识是 NONE 或者str
U = Union[str,int]  # 其中一种


class My(Generic[T]):   # 继承Generic类型和它的getitem方法，同时MY就变成了一个泛型
    def __init__(self, a):
        self.a = a

    def f2(self):
        return self.a *2

def fun(name: My[T], num: My[str], s3: List) -> T:
    """就形成了一个静态的检查条件，第一个参数为参数类型为T的MY类型， 第二个参数为参数类型为str的MY类型
    #第三个参数为 s3是一个列表， 同时函数的返回值也需要是T中包含的一种"""

    return name + num
def f2(a: int):
    print(a)

f2('9')
print(f2)
b = My(6)

fun(b,1)

# 泛型











import functools


class Foo:
    a =90
    def __init__(self):
        print('jj')
    def sing(self,name):
        """my func explaination"""
        self.name = 'robin'
    def __call__(self, *args, **kwargs):
        print('called')
        self.b=*args[1]

f=Foo()
print(Foo.a,f.a)
f('allen')

print(Foo().method)
def f1(a,b):
    print(a, b)

f2 = functools.partial(f1,a=100)
f2(b=88)
print(Foo.a)



class Local:
    def __init__(self):
        # self.stack = []   # 此处不能这样写，会先调用setattr陷入循环调用,用父类方法创建super(类名，实例对象）
        super(Local, self).__setattr__('stack', {})

    def __setattr__(self, key, value):
        tid = get_ident()
        if tid in self.stack:
            self.stack[tid][key] = value
        else:
            self.stack[tid] = {key: value}
        
    def __getattr__(self, item):
        tid = get_ident()
        return self.stack[tid][item]

# 假设Local里没专门定义__setattr__、__getattr__但是依然可以赋值和获取，说明调用了父类object里的同名方法，如果Local里定义了但是只有pass，那么是会调用子类方法，无法赋值和取值的

loc = Local()


class Foo:
    def __init__(self):
        self.v1 = 0


f = Foo()


def task(arg):
    # loc.var = arg
    f.v1 = arg
    time.sleep(1)
    print(id(f), f.v1)


for i in range(6):
    t = Thread(target=task, args=(i, ))
    t.start()

