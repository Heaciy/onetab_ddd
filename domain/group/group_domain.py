# -*- encoding: utf-8 -*-
from domain.group import group_factory
from domain.group.repository.group_repository import GroupRepository
from infrastructure.dependency import dependency, inject
from infrastructure.dependency.container.repository import RepositoryContainer


class Domain:
    pass


class GroupDomain(Domain):
    @inject
    def __init__(self, group_repository: GroupRepository = dependency(RepositoryContainer.group_repository)):
        self.group_repository = group_repository

    def create(self, do):
        po = group_factory.create_group_po(do)  # TODO: 为什么要多层转换
        self.group_repository.create(po)  # FIXME: po不能全局传递，在session.close()后无法获取到相关属性
        return po.id
