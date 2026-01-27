from fastapi import FastAPI
import asyncpg
from routes.arte_routes import arteRouter
from routes.categoria_routes import categoryRouter
from routes.cadastro_routes import cadastro
from routes.usuario_routes import usuarioRouter
from routes.loginRouter import loginRouter

app = FastAPI()


app.include_router(arteRouter)
app.include_router(categoryRouter)
app.include_router(cadastro)
app.include_router(usuarioRouter)
app.include_router(loginRouter)
