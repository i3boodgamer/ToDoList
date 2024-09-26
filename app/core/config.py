from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, PostgresDsn


class AccessToken(BaseModel):
    path: str = "/api_v1/auth/login"
    lifetime_second: int = 3600
    reset_password_token_secret: str
    verification_token_secret: str


class ApiV1Prefix(BaseModel):
    prefix: str = "/api_v1"
    access_token_prefix: str = "/auth"
    user: str = "/user"


class ApiPrefix(BaseModel):
    v1: ApiV1Prefix = ApiV1Prefix()


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 5
    max_overflow: int = 10

    convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    }


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig
    access_token: AccessToken


settings = Settings()
