import asyncpg
from database import get_db_connection
from models import Usuario
from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

cadastro = APIRouter(prefix='/autenticacao', tags=["autenticacao"])

# verifica se banco com o email. fetchrow retorna None se não existe ou algo se existe.
async def usuario_ja_existe(conn, email: str):
    query = "SELECT 1 FROM usuario WHERE email = $1" #verifica se existe pelo menos um registro
    resultado = await conn.fetchrow(query, email)
    return resultado is not None

@cadastro.post('/cadastro')
async def criar(usuario: Usuario):
    conn = await get_db_connection()

    # verifica se já existe
    if await usuario_ja_existe(conn, usuario.email):
        await conn.close()
        raise HTTPException( #interrompe imediatamente a execução da função
            status_code=HTTP_400_BAD_REQUEST,
            detail="Usuário já cadastrado com esse e-mail"
        )

    await conn.execute(
        """
        INSERT INTO usuario (
            username, nome, sobrenome, data_de_nascimento, email, senha,
            numero_de_telefone, rua, numero, bairro, cidade, cep
        )
        VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12)
        """,
        usuario.username,
        usuario.nome,
        usuario.sobrenome,
        usuario.data_de_nascimento,
        usuario.email,
        usuario.senha,
        usuario.numero_de_telefone,
        usuario.rua,
        usuario.numero,
        usuario.bairro,
        usuario.cidade,
        usuario.cep
    )

    await conn.close()
    return {"message": f"Usuário ({usuario.nome}) cadastrado com sucesso!"}