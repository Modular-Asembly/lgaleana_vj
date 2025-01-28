from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.models.Customer import Customer
from app.modassembly.database.sql.get_sql_session import get_sql_session

router = APIRouter()

class ContactUpdate(BaseModel):
    name: str
    email: str
    phone_number: str
    address: str

class SuccessResponse(BaseModel):
    message: str

@router.put("/contacts/{contact_id}", response_model=SuccessResponse)
def update_contact(contact_id: int, contact_data: ContactUpdate, db: Session = Depends(get_sql_session)) -> SuccessResponse:
    """
    Update a contact's information.

    - **contact_id**: The ID of the contact to update.
    - **contact_data**: The new data for the contact.
    """
    contact = db.query(Customer).filter(Customer.id == contact_id).first()
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")

    contact.name = contact_data.name
    contact.email = contact_data.email
    contact.phone_number = contact_data.phone_number
    contact.address = contact_data.address

    db.commit()

    return SuccessResponse(message="Contact updated successfully")
