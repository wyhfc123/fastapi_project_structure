# -*-coding:utf-8-*-
import os

from typing import Union, Optional
from pydantic import AnyHttpUrl, BaseSettings, IPvAnyAddress


class Config(BaseSettings):
    # 文档地址 成产环境可以关闭 None
    DOCS_URL: Optional[str] = "/api/v1/docs"
    # # 文档关联请求数据接口 成产环境可以关闭 None
    OPENAPI_URL: Optional[str] = "/api/v1/openapi.json"
    # 禁用 redoc 文档
    REDOC_URL: Optional[str] = None

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 天
    SECRET_KEY: str = '-*&^)()sd(*A%&^aWEQaasda_asdasd*&*)(asd%$#'

    MYSQL_USERNAME: str = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD", "123456")
    MYSQL_HOST: Union[AnyHttpUrl, IPvAnyAddress] = os.getenv("MYSQL_HOST", "127.0.0.1")
    MYSQL_DATABASE: str = 'fast_api_test'

    # Mysql地址
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@" \
                              f"{MYSQL_HOST}:{3306}/{MYSQL_DATABASE}?charset=utf8mb4"
    print("mysql+pymysql://root:123456@127.0.0.1:3306/kgl")
    print(SQLALCHEMY_DATABASE_URI)

config = Config()