"""Types which define the input/output of the API"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class NewTransactionInput(BaseModel):
    accountId: str
    transactionAmount: int

class TransactionDetail(BaseModel):
    transactionId: str
    transactionAmount: int
    transactionDate: datetime
