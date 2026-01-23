from fastapi import FastAPI, APIRouter
import asyncpg
from routes.Arte_routes import arteRouter

app = FastAPI()

app.include_router(arteRouter)

