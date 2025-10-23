from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import json


app = FastAPI(title="Automated Invoice Generator")


class Item(BaseModel):
    description: str
    rate_per_hour: float
    hours: float

class ClientInformation(BaseModel):
    client_name: str
    email: str
    company_name: Optional[str] = None
    country: str
    due_date: str  # ISO format

class InvoiceData(BaseModel):
    client_information: ClientInformation
    items: list[Item]
    notes: Optional[str] = None
    submission_date: str  # ISO format, auto
    total_amount: float

    class Config:
        # Allow extra fields to be ignored
        extra = "ignore"

@app.post("/generate_invoice")
async def generate_invoice_endpoint(invoice_data: InvoiceData):
    print(
        f"Received invoice generation request:\n{json.dumps(invoice_data.model_dump(), indent=2)}"
    )