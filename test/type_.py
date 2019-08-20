#!/usr/bin/python3
# coding: utf-8
"""
Python中的元类
1. type
2. metaclass
"""

# class User():
#     def say(self, txt):
#         print('hi, %s' % txt)
#


# type(class_name, bases, attrs)
# class_name 类名，
# bases 类的继承的父类， 是元组类, 空元组 ()
# attrs 类的属性成员（方法和属性）， 是字典类型
User = type('User', (), {
    'say': lambda self, msg: 'hi, %s' % msg
})

u = User()
print(u.say('jack'))

"""
 type 元类实现类的ORM映射
 
 Person()
    id = Column(String, max_length=20)
    name = Column(String, max_length=20)
    
    
 create table table_name(field_name field_type...)
 
"""

class BaseField():
    pass

class CharField(BaseField):
    def __init__(self, length):
        self.length = length

class IntField(BaseField):
    pass

class BaseModelMeta(type):
    def __new__(cls, name, bases, attrs):
        print('--BaseModelMeta--', name)
        print('--BaseModelMeta--', bases)
        print('--BaseModelMeta--', attrs)

        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)

        fields = { }
        for key, field in attrs.items():
            if isinstance(field, BaseField):
                fields[key] = field

        table = attrs.get('__tablename__', name.lower())

        attrs['fields'] = fields
        attrs['table'] = table

        return type.__new__(cls, name, bases, attrs)


class Model(metaclass=BaseModelMeta):
    def create(self):
        print('---create--')

        sql = "create table %s(%s)"
        table_name = self.table
        columns = ['%s %s' % (key, 'varchar(%s)'% field.length if isinstance(field, CharField) else 'Integer')
                   for key, field in self.fields.items() ]

        sql = sql % (table_name, ','.join(columns))
        print(sql)

    def save(self):
        pass
    def delete(self):
        pass
    def query(self):
        pass

class Person(Model):
    __tablename__ = 't_person'

    id = IntField()
    name = CharField(50)
    city = CharField(20)


p = Person()
p.create()



