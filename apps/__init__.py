# -*-coding:utf-8-*-



from fastapi import FastAPI, APIRouter

from apps.home.urls import api as home_api

from apps.user.urls import api as user_api
from cors.cors import register_cors
from execption.exception import register_exception
from intercept.intercept import register_middleware
from settings.production_config import config

tags_metadata = [
    {
        "name": "首页API",
        "description": "商品首页数据API",
    },
]

apis = APIRouter(prefix="/api/v1")
#include_router 可以包含各个子模块路由   (可以在apps下再加一层目录，将总路由添加到新加的目录当中)
apis.include_router(home_api,tags=[""])
apis.include_router(user_api,tags=[""])

def create_app():
    app = FastAPI(
        title="FastAPI",
        description="aaa",
        version="0.1.1",
        docs_url=config.DOCS_URL,
        openapi_url=config.OPENAPI_URL,
        redoc_url=config.REDOC_URL,
        openapi_tags=tags_metadata,
    )

    app.include_router(apis)
    register_exception(app)
    register_cors(app)
    register_middleware(app)
    return app



