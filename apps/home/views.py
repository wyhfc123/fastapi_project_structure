# -*-coding:utf-8-*-
from apps.models import UserInfo
from database.connect import get_db


async def index_home():
    #调用生成器
    res = next(get_db()).query(UserInfo).filter(UserInfo.id == 1).first()
    return {"message":"Hello World"}