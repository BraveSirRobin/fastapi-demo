import os
from fastapi import FastAPI
from httpx import AsyncClient

from .service_types import NewAccountInput, NewAccountOutput
from .data_layer import InMemoryAccountDatastore, Account

app = FastAPI()
transaction_service_url = os.environ["TRANSATIONS_SERVICE_PORT"]

AccountDS = InMemoryAccountDatastore()

@app.post("/open")
async def open(new_ac_detail: NewAccountInput) -> NewAccountOutput:
    account: Account = Account(
        customerId=new_ac_detail.customerId,
        customerFirstName=new_ac_detail.customerFirstName,
        customerLastName=new_ac_detail.customerLastName
    )
    AccountDS.add_account(account)
    if new_ac_detail.openingBalance > 0:
        async with AsyncClient() as client:
            r = await client.post(
                f"{transaction_service_url}/new",
                json={
                    "accountId": account.accountId,
                    "transactionAmount": new_ac_detail.openingBalance
                },
            )
            print(r.json())
    return NewAccountOutput(
        customerId=account.customerId,
        accountId=account.accountId
    )