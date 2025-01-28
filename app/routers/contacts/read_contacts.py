from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.Customer import Customer
from app.modassembly.database.sql.get_sql_session import get_sql_session
from pydantic import BaseModel

router = APIRouter()

class CustomerResponse(BaseModel):
    id: int
    name: str
    email: str
    phone_number: str
    address: str

    class Config:
        orm_mode = True

@router.get("/contacts", response_model=List[CustomerResponse], summary="Get all contacts", description="Retrieve a list of all contacts from the database.")
def read_contacts(db: Session = Depends(get_sql_session)) -> List[CustomerResponse]:
    """
    Retrieves all contacts from the database.

    - **db**: Database session dependency.
    - **returns**: List of contacts.
    """
    contacts = db.query(Customer).all()
    return [CustomerResponse(
        id=contact.id,
        name=contact.name.__str__(),
        email=contact.email.__str__(),
        phone_number=contact.phone_number.__str__(),
        address=contact.address.__str__()
    ) for contact in contacts]
