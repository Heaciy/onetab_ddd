# -*- encoding: utf-8 -*-
from fastapi import Depends
from dependency_injector.wiring import Provide, inject


def dependency(provider):
    return Depends(Provide[provider])
