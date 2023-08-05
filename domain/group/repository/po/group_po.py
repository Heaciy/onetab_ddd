# -*- encoding: utf-8 -*-
from sqlalchemy import Column, Text, JSON, DateTime, BigInteger, SmallInteger
from infrastructure.database import BaseModel


# 定义模型
class Group(BaseModel):
    __tablename__ = 'group'
    id = Column(BigInteger, primary_key=True)
    name = Column(Text)
    links = Column(JSON)
    create_time = Column(DateTime)
    update_time = Column(DateTime)
    device_id = Column(BigInteger)
    status = Column(SmallInteger)
