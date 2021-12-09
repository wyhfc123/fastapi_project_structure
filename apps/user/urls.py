# -*-coding:utf-8-*-
from fastapi.routing import APIRouter

from apps.user.views import login





api = APIRouter()
api.add_api_route("/login",login)