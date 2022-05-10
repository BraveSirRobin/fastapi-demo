from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Account(BaseModel):
    accountId: str
    userFirstname: str
    userLastname: str
    dateOpened: str  # TODO: Make a datetime

