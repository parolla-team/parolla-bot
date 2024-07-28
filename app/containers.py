from dependency_injector import containers, providers

from app.config import Config, settings
from app.infra.database.database import Database
from app.infra.unit_of_work.database import Uow


class DBContainer(containers.DeclarativeContainer):
    config: Config = providers.Configuration()

    db = providers.Singleton(Database, dsn=config.DATABASE_URL, echo=config.DATABASE_ECHO)
    uow = providers.Factory(Uow, session_factory=db.provided.session_factory)


class Container(containers.DeclarativeContainer):
    config: Config = providers.Configuration()
    db = providers.Container(DBContainer, config=config)

    # Create now use cases (answer to 1&1, answer to group discussion, translation, configuration profil, etc.)
    # THose use cases will be able to access database and also other infra services (like stripe, chatbot, etc.)
    # db.container.uow # This will allow use cases to access the database through the unit of work pattern


container = Container()
container.config.from_dict(settings.model_dump())
