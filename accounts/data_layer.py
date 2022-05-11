"""Data model classes and persistence adapters
"""
from typing import Dict
from abc import ABC, abstractmethod
from pydantic import BaseModel


class Account(BaseModel):
    accountId: str
    customerId: str
    customerFirstName: str
    customerLastName: str


class UnknownAccountError(ValueError):
    """Error type when an account is not known"""
    pass


class AccountDatastore(ABC):
    """Base class for and account store, can be used for alternative backend storage"""
    @abstractmethod
    def add_account(self, account: Account) -> None:
        pass

    @abstractmethod
    def get_account(self, account_id: str) -> Account:
        pass


class InMemoryAccountDatastore(AccountDatastore):
    """An in-memory account store for local development and testing

    Warning: this data store is not persistent!
    """
    def __init__(self):
        self._accounts: Dict[str, Account] = {}

    def add_account(self, account: Account):
        self._accounts[account.accountId] = account
    
    def get_account(self, account_id: str) -> Account:
        if account_id not in self._accounts:
            raise UnknownAccountError(f"account {account_id} is not known")
        return self._accounts[account_id]
