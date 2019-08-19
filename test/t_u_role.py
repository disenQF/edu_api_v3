#!/usr/bin/python3
# coding: utf-8
from mainapp import app
from models.user import User, Role, QX, user_role, db
from utils import crypt


def add_user():
    u1 = User()
    u1.phone = '17791692077'
    u1.auth_key = crypt.pwd('123456')
    u1.nick_name = 'Disen666@888'

    u2 = User()
    u2.phone = '17791692095'
    u2.auth_key = crypt.pwd('123456')
    u2.nick_name = 'Disen@888'

    db.session.add_all((u1, u2))
    db.session.commit()
    print('提交之后的User-Id:', u1.id, u2.id)


def add_role():
    r1 = Role(name='系统管理员')
    r2 = Role(name='普通用户')

    # 批量添加
    db.session.add_all((r1, r2))
    db.session.commit()
    print(r1.id, r2.id)

def add_user_role():

    # db.Table()不能作为模型类使用
    # db.session.add_all((
    #     user_role(user_id=1, role_id=1),
    #     user_role(user_id=2, role_id=1),
    #     user_role(user_id=2, role_id=2)
    # ))

    # 为用户ID为1的用户增加"系统管理员" 角色
    u = User.query.get(1)

    admin_role = Role.query.filter(Role.name.__eq__('系统管理员')).one()
    print(u.nick_name, admin_role.name)

    # 将角色对象添加给用户
    u.roles.append(admin_role)

    db.session.commit()
    print('ok')

def query_user_role(user_id=1):
    u = User.query.get(user_id)
    print('------拥有的角色-------')
    for role in u.roles:
        print(role.name)


if __name__ == '__main__':
    app.app_context().push()
    db.init_app(app)

    # add_user()
    # add_role()
    # add_user_role()
    query_user_role(1)