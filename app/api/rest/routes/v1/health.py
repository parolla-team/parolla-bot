import logging

import sqlalchemy
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.api.schemas.types import StrDict
from app.containers import Container
from app.infra.unit_of_work.database import Uow

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get(path="/health")
@inject
async def health(uow: Uow = Depends(Provide[Container.db.container.uow])) -> StrDict:
    async with uow() as session:
        await session._session.execute(sqlalchemy.text("SELECT 1 = 1;"))
    return {"status": "alive"}


@router.get("/")
async def root() -> StrDict:
    logger.debug("DEBUG MESSAGE")
    logger.info("INFO MESSAGE")
    logger.warning("WARNING MESSAGE")
    logger.error("ERROR MESSAGE")
    # FIXME: delay doesn't exist in test_task
    # test_task.delay()
    return {"message": "Hello World!"}


@router.get("/hello/{name}")
async def say_hello(name: str) -> StrDict:
    return {"message": f"Hello {name}"}
