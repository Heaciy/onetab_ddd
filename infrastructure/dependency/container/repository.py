# -*- encoding: utf-8 -*-
from infrastructure.dependency.container import providers, BaseContainer
from domain.group.repository.implement.group_repository_implement import GroupRepositoryImplement


class RepositoryContainer(BaseContainer):
    """供Domain使用"""
    group_repository = providers.Singleton(GroupRepositoryImplement)
