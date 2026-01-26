from fastapi import FastAPI, APIRouter
import asyncpg
from routes.arte_routes import arteRouter
from routes.categoria_routes import categoryRouter
from routes.cadastro_routes import cadastro

app = FastAPI()

app.include_router(arteRouter)
app.include_router(categoryRouter)
app.include_router(cadastro)
