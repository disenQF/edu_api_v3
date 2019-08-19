#!/usr/bin/python3
# coding: utf-8
import hashlib


def pwd(txt):
    # 将明文的txt转成md5格式的密文
    md5_ = hashlib.md5()
    md5_.update(txt.encode('utf-8'))
    md5_.update('@disen@8888#$*%'.encode('utf-8'))
    return md5_.hexdigest()


if __name__ == '__main__':
    print(pwd('000000000'))