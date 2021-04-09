#!/usr/bin/env python
# coding=utf-8

from flask import Flask

# 初始化
app = Flask(__name__)

# 路由

@app.route('/')
def index():
    return "index page!"

# <name>对应函数中的参数
@app.route('/user/<name>')
def user(name):
    return "hello{}".format(name)

if __name__=='__main__':
    # app.run(port=8080,host=127.0.0.1)
    app.run()
