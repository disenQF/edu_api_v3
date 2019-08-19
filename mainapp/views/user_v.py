#!/usr/bin/python3
# coding: utf-8
import uuid
from datetime import datetime, timedelta

from flask import Blueprint, make_response, redirect
from flask import request, render_template
from models.user import User
from utils import crypt, cache

blue = Blueprint('userBlue', __name__)


@blue.route('/logout', methods=['GET'])
def logout():

    # 删除redis中token
    token = request.cookies.get('token')
    cache.clear_token(token)

    # 删除cookie
    resp = redirect('/user/login')
    resp.delete_cookie('token')

    return resp



@blue.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        phone = request.form.get('phone')
        passwd = request.form.get('passwd')

        login_user = User.query.filter(User.phone == phone,
                                       User.auth_key == crypt.pwd(passwd)).one()
        if login_user:
            # 登录成功
            # 生成token
            token = uuid.uuid4().hex
            resp = redirect('/')
            resp.set_cookie('token', token, expires=(datetime.now()+timedelta(days=3)))

            # 将token添加到redis, token-user_id
            cache.save_token(token, login_user.id)
            return resp
        else:
            message = '查无此用户'

    return render_template('user/login.html', msg=message)
