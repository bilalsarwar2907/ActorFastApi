from fastapi import FastAPI
from routers import actor_router

app = FastAPI()
app.include_router(actor_router.router)