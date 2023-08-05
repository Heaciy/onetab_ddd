# -*- encoding: utf-8 -*-
import uvicorn
from fastapi import FastAPI

from interface.group import group_api
from infrastructure.dependency.container.database import DatabaseContainer
from infrastructure.dependency.container.repository import RepositoryContainer
from infrastructure.dependency.container.domain import DomainContainer
from infrastructure.dependency.container.application import ApplicationContainer
from infrastructure.config import Config


def inject():
    db_container = DatabaseContainer()
    repo_container = RepositoryContainer()
    domain_container = DomainContainer()
    app_container = ApplicationContainer()
    # 挂载配置
    conf_dict = Config().model_dump(mode="json")
    db_container.config.from_dict(conf_dict)
    # TODO: 将模块路径写入配置中，然后在下面自动加载
    db_container.wire(modules=[
        "infrastructure.repository",
        "domain.group.repository",
        "domain.group.repository.implement.group_repository_implement"
    ])
    repo_container.wire(modules=[
        "domain.group.group_domain"
    ])
    domain_container.wire(modules=[
        "application.group_app"
    ])
    app_container.wire(modules=[
        "interface.group.group_api"
    ])


def main():
    inject()  # 注入变量
    app = FastAPI()
    app.include_router(group_api.router)  # TODO: 实现CBV式的注入
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == '__main__':
    main()
