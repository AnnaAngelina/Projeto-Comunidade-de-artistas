import asyncpg
from fastapi import APIRouter
from models import Categoria
from database import get_db_connection

categoryRouter = APIRouter(prefix='/categoria', tags=['categorias'])

@categoryRouter.post('/new-category')
async def newCategory(category: Categoria):
    """Adicionar uma nova categoria"""
    conn = await get_db_connection()
    await conn.execute("INSERT INTO categoria (nome_categoria) VALUES ($1)", category.nome_categoria)
    await conn.close()
    return {'Mensagem': f'Categoria ({category.nome_categoria}) adicionada com sucesso!'}

@categoryRouter.get('/list-category')
async def listCategory():
    """Listar as categorias existentes"""
    conn = await get_db_connection()
    categorias = await conn.fetch("SELECT nome_categoria FROM categoria")
    await conn.close()
    return {'Categorias': categorias}
