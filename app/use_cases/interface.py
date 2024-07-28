from abc import ABC, abstractmethod
from typing import Union


class Request:
    # TODO: need to implement a good model of request
    pass


class BaseHandler(ABC):
    def __init__(self, next_handler: Union["BaseHandler", None] = None) -> None:
        self._next_handler = next_handler

    @abstractmethod
    def handle(self, request: Request) -> Request | None:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None
