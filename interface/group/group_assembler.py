# -*- encoding: utf-8 -*-
from domain.group.entity.group import Group
from interface.group.group_form import GroupForm


def to_create_do(dto: GroupForm):
    return Group(**dto.model_dump(mode="json"))
