from typing import Optional
"""Types which define the input/output of the API"""
from pydantic import BaseModel


class NewAccountInput(BaseModel):
    customerId: str
    customerFirstName: str
    customerLastName: str
    openingBalance: Optional[int] = 0

class NewAccountOutput(BaseModel):
    customerId: str
    accountId: str
