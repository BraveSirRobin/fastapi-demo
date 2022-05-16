"""Domain model definitions and persistence adapters
"""
from uuid import uuid4
from datetime import datetime
from typing import List
from abc import ABC, abstractmethod
from pydantic import BaseModel, Field

def _uuid():
    """A wrapper to convert a UUID to a string"""
    return str(uuid4())

class Transaction(BaseModel):
    transactionId: str = Field(default_factory=_uuid)
    accountId: str
    transactionAmount: int
    transactionDate: datetime = Field(default_factory=datetime.now)

class TransactionDatastore(ABC):
    """Base class for and account store, can be used for alternative backend storage"""
    @abstractmethod
    def add_transaction(self, account: Transaction) -> None:
        pass

    @abstractmethod
    def get_transactions_for_account(self, account_id: str) -> List[Transaction]:
        pass

class InMemoryTransactionDatastore(TransactionDatastore):
    def __init__(self):
        self._transactions: list[Transaction] = []

    def add_transaction(self, transaction: Transaction):
        self._transactions.append(transaction)

    def get_transactions_for_account(self, account_id: str) -> List[Transaction]:
        return [x for x in self._transactions if x.accountId == account_id]