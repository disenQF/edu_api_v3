#!/usr/bin/python3
# coding: utf-8
from flask import render_template, request, redirect, url_for

from mainapp import app
from mainapp.views import user_v
from flask_script import Manager
from models.user import db, User
from utils import cache


@app.before_request
def check_login():
    if request.path != '/user/login':

        # 判断request中是否包含token
        # 验证token是否有效
        token = request.cookies.get('token')
        if not token:
            return redirect(url_for('userBlue.login'))
        else:
            user_id = cache.get_user_id(token)
            if not user_id:
                return redirect(url_for('userBlue.login'))


@app.route('/')
def index():
    # 获取用户登录的信息
    token = request.cookies.get('token')
    user_id = cache.get_user_id(token)
    user = User.query.get(int(user_id))

    return render_template('index.html', user=user)


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
