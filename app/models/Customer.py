from sqlalchemy import Column, Integer, String
from app.modassembly.database.sql.get_sql_session import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone_number = Column(String, nullable=False)
    address = Column(String, nullable=False)
