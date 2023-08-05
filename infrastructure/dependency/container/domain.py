# -*- encoding: utf-8 -*-
from infrastructure.dependency.container import providers, BaseContainer
from domain.group.group_domain import GroupDomain


class DomainContainer(BaseContainer):
    """供Application使用"""
    group_domain = providers.Singleton(GroupDomain)

# TODO: 使用动态容器改造 + @domain装饰器实现
#  https://python-dependency-injector.ets-labs.org/containers/dynamic.html
