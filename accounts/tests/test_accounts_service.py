import os
from unittest import mock

import pytest

from httpx import AsyncClient

from accounts.main import app



@pytest.mark.asyncio
async def test_accounts_open_no_opening_balance():
    async with AsyncClient(app=app, base_url="http://test") as asc:
        response = await asc.post(
            "/open",
            json={
                "customerId": "cust-1",
                "customerFirstName": "Henry",
                "customerLastName": "Holmes",
            }
        )
        assert "accountId" in response.json()
        assert "customerId" in response.json()
        assert response.json()["customerId"] == "cust-1"
        assert response.json()["faultMessage"] == None


@pytest.mark.asyncio
async def test_accounts_open_with_zero_opening_balance():
    async with AsyncClient(app=app, base_url="http://test") as asc:
        response = await asc.post(
            "/open",
            json={
                "customerId": "cust-1",
                "customerFirstName": "Henry",
                "customerLastName": "Holmes",
                "openingBalance": 0
            }
        )
        assert "accountId" in response.json()
        assert "customerId" in response.json()
        assert response.json()["customerId"] == "cust-1"
        assert response.json()["faultMessage"] == None


@pytest.mark.asyncio
async def test_accounts_open_with_negative_opening_balance():
    async with AsyncClient(app=app, base_url="http://test") as asc:
        response = await asc.post(
            "/open",
            json={
                "customerId": "cust-1",
                "customerFirstName": "Henry",
                "customerLastName": "Holmes",
                "openingBalance": -55
            }
        )
        assert response.status_code == 422


@pytest.mark.asyncio
@mock.patch(
    "accounts.config.AccountsServiceConfig",
)
@mock.patch(
    "accounts.transaction_service.TransactionService.call_new_transaction",
    return_value={
        "transactionId": "b732667d-3adb-44bf-87c5-13fff2531fdf",
        "transactionAmount": 55,
        "transactionDate": "2022-05-15T21:18:29.970481"
    }
)
async def test_accounts_open_with_positive_opening_balance(
    _mock_new_trans,
    _mock_asc,
):
    async with AsyncClient(app=app, base_url="http://test") as asc:
        response = await asc.post(
            "/open",
            json={
                "customerId": "cust-1",
                "customerFirstName": "Henry",
                "customerLastName": "Holmes",
                "openingBalance": 55
            }
        )
        assert response.status_code == 200
        resp_data = response.json()
        assert "openingBalanceTransaction" in resp_data
        assert "transactionId" in resp_data["openingBalanceTransaction"]
        assert "transactionAmount" in resp_data["openingBalanceTransaction"]
        assert "transactionDate" in resp_data["openingBalanceTransaction"]
        assert resp_data["openingBalanceTransaction"]["transactionAmount"] == 55


