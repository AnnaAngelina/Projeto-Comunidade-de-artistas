from fastapi import FastAPI, APIRouter
import asyncpg
from routes.Arte_routes import arteRouter
from routes.cadastro_routes import cadastro

app = FastAPI()

app.include_router(arteRouter)

app.include_router(cadastro)
