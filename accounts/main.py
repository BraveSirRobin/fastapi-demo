import os
from uuid import uuid4
from fastapi import FastAPI

from .service_types import NewAccountInput, NewAccountOutput
from .data_layer import InMemoryAccountDatastore, Account

app = FastAPI()

AccountDS = InMemoryAccountDatastore()

@app.post("/open")
async def open(new_ac_detail: NewAccountInput) -> NewAccountOutput:
    account: Account = Account(
        accountId=str(uuid4()),
        customerId=new_ac_detail.customerId,
        customerFirstName=new_ac_detail.customerFirstName,
        customerLastName=new_ac_detail.customerLastName
    )
    account_id = AccountDS.add_account(account)
    return NewAccountOutput(
        customerId=account.customerId,
        accountId=account.accountId
    )