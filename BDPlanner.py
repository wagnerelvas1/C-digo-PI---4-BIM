from Conexao import *
conexao = iniciarConexao()

sqlTabelaUsuario = ''' CREATE TABLE IF NOT EXISTS usuario (
                        id INTEGER PRIMARY KEY NOT NULL, 
                        nome VARCHAR(50) NOT NULL, 
                        tipo VARCHAR(45) NOT NULL, 
                        telefone CHAR(14) NOT NULL, 
                        email VARCHAR(50) NOT NULL, 
                        senha CHAR(8) NOT NULL
                        ); '''

sqlTabelaCalendario = ''' CREATE TABLE IF NOT EXISTS calendario (
                        id INTEGER PRIMARY KEY NOT NULL, 
                        diaMes DATE NOT NULL, 
                        ano YEAR NOT NULL, 
                        horaMinuto TIME NOT NULL
                        ); '''

sqlTabelaAgendamento = ''' CREATE TABLE IF NOT EXISTS agendamento (
                        id INTEGER PRIMARY KEY NOT NULL
                        ); '''


sqlTabelaAtividade = ''' CREATE TABLE IF NOT EXISTS atividade (
                        id INTEGER PRIMARY KEY NOT NULL, 
                        titulo VARCHAR(45) NOT NULL, 
                        descricao VARCHAR(45), 
                        prazo INTEGER NOT NULL, 
                        data INTEGER NOT NULL, 
                        horario INTEGER NOT NULL, 
                        fk_idUsuario INTEGER, 
                        FOREIGN KEY (fk_idUsuario)
                        REFERENCES usuario (id)
                        ); '''

sqlTabelaEndereco = ''' CREATE TABLE IF NOT EXISTS endereco (
                        id INTEGER PRIMARY KEY NOT NULL, 
                        logradouro VARCHAR(45) NOT NULL, 
                        cidade VARCHAR(45) NOT NULL, 
                        estado VARCHAR(45) NOT NULL, 
                        cep VARCHAR(45) NOT NULL
                        ); '''
