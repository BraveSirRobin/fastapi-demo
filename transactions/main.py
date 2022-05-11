from uuid import uuid4
from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel

from .service_types import NewTransactionInput, TransactionDetail
from .data_layer import InMemoryTransactionDatastore, Transaction

app = FastAPI()


TransactionDS = InMemoryTransactionDatastore()

@app.post("/new")
async def new(new_trans_detail: NewTransactionInput):
    transaction: Transaction = Transaction(
        accountId=new_trans_detail.accountId,
        transactionAmount=new_trans_detail.transactionAmount
    )
    TransactionDS.add_transaction(transaction)
    return TransactionDetail(
        transactionId=transaction.transactionId,
        transactionAmount=transaction.transactionAmount,
        transactionDate=transaction.transactionDate
    )

@app.get("/get/{account_id}")
async def get_transactions(account_id: str) -> List[Transaction]:
    transactions = TransactionDS.get_transactions_for_account(account_id)
    return [
        TransactionDetail(
            transactionId=t.transactionId,
            transactionAmount=t.transactionAmount,
            transactionDate=t.transactionDate
        )
        for t in transactions
    ]
