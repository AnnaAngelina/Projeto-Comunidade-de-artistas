from fastapi import FastAPI, APIRouter
import asyncpg
from routes.arte_routes import arteRouter
from routes.categoria_routes import categoryRouter

app = FastAPI()

app.include_router(arteRouter)
app.include_router(categoryRouter)
