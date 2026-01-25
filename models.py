from pydantic import BaseModel
from datetime import date
from typing import Optional

class Categoria(BaseModel):
    nome_categoria: str

class Arte(BaseModel):
    id_artista: int
    id_categoria: int
    nome_arte: str
    descricao: Optional[str] = None
    data_publicacao: date
    data_de_criacao: date

class Usuario(BaseModel):
    nome: str
    sobrenome: str
    data_de_nascimento: date
    email: str
    senha: str
    numero_de_telefone: str   
    rua: str
    numero: str               
    bairro: str
    cidade: str
    cep: str  