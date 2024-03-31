CREATE DATABASE my_cash_flow;

-- Tabela de Lançamentos
CREATE TABLE lancamentos (
    id SERIAL PRIMARY KEY,
    data_lancamento DATE NOT NULL,
    tipo_lancamento VARCHAR(20) NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    descricao TEXT,
    conta_id INTEGER REFERENCES contas(id)
);

-- Tabela de Categorias
CREATE TABLE categorias (
    id SERIAL PRIMARY KEY,
    tipo_lancamento VARCHAR(20) NOT NULL,
    nome VARCHAR(100) NOT NULL
);

-- Tabela de Contas
CREATE TABLE contas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    tipo_conta VARCHAR(50) NOT NULL,
    saldo DATE,
    dia_vcto INTEGER,
    dia_fechamento INTEGER
);