# Create a DTO that will be transforming in-coming messages from any messaging platform
# Use it in the usecase, use it repository
from datetime import datetime
from typing import Annotated, Optional

from pydantic import BaseModel, ConfigDict, StringConstraints


class UserModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    guid: str
    is_active: bool = True
    username: Annotated[str, StringConstraints(max_length=90)]
    created_at: datetime

    profiles: Optional[list["ProfileModel"]] = None
    sessions: Optional[list["SessionModel"]] = None


class ProfileModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    learning_frequency: Annotated[str, StringConstraints(max_length=255)]
    language_region: Annotated[str, StringConstraints(max_length=255)]
    global_feedback: str
    learning_methodology: str
    created_at: datetime

    user: UserModel
    roadmaps: Optional[list["RoadmapModel"]] = None


class RoadmapModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    profile_id: int
    description: str
    created_at: datetime

    profile: ProfileModel


class InteractionModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    session_id: int
    author: Annotated[str, StringConstraints(max_length=255)]
    text: str
    platform_message_id: Annotated[str, StringConstraints(max_length=255)]
    created_at: datetime

    session: "SessionModel"


class SessionModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    description: Annotated[str, StringConstraints(max_length=255)]
    platform_channel_id: Annotated[str, StringConstraints(max_length=255)]
    created_at: datetime

    user: UserModel
    interactions: list[InteractionModel] = []


# ProfileModel.model_validate(profile_orm)
