# # -*- encoding: utf-8 -*-
# from sqlalchemy import MetaData
# from sqlalchemy.orm import DeclarativeBase
#
#
# class BaseModel(DeclarativeBase):
#     __abstract__ = True
#     metadata = MetaData(schema="onetab")

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    __table_args__ = {'schema': 'onetab'}
