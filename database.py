import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()

async def get_db_connection():
    return await asyncpg.connect(
        user='postgres',
        password='programadora2.0',
        database='blog_pequenos_artistas',
        host='localhost',
        port=5432
    )

# user=os.getenv('DB_USER','postgres'),
# password=os.getenv('DB_PASSWORD'),
# database=os.getenv('DB_DATABASE','blog_pequenos_artistas'),
# host=os.getenv('DB_HOST','localhost'),
# port=os.getenv('DB_PORT',5432)
