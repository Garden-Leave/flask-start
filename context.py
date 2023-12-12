

# 上下文管理，通过特殊方法来定义进入class和退出class时的返回操作，实现一些类相关的功能自动化
# 例如文件打开访问后自动关闭，数据库连接打开后自动关闭

class Boy:
    def say(self):
        print('hello')




class Context:
    def __enter__(self):
        # return 'exited'    # 返回内容就是c， 可以是对象或者方法
        return Boy()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exiting')


with Context() as c:    #  c 就是 __enter__返回的对象，这里就返回一个Boy对象了
    c.say()
