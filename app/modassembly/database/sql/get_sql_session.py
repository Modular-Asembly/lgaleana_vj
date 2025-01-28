import os
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker


Base = declarative_base()
engine = create_engine(os.environ["DB_URL"])
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_sql_session() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
