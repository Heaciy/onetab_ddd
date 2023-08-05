# -*- encoding: utf-8 -*-
from typing import Optional
from pydantic import BaseModel


class Link(BaseModel):
    url: str
    title: str = None
    id: Optional[str] = None
