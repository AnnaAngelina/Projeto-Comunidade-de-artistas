import asyncpg
from database import get_db_connection
from models import Arte
from fastapi import APIRouter

arteRouter = APIRouter(prefix='/arte', tags=["artes"])

@arteRouter.post('/new-Art')
async def newArt(arte: Arte):
    """Adicionar uma nova arte ao blog"""
    conn = await get_db_connection()
    await conn.execute("INSERT INTO artes (id_usuario, id_categoria, nome_arte, descricao, data_publicacao, data_de_criacao) VALUES ($1, $2, $3, $4, $5, $6)", arte.id_usuario, arte.id_categoria, arte.nome_arte, arte.descricao, arte.data_publicacao, arte.data_de_criacao)
    await conn.close()
    return {"message": f"Arte ({arte.nome_arte}) adicionada com sucesso!"}

