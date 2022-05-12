import httpx


class TransactionServiceException(Exception):
    pass


class TransactionService:

    def __init__(self, transaction_service_url_base: str):
        self._trans_base = transaction_service_url_base

    async def call_new_transaction(self, account_id: str, transaction_amount: int) -> list:
        try:
            async with httpx.AsyncClient() as client:
                r = await client.post(
                    f"{self._trans_base}/new",
                    json={
                        "accountId": account_id,
                        "transactionAmount": transaction_amount
                    },
                )
        except:
            raise TransactionServiceException("http exception whilst calling transaction service")
        else:
            if r.status_code != 200:
                raise TransactionServiceException(f"transaction service failed with status {r.status_code}")
            return r.json()

    async def call_get_transactions(self, account_id: str) -> list:
        try:
            async with httpx.AsyncClient() as client:
                r = await client.get(f"{self._trans_base}/get/{account_id}")
        except:
            raise TransactionServiceException("http exception whilst calling transaction service")
        if r.status_code != 200:
            raise TransactionServiceException(f"transaction service failed with status {r.status_code}")
        return r.json()