# -*- coding: utf-8 -*-
# @Time : 2020年11月25日 13时49分
# @Email : dsybzcf@163.com
# @Author : Hobart-CF
# @File : main.py
# @notice ：


from app import create_app
import uvicorn

apps = create_app()

if __name__ == "__main__":
    uvicorn.run(app="main:apps", host='192.168.50.125', port=8000, debug=True, reload=True)
