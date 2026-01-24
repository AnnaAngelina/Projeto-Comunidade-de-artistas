from pydantic import BaseModel
from datetime import date
from typing import Optional

class Categoria(BaseModel):
    nome_categoria: str

class Arte(BaseModel):
    id_usuario: int
    id_categoria: int
    nome_arte: str
    descricao: Optional[str] = None
    data_publicacao: date
    data_de_criacao: date