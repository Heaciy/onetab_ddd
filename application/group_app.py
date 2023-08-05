# -*- encoding: utf-8 -*-
from domain.group.group_domain import GroupDomain
from domain.group.entity.group import Group
# from infrastructure.dependency.inject_factory import Application
from infrastructure.dependency import dependency, inject
from infrastructure.dependency.container.domain import DomainContainer


class GroupAPP:
    @inject
    def __init__(self, group_domain: GroupDomain = dependency(DomainContainer.group_domain)):
        self.group_domain = group_domain

    def create(self, group_do: Group):
        return self.group_domain.create(group_do)

# class Application:
#     pass
# class GroupAPP(Application):
#     # TODO: 根据注解自动注入
#     def __init__(self, group_domain: GroupDomain):
#         self.group_domain = group_domain
#
#     def create(self, group_do: Group):
#         return self.group_domain.create(group_do)

# TODO: 目前有三种注入方案，先尝试第一种方案
#  1. https://github.com/ets-labs/python-dependency-injector
#  2. https://github.com/python-injector/injector
#  3. https://github.com/dstanek/snake-guice
