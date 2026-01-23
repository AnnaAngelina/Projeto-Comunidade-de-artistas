import asyncpg

async def get_db_connection():
    return await asyncpg.connect(
        user= "postgres",
        password= "programadora2.0",
        database="blog_pequenos_artistas",
        host="localhost",
        port = 5432
    )
