from uuid import uuid4

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infra.database.base import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    guid: Mapped[str] = mapped_column(String, nullable=False, default=str(uuid4()))
    platform_user_id: Mapped[str] = mapped_column(String(255))
    platform_private_channel_id: Mapped[str] = mapped_column(String(255))
    platform_name: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(default=True)
    username: Mapped[str | None] = mapped_column(String(90), nullable=False)

    profiles = relationship("Profile", back_populates="user")
    sessions = relationship("Session", back_populates="user")


class Profile(BaseModel):
    __tablename__ = "profiles"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    learning_frequency: Mapped[str] = mapped_column(String(255), nullable=False)
    language_region: Mapped[str] = mapped_column(String(255), nullable=False)
    global_feedback: Mapped[str] = mapped_column(Text, nullable=False)
    learning_methodology: Mapped[str] = mapped_column(Text, nullable=False)

    user = relationship("User", back_populates="profiles")
    roadmaps = relationship("Roadmap", back_populates="profile")


class Roadmap(BaseModel):
    __tablename__ = "roadmaps"

    profile_id: Mapped[int] = mapped_column(ForeignKey("profiles.id"), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)

    profile = relationship("Profile", back_populates="roadmaps")


class Session(BaseModel):
    __tablename__ = "sessions"

    guid: Mapped[str] = mapped_column(String, nullable=False, default=str(uuid4()))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    platform_channel_id: Mapped[str] = mapped_column(String(255), nullable=False)

    user = relationship("User", back_populates="sessions")
    interactions = relationship("Interaction", back_populates="session")


class Interaction(BaseModel):
    __tablename__ = "interactions"

    session_id: Mapped[int] = mapped_column(ForeignKey("sessions.id"), nullable=False)
    author: Mapped[str] = mapped_column(String(255), nullable=False)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    platform_message_id: Mapped[str] = mapped_column(String(255), nullable=False)

    session = relationship("Session", back_populates="interactions")
