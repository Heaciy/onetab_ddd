# -*- encoding: utf-8 -*-
from typing import List
from datetime import datetime

import shortuuid
from pydantic import Field, AnyUrl, BaseModel


class Link(BaseModel):
    # TODO: 处于安全应该对长度进行限制
    url: AnyUrl = Field(strict=False)
    title: str = Field(max_length=255)
    id: str = Field(default_factory=shortuuid.uuid)


class GroupForm(BaseModel):
    id: int = None
    name: str = None
    links: List[Link] = None
    create_time: datetime = None
    update_time: datetime = None
    device_id: int = None
    status: int = None


class QueryForm(BaseModel):
    start_time: datetime = None
    end_time: datetime = None
    order: str = None  # desc/asc
    limit: int = None  # 返回的Group数量
    # page_index: int = None
    # page_size: int = None
