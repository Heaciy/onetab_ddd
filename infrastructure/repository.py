# -*- encoding: utf-8 -*-
from abc import ABC, abstractmethod
from contextlib import contextmanager
from sqlalchemy.orm.session import Session
from infrastructure.dependency import dependency, inject
from infrastructure.dependency.container.database import DatabaseContainer


class Repository(ABC):
    """应该是个抽象类"""

    @inject
    def __init__(self, session=dependency(DatabaseContainer.session)):
        print(session)
        self._session = session

    @contextmanager
    def session(self) -> Session:
        _session = self._session()
        try:
            yield _session
        finally:
            _session.commit()
            # _session.close()

    @abstractmethod
    def create(self, po):
        raise NotImplementedError

    # TODO: 抽象方法和非抽象方法混着来
    #  默认实现增删改查

    # TODO: 改为装饰器式的实现：@Repository
