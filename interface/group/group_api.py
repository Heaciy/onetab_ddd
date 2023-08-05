# -*- encoding: utf-8 -*-
from fastapi import APIRouter
from fastapi import UploadFile

from application.group_app import GroupAPP
from interface.group.group_form import GroupForm, QueryForm
from interface.group.group_assembler import to_create_do
from infrastructure.api import api, Router
from infrastructure.dependency import dependency, inject
from infrastructure.dependency.container.application import ApplicationContainer

#
# class Api:
#     pass


# TODO: 实现CBV 支持异步 封装全局的异常处理和日志处理(注意日志的级别)
# FIXME: 事务处理在哪一层？

router = Router(prefix="/group")


@api(router)
class GroupAPI:
    @inject
    def __init__(self, group_app: GroupAPP = dependency(ApplicationContainer.group_app)):
        self.group_app = group_app
        # TODO: 能否在这儿进行全局的session的传递 装饰器 or 注入
        # self.seeion

    @router.post("/create")
    def create(self, group: GroupForm):
        do = to_create_do(group)
        data = self.group_app.create(do)
        return data

    @router.post("/query")
    def query(self, query: QueryForm):
        # 1. 只按时间查group - 默认列表
        # 2. 查询API 只查API 查API关联group时是否带上所有的API 时间顺序
        # 3. 按照数量查 - 按照时间查
        pass

    @router.post("/import")
    def import_(self, file: UploadFile):
        # TODO: 文件处理
        pass

# FIXME: 代码重复转换是个大问题
