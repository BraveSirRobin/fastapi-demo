"""Configuration for the accounts service.  Pydantic supports env files and environment variables for config values.
"""
from pydantic import BaseSettings

class AccountsServiceConfig(BaseSettings):
    transaction_service_url: str

    class Config:
        env_file = ".env"