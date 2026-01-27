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

class ArteResponse(BaseModel):
    nome: str
    sobrenome: str
    nome_arte: str
    nome_categoria: str
    descricao: Optional[str] = None
    data_publicacao: date
    data_de_criacao: date


class Usuario(BaseModel):
    username: str
    nome: str
    sobrenome: str
    data_de_nascimento: date
    email: str
    senha: str
    numero_de_telefone: Optional[str] = None  
    rua: Optional[str] = None
    numero: Optional[int] = None               
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    cep: Optional[str] = None