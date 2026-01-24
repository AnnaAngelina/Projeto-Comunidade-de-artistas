import asyncpg
from database import get_db_connection
from models import Usuario
from fastapi import APIRouter

cadastro = APIRouter(prefix='/cadastro', tags=["cadastro"])

@cadastro.post('/criar')
async def criar(usuario: Usuario):
    """Adicionar um usuario"""
    conn = await get_db_connection()
    await conn.execute("INSERT INTO usuario (id_usuario, nome, sobrenome, data_de_nascimento, numero_de_telefone, email, senha, rua, numero, bairro, cidade, cep) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12)", usuario.id_usuario, usuario.nome, usuario.sobrenome, usuario.data_de_nascimento, usuario.numero_de_telefone, usuario.email, usuario.senha, usuario.rua, usuario.numero, usuario.bairro, usuario.cidade, usuario.cep)
    await conn.close()
    return {"message": f"Usuario ({usuario.nome}) cadastrado com sucesso!"}


