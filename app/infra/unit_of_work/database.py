import logging
from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.infra.database import repositories

logger = logging.getLogger(__name__)


class IUnitOfWork(ABC):
    _session: AsyncSession
    roadmaps: repositories.RoadmapsRepository
    users: repositories.UsersRepository
    profiles: repositories.ProfilesRepository
    interactions: repositories.InteractionsRepository
    sessions: repositories.SessionsRepository

    def __call__(self, autocommit: bool = False, *args, **kwargs) -> "IUnitOfWork":
        self._autocommit = autocommit

        return self

    async def __aenter__(self) -> "IUnitOfWork":
        return self  # pragma: no cover

    async def __aexit__(self, exc_type: type[BaseException] | None, *args, **kwargs) -> None:
        if exc_type is not None:
            await self.rollback()
        else:
            if self._autocommit:
                await self.commit()

        await self.shutdown()

    @abstractmethod
    async def commit(self) -> None:
        ...

    @abstractmethod
    async def rollback(self) -> None:
        ...

    @abstractmethod
    async def shutdown(self) -> None:
        ...


class Uow(IUnitOfWork):
    """
    Provides a unit of work pattern for managing transactions and repositories in
    an asynchronous SQLAlchemy session.
    """

    def __init__(self, session_factory: async_sessionmaker[AsyncSession]) -> None:
        self.roadmaps = repositories.RoadmapsRepository(session=session_factory())
        self.users = repositories.UsersRepository(session=session_factory())
        self.profiles = repositories.ProfilesRepository(session=session_factory())
        self.interactions = repositories.InteractionsRepository(session=session_factory())
        self.sessions = repositories.SessionsRepository(session=session_factory())
        self._session_factory = session_factory

    async def __aenter__(self) -> IUnitOfWork:
        self._session = self._session_factory()

        return await super().__aenter__()

    async def commit(self) -> None:
        """Commits the changes made in the session."""

        await self._session.commit()

    async def rollback(self) -> None:
        """Rolls back the changes made in the session."""

        await self._session.rollback()

    async def shutdown(self) -> None:
        """Closes the session."""

        await self._session.close()
