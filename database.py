import asyncpg

async def get_db_connection():
    return await asyncpg.connect(
        user= "postgres",
        password="l3t1cia",
        database="blog_pequenos_artistas",
        host="localhost",
        port = 5432
    )
