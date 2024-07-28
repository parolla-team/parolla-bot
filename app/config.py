from pydantic import Field, PostgresDsn, RedisDsn, ValidationInfo, field_validator
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    APP_TITLE: str = Field("Parolla")
    DEBUG: bool = False
    LOG_LEVEL: str = Field(...)
    ENVIRONMENT: str = Field(...)

    POSTGRES_HOST: str = Field(...)
    POSTGRES_PORT: str = Field(...)
    POSTGRES_USER: str = Field(...)
    POSTGRES_PASSWORD: str = Field(...)
    POSTGRES_DB: str = Field(...)
    DATABASE_SCHEME: str = Field(...)
    DATABASE_URL: PostgresDsn | None = None
    DATABASE_ECHO: bool = Field(False)

    REDIS_HOST: str = Field(...)
    REDIS_PORT: str = Field(...)
    REDIS_DB: str = Field(...)
    REDIS_URL: RedisDsn | None = None

    SENTRY_DSN: str | None = Field(None)

    @field_validator("DATABASE_URL", mode="before")
    @classmethod
    def build_database_url(cls, value: str | None, values: ValidationInfo) -> str:
        if isinstance(value, str):
            return value

        return PostgresDsn.build(
            scheme=values.data.get("DATABASE_SCHEME"),
            username=values.data.get("POSTGRES_USER"),
            password=values.data.get("POSTGRES_PASSWORD"),
            host=values.data.get("POSTGRES_HOST"),
            port=int(values.data["POSTGRES_PORT"]),
            path=f"{values.data.get('POSTGRES_DB') or ''}",
        )

    @field_validator("REDIS_URL", mode="before")
    @classmethod
    def build_redis_url(cls, value: str | None, values: ValidationInfo) -> str:
        if isinstance(value, str):
            return value

        return RedisDsn.build(
            scheme="redis",
            host=values.data.get("REDIS_HOST"),
            port=int(values.data["REDIS_PORT"]),
            path=f"/{values.data.get('REDIS_DB')}",
        )


settings = Config(_env_file=".env", _env_file_encoding="utf-8")
