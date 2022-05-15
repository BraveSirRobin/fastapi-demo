from datetime import datetime
from typing import Optional, List
"""Types which define the input/output of the API"""
from pydantic import BaseModel, validator

class TransactionDetail(BaseModel):
    transactionId: str
    transactionAmount: int
    transactionDate: datetime

class NewAccountInput(BaseModel):
    customerId: str
    customerFirstName: str
    customerLastName: str
    openingBalance: Optional[int] = 0

    @validator("openingBalance")
    def not_negative(cls, val):
        if val < 0:
            raise ValueError("opening balance cannot be negative")
        return val

class NewAccountOutput(BaseModel):
    customerId: str
    accountId: str
    openingBalanceTransaction: Optional[TransactionDetail]
    faultMessage: Optional[str]

class AccountDetails(BaseModel):
    customerId: str
    customerFirstName: str
    customerLastName: str
    balance: Optional[int]
    transactions: Optional[List[TransactionDetail]]
    faultMessage: Optional[str]