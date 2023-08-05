# -*- encoding: utf-8 -*-
from sqlalchemy import create_engine
from infrastructure.config import Config
from infrastructure.database import BaseModel
from domain.group.repository.po.group_po import Group  # 必须要import才能识别

if __name__ == "__main__":
    conf = Config()
    print(conf.SQLALCHEMY_DATABASE_URI)
    engine = create_engine(conf.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
    BaseModel.metadata.create_all(engine)
