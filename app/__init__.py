# -*- coding: utf-8 -*-
# @Time : 2020年11月25日 13时48分
# @Email : dsybzcf@163.com
# @Author : Hobart-CF
# @File : __init__.py.py
# @notice ：

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
# from app.controller.auth import Auth
# from app.controller.login import RegisterLogin
# from app.helpFunc import return_value
from route import login, user
from tortoise.contrib.fastapi import register_tortoise
# import time


def create_app():
    """Create and configure an instance of the Flask application."""
    app = FastAPI()
    app.include_router(login.route)
    app.include_router(
        user.route,
        prefix="/users",
        tags=["users"],
        responses={404: {"description": "Not found"}},
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    register_tortoise(
        app,
        config_file="database_config.json"
    )
    return app