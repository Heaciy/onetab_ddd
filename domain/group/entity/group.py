# -*- encoding: utf-8 -*-
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel
from domain.group.entity.vo.link import Link


class Group(BaseModel):
    id: Optional[int] = None
    name: str = None
    links: List[Link] = None
    create_time: datetime = None
    update_time: datetime = None
    device_id: int = None
    status: int = None
