from pydantic import BaseSettings

class AccountsServiceConfig(BaseSettings):
    transaction_service_url: str

    class Config:
        env_file = ".env"