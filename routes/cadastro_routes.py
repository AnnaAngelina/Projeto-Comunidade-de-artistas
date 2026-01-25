import asyncpg
from database import get_db_connection
from models import Usuario
from fastapi import APIRouter

cadastro = APIRouter(prefix='/cadastro', tags=["cadastro"])

@cadastro.post('/criar')
async def criar(usuario: Usuario):
    conn = await get_db_connection()

    await conn.execute(
        """
        INSERT INTO usuario (
            nome, sobrenome, data_de_nascimento, email, senha,
            numero_de_telefone, rua, numero, bairro, cidade, cep
        )
        VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11)
        """,
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