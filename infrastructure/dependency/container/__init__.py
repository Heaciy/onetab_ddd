# -*- encoding: utf-8 -*-
from dependency_injector import providers, containers
from infrastructure.config import Config


def create_conf_once():
    config = providers.Configuration()
    config.from_pydantic(Config())


class BaseContainer(containers.DeclarativeContainer):
    """默认配置"""
    config = providers.Singleton(create_conf_once)
