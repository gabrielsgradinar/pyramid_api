from abc import ABC, abstractmethod
from typing import List
from pyramid.request import Request


class Repository(ABC):
    @abstractmethod
    def create(request: Request):
        ...

    @abstractmethod
    def lists() -> List:
        ...

    @abstractmethod
    def get(request: Request):
        ...

    @abstractmethod
    def update(request: Request):
        ...

    @abstractmethod
    def delete_country(request: Request):
        ...
