from flask import render_template, request, redirect, url_for, session, signals,flash,get_flashed_messages
import functools
from flask_script import Manager
from ___init__ import create_app
import pymysql

app = create_app()
manager=Manager(app)



data_dict = {
    '1': {'name': 'jack', 'age': '28', 'city': 'NYC'},
    '2': {'name': 'bob', 'age': '18', 'city': 'SJC'},
}
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='111', db='f1')


def wrap1(f):
    def inner(*args, **kwargs):
        print('deco in view')
        return f(*args, **kwargs)
    return inner


def query_db(sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.commit()
    cursor.close()
    return result


def auth(func):          # 装饰器实现基于session的会话判断
    @functools.wraps(func)
    def inner(*args, **kwargs):
        username = session.get('jack')
        if not username:
            return redirect(url_for('lg'))
        return func(*args, **kwargs)
    return inner


@app.route('/db')
def select():
    result = query_db('select * from f1')

    return f'this is result from db:{result}'


@app.route('/login', methods=['GET', 'POST'], endpoint='lg')   # 允许多种方法
def login():
    if request.method == 'GET':     # 区分get和post请求

        return render_template('login.html')  # render
    # return jsonify({'name':'jordan', 'age':60})  JsonResponse
    id = request.form.get('id')
    city = request.form.get('city')
    if id == 'jack' and city == 'bj':
        session['jack'] = 'jack'    # 登录成功后配置一个session 名字为jack,写到客户端的cookie， 服务器默认不存
        return redirect('/index')                # 密码正确就跳转到下一个页面，redirect
    error = '用户名或密码错误啦！'
    return render_template('login.html', error=error)   # 把error msg作为变量传到Html文件里然后渲染


# @app.route('/index', endpoint='idx')
# @auth
# def index():
#     # username = session.get('jack')    # 每次收到get请求先检查是否有提交来自cookie的session信息，如果没有，username就为none，需要跳转到登录
#     # if not username:
#     #     return redirect(url_for('lg'))     # 这里return后函数结束
#
#     # return 'this is your homepage'
#     return render_template('index.html', data_dict=data_dict)   # 展示所用用户信息到html，数据源是字典


@app.route('/edit', endpoint='ed', methods=['GET', 'POST'])  # 允许post
@auth
def edit():
    id = request.args.get('nid')      # 获取从index编辑跳转过来时的id
    if request.method == 'GET':

        return render_template('edit.html', info=data_dict[id])

    # 获取post数据, 此处注意，因为是POST请求，是从form获取而不是args(多用于get)获取，容易混淆， 而且每次一个, 还可以从values获取，get和post都适用
    name = request.form.get('name')
    age = request.form.get('age')
    city = request.form.get('city')
    # v1 = request.values.get('name')
    # print(v1)
    data_dict[id] = {'name': name, 'age': age, 'city': city}  # 修改字典里的数据
    return redirect(url_for('idx'))


@app.route('/dele', endpoint='de')
def dele():
# @app.route('/dele/<int:nid>', endpoint='de')   #另一种传参数的写法，需要提前指定传过来的类型
# def dele(nid):
    id = request.args.get('nid')
    del data_dict[id]
    # return redirect('/index')
    return redirect(url_for('idx'))

@app.before_first_request
def bf1():
    pass

@app.url_value_preprocessor     #url
def uf1():
    pass



@app.before_request
def bf1():
    pass


@app.template_global()     # 在模板范围内注册全局变量，所有模板文件可直接调用被装饰的函数, 方法  {{ g1()  }}
def g1():
    return 'g1 result'


@app.template_filter()
def f1(name):
    return 'f1 result %s' % name


@signals.appcontext_pushed.connect  #利用信号来在特定节点注册自定义功能
def hook1_after_ctx_pushed(arg):
    print('hook 1', arg)


@signals.request_started.connect    #利用信号来在特定节点注册自定义功能
def hook1_after_req_started__pushed(arg):
    print('hook 2', arg)

@signals.before_render_template.connect
def f8():  # 视图函数每次渲染模板之前触发
    flash('abc')
    pass

@signals.template_rendered.connect
def f8():  # 视图函数每次渲染模板之后触发
    msg = get_flashed_messages()
    print(msg)
    pass

@manager.command    # 此时可以在命令行单独调用这个函数，把参数传给它  python3  manager.py printing jordan
def printing(name):
    print(name)

@manager.option('-n','--name',dest='name')  # 传选项   python3 manager.py speak -n roy -u www.baidu.com
@manager.option('-u','--url',dest='url')
def speak(name,url):
    print(name,url)

@app.route('/render')
def render():
    return render_template('render.html')
# 静态文件模板引用时记得  {%，  %} 百分号和花括号挨着，应该写在一起，传变量或者函数时 用{{   }}

@app.after_request
def af1():
    pass

@signals.request_finished.connect
def req_finished():
    pass


@signals.got_request_exception.connect
def except_triggered():
    pass

@app.teardown_request
def tear_down():   #auto_pop时候触发，无论请求成功或者失败都会执行的功能
    pass

@signals.appcontext_popped.connect
def poped(arg):
    pass

if __name__ == '__main__':

    manager.run()


