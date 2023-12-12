from flask import Blueprint, views

user = Blueprint('B1', __name__)


@user.route('/users')
def u1():
    print('/user  path in blueprint user')
    return 'path users from B1:user'


@user.before_request   # 一些请求处理前后的功能，不能有返回值,  执行顺序，b1,b2,a2,a1
def b1():
    print('before req in blueprint user')


@user.before_request   # 不能有返回值
def b2():
    print('before req in blueprint user')


@user.after_request   # 必须有返回值
def a1(response):
    print('after req in blueprint user')
    return response

@user.after_request   # 必须有返回值
def a2(response):
    print('after req in blueprint user')
    return response


@user.add_app_template_global   # 把函数添加到蓝图范围内，在模板文件中调用
def u4():
    print('global f4 func  in blueprint user')


def wrap1(f):
    def inner(*args, **kwargs):
        print('deco in view')
        return f(*args, **kwargs)
    return inner


# 定义一个CBV, view
class MyView(views.MethodView):
    methods = ['GET', 'POST']   # 不定义默认允许所有method,
    decorators = [wrap1, ]             # 可以定义允许的methods和相应内容，可以为这个view添加函数作为装饰器, 给get或post方法添加功能
    def get(self):
        print('get')
        return 'get user-view from a CBV'

    def post(self):
        print('post')
        return 'post'

# app.add_url_rule('/user-view', view_func=MyView.as_view('user'))  # endpoint='user-view'