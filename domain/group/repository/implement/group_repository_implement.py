# -*- encoding: utf-8 -*-
from domain.group.repository.group_repository import GroupRepository
from domain.group.repository.po.group_po import Group


class GroupRepositoryImplement(GroupRepository):
    """具体实现"""

    def create(self, po: Group):
        with self.session() as session:
            session.add(po)
            return po
        # FIXME: session没有close
        # TODO: 实现异步连接池
        # TODO: 在接口层实现UOW的注入，UOW包括session和traceid，前后全局传递

# class GroupRepository(ABC):
#     @abstractmethod
#     def craete(self, po):
#         raise NotImplementedError

# FIXME: 1. 每次实例化session 2.每次实例化repository
