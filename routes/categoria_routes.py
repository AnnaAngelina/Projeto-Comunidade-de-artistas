import asyncpg
from fastapi import APIRouter, HTTPException
from models import Categoria
from database import get_db_connection
from starlette.status import HTTP_400_BAD_REQUEST

categoryRouter = APIRouter(prefix='/categoria', tags=['categorias'])

async def categoria_ja_existe(conn, nome_categoria: str):
    query = "SELECT 1 FROM categoria WHERE nome_categoria = $1" #verifica se existe pelo menos um registro
    resultado = await conn.fetchrow(query, nome_categoria)
    return resultado is not None


@categoryRouter.post('/new-category')
async def newCategory(category: Categoria):
    """Adicionar uma nova categoria"""
    conn = await get_db_connection()

    if await categoria_ja_existe(conn, category.nome_categoria):
        await conn.close()
        raise HTTPException( #interrompe imediatamente a execução da função
            status_code=HTTP_400_BAD_REQUEST,
            detail="Essa categoria já está cadastrada"
        )

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