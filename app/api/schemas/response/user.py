from datetime import datetime

from pydantic import BaseModel


class UserGetResponse(BaseModel):
    guid: str
    username: str
    platform_user_id: str
    platform_private_channel_id: str
    platform_name: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class UsersListResponse(BaseModel):
    users: list[UserGetResponse]
