from flask import Blueprint, views

order = Blueprint('B2', __name__)


@order.route('/orders')
def o1():
    print('/order path  in blueprint order')
    return 'orders path from B2-order'


@order.before_request
def o2():
    print('before func in blueprint order')


@order.after_request
def o3(x):
    print('after req in blueprint order')
    return x

