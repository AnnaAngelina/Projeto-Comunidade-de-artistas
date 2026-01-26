import asyncpg

async def get_db_connection():
    return await asyncpg.connect(
        user= "organizacao_projeto",
        password="12345",
        database="blog_pequenos_artistas",
        host="localhost",
        port = 5432
    )
