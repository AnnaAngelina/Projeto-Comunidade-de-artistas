-- Active: 1754932896160@@127.0.0.1@5432@blog_pequenos_artistas
CREATE TABLE IF NOT EXISTS usuario (
	id_usuario SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    nome VARCHAR(100) NOT NULL,
    sobrenome VARCHAR(100) NOT NULL,
    data_de_nascimento DATE NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    senha VARCHAR(50) NOT NULL,
    numero_de_telefone CHAR(20),
    rua VARCHAR(150),
    numero INT,
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    cep CHAR(10)
);

CREATE TABLE IF NOT EXISTS categoria (
    id_categoria SERIAL PRIMARY KEY,
    nome_categoria VARCHAR(100) UNIQUE NOT NULL 
);

CREATE TABLE IF NOT EXISTS artes (
    id_arte SERIAL PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_categoria INT,
    nome_arte VARCHAR(100) NOT NULL,
    descricao TEXT,
    data_criacao DATE,
    data_publicacao DATE
);

ALTER TABLE artes
ADD CONSTRAINT fk_artes_usuario
FOREIGN KEY (id_usuario)
REFERENCES usuario(id_usuario);

ALTER TABLE artes
ADD CONSTRAINT fk_artes_categoria
FOREIGN KEY (id_categoria)
REFERENCES categoria(id_categoria) ON DELETE SET NULL;

