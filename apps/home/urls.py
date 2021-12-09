# -*-coding:utf-8-*-
from fastapi.routing import APIRouter

from apps.home.views import index_home



api = APIRouter()
api.add_api_route("/",index_home)

