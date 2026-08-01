from fastapi import FastAPI
from routers import actor_router, auth_router
from database.database import create_tables
import models.actor_entity
import models.user_entity  # registers users table with Base

app = FastAPI()
create_tables()
app.include_router(auth_router.router)
app.include_router(actor_router.router)