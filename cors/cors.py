# -*-coding:utf-8-*-
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def register_cors(app: FastAPI):
    """
    支持跨域
    貌似发现了一个bug
    https://github.com/tiangolo/fastapi/issues/133
    :param app:
    :return:
    """

    app.add_middleware(
        CORSMiddleware,
        # allow_origins=['http://localhost:8081'],  # 有效, 但是本地vue端口一直在变化, 接口给其他人用也不一定是这个端口
        # allow_origins=['*'],   # 无效 bug allow_origins=['http://localhost:8081']
        allow_origin_regex='https?://.*',  # 改成用正则就行了
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )