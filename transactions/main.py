from uuid import uuid4
from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NewTransactionInput(BaseModel):
    accountId: str
    transactionAmount: int

class NewTransactionOutput(BaseModel):
    transactionId: str

class Transaction(BaseModel):
    transactionId: str
    transactionAmount: int
    # TODO: transactionDate


class TransactionDatabase:
    def __init__(self):
        self._accounts = {}
    
    def add_account(self, account_detail: NewTransactionInput) -> str:
        transaction_id = str(uuid4())
        self._accounts[transaction_id] = account_detail
        return transaction_id

    def get_transactions_for_customer(self, account_id):
        return [
            Transaction(transactionId=transaction_id, transactionAmount=detail.transactionAmount)
            for transaction_id, detail in self._accounts.items() if detail.accountId == account_id
        ]

TransactionDB = TransactionDatabase()

@app.post("/new")
async def new(new_trans_detail: NewTransactionInput):
    transaction_id = TransactionDB.add_account(new_trans_detail)
    return NewTransactionOutput(
        transactionId=transaction_id
    )

@app.get("/get/{account_id}")
async def get_transactions(account_id: str) -> List[Transaction]:
    transactions = TransactionDB.get_transactions_for_customer(account_id)
    return transactions
