from typing import Optional
"""Types which define the input/output of the API
"""
from pydantic import BaseModel


class NewAccountInput(BaseModel):
    customerId: str
    customerFirstName: str
    customerLastName: str
    openingBalancePence: Optional[int]

class NewAccountOutput(BaseModel):
    customerId: str
    accountId: str
