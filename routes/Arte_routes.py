import asyncpg
from database import get_db_connection
from models import Arte
from fastapi import APIRouter

arteRouter = APIRouter(prefix='/arte', tags=["artes"])

@arteRouter.post('/new-art')
async def newArt(arte: Arte):
    """Adicionar uma nova arte ao blog"""
    conn = await get_db_connection()
    await conn.execute("INSERT INTO artes (id_usuario, id_categoria, nome_arte, descricao, data_publicacao, data_de_criacao) VALUES ($1, $2, $3, $4, $5, $6)", arte.id_usuario, arte.id_categoria, arte.nome_arte, arte.descricao, arte.data_publicacao, arte.data_de_criacao)
    await conn.close()
    return {"message": f"Arte ({arte.nome_arte}) adicionada com sucesso!"}


@arteRouter.get('/list-arts')
async def listArt():
    """Mostrar as artes cadastradas"""
    conn = await get_db_connection()
    arts = await conn.fetch("SELECT nome, sobrenome, nome_arte, nome_categoria, descricao, data_publicacao, data_de_criacao FROM artes INNER JOIN usuario USING (id_usuario) INNER JOIN categoria USING (id_categoria)")
    colecao = []
    for art in arts:
        colecao.append({'artista': f'{art["nome"]} {art["sobrenome"]}', 'título da obra': f'{art["nome_arte"]}', 'categoria': f'{art["nome_categoria"]}', 'descrição': f'{art["descricao"]}', 'data de publicação': f'{art["data_publicacao"]}', 'data de criação': f'{art["data_de_criacao"]}'})
    return {"Total de artes": len(colecao), "Artes": colecao}