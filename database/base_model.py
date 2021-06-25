# -*- coding: utf-8 -*-
# @Time : 2020年11月25日 14时47分
# @Email : dsybzcf@163.com
# @Author : Hobart-CF
# @File : base_model.py
# @notice ：


from tortoise import fields
from tortoise.models import Model


class RealName(Model):
    real_name = fields.CharField(max_length=16)


class Name(Model):
    real_name = fields.CharField(max_length=16)


class Times(Model):
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

