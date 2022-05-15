import os
from unittest import mock

import pytest

from httpx import AsyncClient

from accounts.main import app



@pytest.mark.asyncio
async def test_accounts_happy_path_no_opening_default():
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
async def test_accounts_happy_path_with_zero_opening_default():
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
async def test_accounts_happy_path_with_negative_opening_default():
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
