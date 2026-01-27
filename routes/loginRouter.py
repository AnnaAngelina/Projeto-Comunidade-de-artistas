import asyncpg
from fastapi import APIRouter, HTTPException, status
from models import Usuario, Loguin
from database import get_db_connection
from starlette.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED


loguinRouter = APIRouter(prefix='/login', tags=['login'])

# async def usuario_ja_existe(conn, email: str):
#     query = "SELECT 1 FROM usuario WHERE email = $1" #verifica se existe pelo menos um registro
#     resultado = await conn.fetchrow(query, email)
#     return resultado is not None

async def verificando_senha(conn, email: str, senha:str):
    query = f"SELECT 1 FROM usuario WHERE email = $1 AND senha = $2"  
    resultado = await conn.fetchrow(query, email, senha)
    return resultado is not None

# def login(logui_verificação: Loguin, session: Session = Depends(get_db_connection))

# @loguinRouter.post('/login')


# def login(loguinV: Loguin, session: Session = Depends(get_db_connection))
#     email = loguinV.email
#     telefone = loguinV.



@loguinRouter.post('/login')
async def autentificar_login(user: Loguin):
    conn = await get_db_connection()

    usuario_valido = await verificando_senha(
        conn, user.email, user.senha
    )

    await conn.close()

    if not usuario_valido:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos"
        )

    return {
        'mensagem': 'Login realizado com sucesso'
    }