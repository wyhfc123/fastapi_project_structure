# -*-coding:utf-8-*-
"""
使用MySql数据库
可参考官网:
https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-sqlalchemy-parts
"""



from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings.production_config import config

engine = create_engine(
    config.SQLALCHEMY_DATABASE_URI
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

'''
:key
文件迁移使用    
    1、下载包
        pip install pymysql
        pip install sqlalchemy
        pip install alembic
    2、在项目主目录下执行命令：初始化 alemibic init 迁移目录名称(只需执行一次，创建迁移文件夹)
    3、需要修改alembic.ini 文件  line 38
        # sqlalchemy.url = driver://user:pass@localhost/dbname
        sqlalchemy.url = mysql+pymysql://root:password@localhost:3306/fast_api_test
    4、需要修改env.py文件 line 20
        sys.path.append(os.getcwd())
        from models.auth.model import Base  # note: 该Base必须从表model中导入，而不能从之外的地方导入（会找不到表，迁移为空）
        target_metadata = Base.metadata
    5、执行命令：记录版本 alembic revision --autogenerate -m "提交信息"
    6、alembic upgrade  head 更新最新版本


    alembic 常用命令
        init:创建一个alembic仓库
        rebision:创建一个新的版本文件
        --autogenerate:自动将当前模型的修改，生成迁移脚本
        -m:本次迁移做了哪些修改
        upgrade:将指定版本的迁移文件映射到数据库中，会执行版本文件中的upgrade函数
        head:代表当前的迁移脚本的版本号
        downgrade:会执行指定版本的迁移文件中的downgrade函数
        heads:展示当前可用的heads脚本文件
        history:列出所有的迁移版本及其信息
        current:展示当前数据库中的版本号
'''