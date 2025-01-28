from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.Customer import Customer
from app.modassembly.database.sql.get_sql_session import get_sql_session

router = APIRouter()

@router.delete("/contacts/{contact_id}", response_model=dict)
async def delete_contact(contact_id: int, db: Session = Depends(get_sql_session)) -> dict:
    """
    Deletes a contact by its identifier.

    - **contact_id**: The ID of the contact to delete.
    """
    # Find the existing contact by identifier
    contact = db.query(Customer).filter(Customer.id == contact_id).first()
    
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")

    # Delete the contact's record
    db.delete(contact)
    db.commit()

    return {"message": "Contact deleted successfully"}
