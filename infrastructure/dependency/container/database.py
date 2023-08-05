# -*- encoding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from infrastructure.dependency.container import providers, BaseContainer


def create_engine_once(config):
    return create_engine(config["SQLALCHEMY_DATABASE_URI"])


class DatabaseContainer(BaseContainer):
    """供Repository使用"""
    # 创建数据库连接
    config = providers.Configuration()
    engine = providers.Singleton(create_engine_once, config)
    session = providers.Singleton(sessionmaker,
                                  bind=engine,
                                  expire_on_commit=False
                                  )
    # TODO: 提供session连接池
# 从数据库获取配置
# 1. 每次实例化Repository对象
# 2. 每次实例化session
