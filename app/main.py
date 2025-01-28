from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


load_dotenv()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models

from app.models.Customer import Customer

# Endpoints

from app.routers.contacts.create_contact import router
app.include_router(router)
from app.routers.contacts.read_contacts import router
app.include_router(router)
from app.routers.contacts.update_contact import router
app.include_router(router)
from app.routers.contacts.delete_contact import router
app.include_router(router)

# Database

from app.modassembly.database.sql.get_sql_session import Base, engine
Base.metadata.create_all(engine)
