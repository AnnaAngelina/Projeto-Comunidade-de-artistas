from fastapi import FastAPI
import asyncpg

app = FastAPI()

async def get_db_connection():
    return await asyncpg.connect(
        user= "postgres",
        password= "",
        database="blog_pequenos_artistas",
        host="localhost",
    )

@app.get('/')
async def test_conection():
    conn = await get_db_connection()
    await conn.close()
    return {'message': 'Conexão estabelecida'}
