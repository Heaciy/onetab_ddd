# -*- encoding: utf-8 -*-
import uuid as uuid_
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel
from domain.group.entity.vo.link import Link


class Group(BaseModel):
    id: Optional[int] = None
    uuid: Optional[uuid_.UUID] = None
    name: str = None
    links: List[Link] = None
    create_time: datetime = None
    update_time: datetime = None
    device_id: int = None
    status: int = None
