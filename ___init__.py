from flask import Flask, render_template, jsonify, request, redirect, url_for, session, views
from Blueprint.user import user, MyView
from Blueprint.order import order
from config import settings, local_settings


def create_app():
    # static_url_path 决定了静态文件里插入的静态文件的url地址前缀，这里/static/jwt.jpg在前端url里就会体现成/xx/jwt.jpg
    # folder名字不用加/，如果不在同一级可以写，../static

    app = Flask('allen', template_folder='templates', static_folder='static', static_url_path='/xx')
    app.config.from_object(settings)

    @app.route('/')
    def root():
        return redirect('/index')

    @app.route('/index')
    def index():
        return render_template('form.html')
    app.register_blueprint(user, url_prefix='/user')   # 这里按业务模块注册蓝图就行，
    app.register_blueprint(order, url_prefix='/order')
    app.add_url_rule('/user-view', view_func=MyView.as_view('user'))  # endpoint='user-view'
    return app



