from abc import ABCMeta,abstractmethod


class Boy(metaclass=abc):

    city = 'bj'

    def __init__(self, age):
        self.age = age

    @staticmethod     # 不需要传入实例对象或者类对象，可以直接调用
    def say():
        print('人物已创建')

    @property       # 把一个方法属性化
    def age_check(self):
        if not self.age > 18:
            print('false')

    @property
    def span(self):
        s = self.age - 18
        # print('您已成年%s年' % s)
        # print('您已经成年{}年了'.format(s))
        print(f"您已经成年{s}年啦")

    @classmethod     # 修改类属性，以后新的实例会按新的city初始化,第一个参数是cls, 第二个是位参
    def update_class(cls, city):
        Boy.city = city

    @abstractmethod    # 定义抽象方法
    def speak(self):
        pass
#
# Boy.say()
# b.say()
# b.span
# b.age_check


b = Boy(66)
print(b.city)
b.update_class('shang')
c = Boy(32)
print(c.city, c.age)




