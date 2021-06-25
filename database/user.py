# -*- coding: utf-8 -*-
# @Time : 2020年11月25日 14时58分
# @Email : dsybzcf@163.com
# @Author : Hobart-CF
# @File : user.py
# @notice ：


from tortoise import fields
from database.base_model import RealName, Times


class User(RealName, Times):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=32)
    password = fields.CharField(max_length=255)
    department_id = fields.BigIntField()
    phone = fields.CharField(max_length=16)
    mode = fields.SmallIntField()
    remember_token = fields.CharField(max_length=255)

    class Meta:
        table = "users"