# -*- encoding: utf-8 -*-
from domain.group.entity.group import Group as GroupDo
from domain.group.repository.po.group_po import Group as GroupPo


def create_group_po(do: GroupDo):
    return GroupPo(**do.model_dump(mode="json"))
