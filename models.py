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
    data_criacao: date

class ArteResponse(BaseModel):
    artista: str
    titulo: str
    categoria: str
    descricao: Optional[str] = None
    publicacao: date
    criacao: date

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

class Login(BaseModel):
    email: str
    senha: str

