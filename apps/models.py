# -*-coding:utf-8-*-
from sqlalchemy import Column, Integer,String,Boolean

from database.connect import Base


class UserInfo(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(128), unique=True, index=True)
    hashed_password = Column(String(128),nullable=True)
    is_active = Column(Boolean, default=True)