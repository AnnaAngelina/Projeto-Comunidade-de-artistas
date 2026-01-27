import asyncpg
from fastapi import APIRouter, HTTPException, status
from models import Loguin
from database import get_db_connection
from starlette.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED


loguinRouter = APIRouter(prefix='/login', tags=['login'])

async def verificando_usuario(conn, email: str, senha: str):
    query = "SELECT id_usuario, nome FROM usuario WHERE email = $1 AND senha = $2"
    return await conn.fetchrow(query, email, senha)

@loguinRouter.post('/')
async def autentificar_login(user: Loguin):
    conn = await get_db_connection()

    usuario = await verificando_usuario(conn, user.email, user.senha)

    await conn.close()

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos"
        )

    return {
        "mensagem": "Login realizado com sucesso",
        "usuario": {
            "id": usuario["id_usuario"],
            "nome": usuario["nome"]
        }
    }
