from pydantic import BaseModel


class UserCreateRequest(BaseModel):
    username: str
    platform_user_id: str
    platform_private_channel_id: str
    platform_name: str
    is_active: bool

    class Config:
        from_attributes = True
