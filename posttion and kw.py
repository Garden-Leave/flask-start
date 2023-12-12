
from threading import Thread


def test(p1, kw=0, **kwargs):       # *args 参数会放进一个元祖，  **kwargs, 参数会放进一个dict, 在这里，只接受一个pos p1,
                                    # 一个默认参数，默认按位置取值，也可以kw指定，但是要放在可变参数之前

                                    # 调用时名字不和pos,def重合的kw参数，才会被放进可变参数的字典里
    print(p1, kw)

# def test(kw=0, p1, p2):   #位置参数一定要放在kw参数之前,定义和调用都要遵守，不然要报错，kw参数之间没有顺序
#     print(kw, p1, p2)     #一个参数，定义的时候如果是个位置参数，那调用可以用pos/kw方式传递值，如果定义是kw类型，一定通过kw=value来赋值
                             # 或者忽略，等于default值
#
# test()

print(test(p1=6, ))


def add(a=8, *args):   # 这里，只允许有一个pos,一个kw， a是一个默认参数，而不是kw参数， 也会按位置参数的方法传递
    print(a, args)


# add(4, a=3)  # 会报错，因为4 按照Pos方式给a一次，又发现kw，再按关键字形式给a一次，就multiple values了
# add(a=6, 8)    # 报错，调用时，pos不能放在kw方式之后，后面
add(1, 2)     # kw参数赋值也可以按位置传递




# t = Thread(target= test, args=(12, 3,))
#
# t.start()