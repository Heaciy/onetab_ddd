# -*- encoding: utf-8 -*-
from abc import ABC, abstractmethod
from infrastructure.repository import Repository


class GroupRepository(Repository, ABC):
    """抽象接口"""
    pass

    # @abstractmethod
    # def update(self, po):
    #     raise NotImplementedError
