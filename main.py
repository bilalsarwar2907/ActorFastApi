from fastapi import FastAPI
from routers import actor_router
from database.database import create_tables
import models.actor_entity  # registers the table with Base

app = FastAPI()
create_tables()
app.include_router(actor_router.router)