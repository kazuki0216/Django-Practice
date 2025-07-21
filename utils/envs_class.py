from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvSettings(BaseSettings):
    db_name: str
    db_user: str
    db_password: str
    db_port: str
    db_host: str
    model_config = SettingsConfigDict(env_file=".env")
