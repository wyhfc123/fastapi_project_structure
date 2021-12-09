# -*-coding:utf-8-*-
from fastapi import FastAPI,Request

from docs.logger import logger


def register_middleware(app: FastAPI):
    """
    请求响应拦截 hook
    https://fastapi.tiangolo.com/tutorial/middleware/
    :param app:
    :return:
    """

    @app.middleware("http")
    async def logger_request(request: Request, call_next):
        # https://stackoverflow.com/questions/60098005/fastapi-starlette-get-client-real-ip
        logger.info(f"访问记录:{request.method} url:{request.url}\nheaders:{request.headers.get('user-agent')}"
                    f"\nIP:{request.client.host}")

        response = await call_next(request)

        return response