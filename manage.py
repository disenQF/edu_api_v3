#!/usr/bin/python3
# coding: utf-8
from flask import render_template

from mainapp import app
from mainapp.views import user_v
from flask_script import Manager
from models.user import db


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create_db')
def create_database():
    db.create_all()
    return "创建数据库中的所有模型表成功"


@app.route('/drop_db')
def drop_database():
    db.drop_all()
    return "删除库中所有模型类对应的表"


if __name__ == '__main__':
    # 将蓝图注册到app中
    app.register_blueprint(user_v.blue, url_prefix='/user')

    # 初始化数据库
    db.init_app(app)

    manager = Manager(app)
    manager.run()
