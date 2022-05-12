import os
from urllib import response
from fastapi import FastAPI, Response, status
import httpx

from .service_types import NewAccountInput, NewAccountOutput, AccountDetails, TransactionDetail
from .data_layer import InMemoryAccountDatastore, Account, UnknownAccountError
from .transaction_service import TransactionService, TransactionServiceException

app = FastAPI()
transaction_service_url = os.environ["TRANSATIONS_SERVICE_PORT"]

AccountDS = InMemoryAccountDatastore()


@app.post("/open", response_model=NewAccountOutput)
async def open(new_ac_detail: NewAccountInput):
    account: Account = Account(
        customerId=new_ac_detail.customerId,
        customerFirstName=new_ac_detail.customerFirstName,
        customerLastName=new_ac_detail.customerLastName
    )
    AccountDS.add_account(account)
    response_params = {
        "customerId": account.customerId,
        "accountId": account.accountId,
    }
    if new_ac_detail.openingBalance > 0:
        try:
            trans_service = TransactionService(transaction_service_url)
            r = await trans_service.call_new_transaction(account.accountId, new_ac_detail.openingBalance)
            response_params["openingBalanceTransaction"] = TransactionDetail(**r)
        except TransactionServiceException:
            response_params["faultMessage"] = "failed to store opening balance transaction"
    return NewAccountOutput(**response_params)



@app.get("/account-details/{account_id}", response_model=AccountDetails)
async def account_details(account_id: str, response: Response):
    try:
        account: Account = AccountDS.get_account(account_id)
    except UnknownAccountError:
        response.status_code = status.HTTP_404_NOT_FOUND
    else:
        response_params = {
            "customerId": account.customerId,
            "customerFirstName": account.customerFirstName,
            "customerLastName": account.customerLastName,
        }
        try:
            trans_service = TransactionService(transaction_service_url)
            transactions = await trans_service.call_get_transactions(account_id)
        except TransactionServiceException:
            response_params["faultMessage"] = "failed to fetch transactions"
        else:
            response_params["balance"] = sum(x["transactionAmount"] for x in transactions)
            response_params["transactions"] = [TransactionDetail(**t) for t in transactions]

        return AccountDetails(**response_params)

