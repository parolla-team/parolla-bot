import dataclasses

from app.domain import models as schemas
from app.infra.database import models
from app.infra.interfaces.repository import BaseRepository


@dataclasses.dataclass(kw_only=True)
class RoadmapsRepository(BaseRepository[models.Roadmap]):
    model = models.Roadmap
    schema = schemas.RoadmapModel


@dataclasses.dataclass(kw_only=True)
class UsersRepository(BaseRepository[models.User]):
    model = models.User
    schema = schemas.UserModel


@dataclasses.dataclass(kw_only=True)
class ProfilesRepository(BaseRepository[models.Profile]):
    model = models.Profile
    schema = schemas.ProfileModel


@dataclasses.dataclass(kw_only=True)
class InteractionsRepository(BaseRepository[models.Interaction]):
    model = models.Interaction
    schema = schemas.InteractionModel


@dataclasses.dataclass(kw_only=True)
class SessionsRepository(BaseRepository[models.Session]):
    model = models.Session
    schema = schemas.SessionModel
