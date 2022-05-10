import os
from uuid import uuid4
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NewAccountInput(BaseModel):
    customerId: str
    customerFirstName: str
    customerLastName: str
    openingBalancePence: Optional[int]

class NewAccountOutput(BaseModel):
    customerId: str
    accountId: str

class AccountDatabase:
    def __init__(self):
        self._accounts = {}
    
    def add_account(self, account_detail: NewAccountInput) -> str:
        account_id = str(uuid4())
        self._accounts[account_id] = account_detail
        return account_id

AccountDB = AccountDatabase()

@app.post("/open")
async def open(new_ac_detail: NewAccountInput) -> NewAccountOutput:
    account_id = AccountDB.add_account(new_ac_detail)
    return NewAccountOutput(
        customerId=new_ac_detail.customerId,
        accountId=account_id
    )