import datetime
import typing

import sqlalchemy as sa
from sqlalchemy import orm

from app.helpers import generate_utc_dt

METADATA: typing.Final = sa.MetaData()


class Base(orm.DeclarativeBase):
    metadata = METADATA


class BaseModel(Base):
    __abstract__ = True

    id: orm.Mapped[typing.Annotated[int, orm.mapped_column(primary_key=True)]]
    created_at: orm.Mapped[
        typing.Annotated[
            datetime.datetime,
            orm.mapped_column(sa.DateTime(timezone=True), default=generate_utc_dt, nullable=False),
        ]
    ]
    updated_at: orm.Mapped[
        typing.Annotated[
            datetime.datetime,
            orm.mapped_column(sa.DateTime(timezone=True), default=generate_utc_dt, nullable=False),
        ]
    ]

    def __str__(self) -> str:
        return f"<{type(self).__name__}({self.id=})>"
