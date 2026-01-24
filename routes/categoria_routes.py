import asyncpg
from fastapi import APIRouter, HTTPException
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
    categorias = await conn.fetch("SELECT * FROM categoria")
    await conn.close()
    return {'Categorias': categorias}

@categoryRouter.delete('/{id_category}')
async def deleteCategory(id_category: int):
    """Excluir (permanentemente) uma categoria"""
    conn = await get_db_connection()
    categorydel = await conn.fetch("SELECT * FROM categoria WHERE id_categoria = $1", id_category)
    if categorydel:
        await conn.execute("DELETE FROM categoria WHERE id_categoria = $1", id_category)
        await conn.close()
        return {'Message': 'Categoria excluida com sucesso!'}
    else:
        raise HTTPException(status_code=404, detail=f"Não há categoria associada ao id ({id_category})")   