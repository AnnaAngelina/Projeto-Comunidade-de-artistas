import asyncpg
from fastapi import APIRouter, HTTPException
from models import Usuario
from database import get_db_connection

usuarioRouter = APIRouter(
    prefix='/user',
    tags=['usuario']
)

@usuarioRouter.get('/{nickname}')
async def get_usuario(nickname: str):
    conn = await get_db_connection()

    usuario = await conn.fetch('SELECT * FROM usuario WHERE username = $1', nickname)
    await conn.close()
    if not usuario:
        raise HTTPException(
            status_code=404,
            detail=f'O usuário com o nome de usuário {nickname} não foi encontrado.'
        )
    return usuario


@usuarioRouter.put('/update/{nickname}') 
async def update_usuario(nickname: str, usuario_edit: Usuario):
    conn = await get_db_connection() 
     
    user_upd = await conn.fetchrow('SELECT 1 FROM usuario WHERE username = $1', nickname) 
     
    if user_upd: 
         await conn.execute('UPDATE usuario SET username = $1, nome = $2, sobrenome = $3, data_de_nascimento = $4, email = $5, senha = $6, numero_de_telefone = $7, rua = $8, numero = $9, bairro = $10, cidade = $11, cep = $12 WHERE username = $13', 
                            usuario_edit.username, 
                            usuario_edit.nome, 
                            usuario_edit.sobrenome, 
                            usuario_edit.data_de_nascimento, 
                            usuario_edit.email, 
                            usuario_edit.senha, 
                            usuario_edit.numero_de_telefone, 
                            usuario_edit.rua, 
                            usuario_edit.numero, 
                            usuario_edit.bairro, 
                            usuario_edit.cidade, 
                            usuario_edit.cep, 
                            nickname) 
        
    else:
         raise HTTPException(
              status_code=404, 
              detail=f'O usuário com o nome de usuário {nickname} não foi encontrado.' 
              )
    await conn.close()
    return {"message": "Usuário atualizado com sucesso"}


@usuarioRouter.delete('delete/{nickname}')
async def delete(nickname: str):
    conn = await get_db_connection()
    
    user_del = await conn.fetch('SELECT * FROM usuario WHERE username = $1', nickname)
    if user_del:
        await conn.execute('DELETE FROM usuario WHERE username = $1', nickname)
        return {"message": "Usuário deletado com sucesso."}

    else: 
        await conn.close()
        raise HTTPException(
            status_code=404,
            detail=f'O usuário com o nome de usuário {nickname} não foi encontrado.'
        )
        


    

    

        
