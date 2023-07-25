from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = Field(default="Changeme")
    PROJECT_VERSION: str = Field(default="Changeme")
    API_PREFIX: str = "/api"
    SECRET_KEY: str = Field(default="Changeme")
    ALGORITHM: str = Field(default="Changeme")
    POSTGRES_USER: str = Field(default="Changeme")
    POSTGRES_PASSWORD: str = Field(default="Changeme")
    POSTGRES_SERVER: str = Field(default="Changeme")
    POSTGRES_PORT: str = Field(default="5432")
    POSTGRES_DB: str = Field(default="Changeme")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @property
    def DATABASE_URL(self) -> str:
        """
        Настраиваемое свойство для формирования строки подключения
        к БД.
        :return: str - строка подключения к БД
        """
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:"
            f"{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


settings = Settings()
