# -*- encoding: utf-8 -*-
from infrastructure.dependency.container import providers, BaseContainer
from application.group_app import GroupAPP


class ApplicationContainer(BaseContainer):
    """供Interface使用"""
    group_app = providers.Singleton(GroupAPP)
