# app/core/config.py
from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = "QRKot"
    # Имя базы явно указано в задании, требуется для прохождения тестов
    database_url: str = "sqlite+aiosqlite:///./fastapi.db"
    secret: str = "SECRET"
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
    # Переменные для Google API
    type: Optional[str] = None
    project_id: Optional[str] = None
    private_key_id: Optional[str] = None
    private_key: Optional[str] = None
    client_email: Optional[str] = None
    client_id: Optional[str] = None
    auth_uri: Optional[str] = None
    token_uri: Optional[str] = None
    auth_provider_x509_cert_url: Optional[str] = None
    client_x509_cert_url: Optional[str] = None
    myemail: Optional[str] = None
    email: Optional[str] = None

    class Config:
        env_file = ".env"

        @classmethod
        def parse_private_key(cls, field_name: str, raw_val: str) -> str:
            if field_name == "private_key":
                return raw_val.replace("\\n", "\n")


settings = Settings()
