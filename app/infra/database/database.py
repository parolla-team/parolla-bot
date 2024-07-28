import json
from collections.abc import Callable
from typing import Any

import orjson
from pydantic import PostgresDsn
from pydantic.v1.json import pydantic_encoder
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)


def json_dumps(value: Any, *, default: Callable[[Any], Any] = pydantic_encoder) -> str:  # noqa: ANN401
    return json.dumps(value, default=default)


class Database:
    def __init__(self, dsn: PostgresDsn, echo: bool = False) -> None:
        self._engine: AsyncEngine = create_async_engine(
            url=str(dsn),
            json_serializer=json_dumps,
            json_deserializer=orjson.loads,
            echo=echo,
        )
        self._session_factory = async_sessionmaker(bind=self._engine, expire_on_commit=False)

    @property
    def engine(self) -> AsyncEngine:
        return self._engine

    @property
    def session_factory(self) -> async_sessionmaker[AsyncSession]:
        return self._session_factory
