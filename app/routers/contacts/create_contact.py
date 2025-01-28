from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from app.models.Customer import Customer
from app.modassembly.database.sql.get_sql_session import get_sql_session

router = APIRouter()

class ContactCreate(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    address: str

class ContactResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone_number: str
    address: str

@router.post("/contacts/", response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
def create_contact(contact: ContactCreate, db: Session = Depends(get_sql_session)) -> ContactResponse:
    """
    Create a new contact in the database.

    - **name**: The full name of the contact
    - **email**: The email address of the contact
    - **phone_number**: The phone number of the contact
    - **address**: The physical address of the contact
    """
    db_contact = Customer(
        name=contact.name,
        email=contact.email,
        phone_number=contact.phone_number,
        address=contact.address
    )
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return ContactResponse(
        id=db_contact.id,
        name=db_contact.name.__str__(),
        email=db_contact.email.__str__(),
        phone_number=db_contact.phone_number.__str__(),
        address=db_contact.address.__str__()
    )
