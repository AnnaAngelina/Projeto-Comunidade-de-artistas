import asyncpg
from database import get_db_connection
from models import Arte
from fastapi import APIRouter, HTTPException

arteRouter = APIRouter(prefix='/arte', tags=["artes"])

@arteRouter.post('/new-art')
async def newArt(arte: Arte):
    """Adicionar uma nova arte ao blog"""
    conn = await get_db_connection()
    await conn.execute("INSERT INTO artes (id_usuario, id_categoria, nome_arte, descricao, data_publicacao, data_de_criacao) VALUES ($1, $2, $3, $4, $5, $6)", arte.id_artista, arte.id_categoria, arte.nome_arte, arte.descricao, arte.data_publicacao, arte.data_de_criacao)
    await conn.close()
    return {"message": f"Arte ({arte.nome_arte}) adicionada com sucesso!"}


@arteRouter.get('/list-arts')
async def listArt():
    """Mostrar as artes cadastradas"""
    conn = await get_db_connection()
    arts = await conn.fetch("SELECT id_arte, nome, sobrenome, nome_arte, nome_categoria, descricao, data_publicacao, data_de_criacao FROM artes INNER JOIN usuario USING (id_usuario) INNER JOIN categoria USING (id_categoria)")
    await conn.close()
    colecao = []
    for art in arts:
        colecao.append({'id': art["id_arte"], 'artista': f'{art["nome"]} {art["sobrenome"]}', 'título da obra': f'{art["nome_arte"]}', 'categoria': f'{art["nome_categoria"]}', 'descrição': f'{art["descricao"]}', 'data de publicação': f'{art["data_publicacao"]}', 'data de criação': f'{art["data_de_criacao"]}'})
    return {"Total de artes": len(colecao), "Artes": colecao}


@arteRouter.put('/{id_art}')
async def updateArt(id_art: int, arte: Arte):
    """Atualizar uma arte"""
    conn = await get_db_connection()
    arteUpd = await conn.fetch("SELECT * FROM artes WHERE id_arte = $1", id_art)
    if arteUpd:
        await conn.execute("UPDATE artes SET id_usuario = $1, id_categoria = $2, nome_arte = $3, descricao = $4, data_publicacao = $5, data_de_criacao = $6 WHERE id_arte = $7", arte.id_artista, arte.id_categoria, arte.nome_arte, arte.descricao, arte.data_publicacao, arte.data_de_criacao, id_art)
        await conn.close()
        return {'Message': 'Arte atualizada com sucesso!'}
    else:
        raise HTTPException(status_code=404, detail=f"Não há Arte associada ao id ({id_art})")

@arteRouter.delete('/{id_art}')
async def deleteArt(id_art: int):
    """Apagar (permanentemente) uma arte"""
    conn = await get_db_connection()
    artedel = await conn.fetch("SELECT * FROM artes WHERE id_arte = $1", id_art)
    if artedel:
        await conn.execute("DELETE FROM artes WHERE id_arte = $1", id_art)
        await conn.close()
        return {'Message': 'Arte excluída com sucesso!'}
    else:
        raise HTTPException(status_code=404, detail=f"Não há Arte associada ao id ({id_art})")