import sqlite3


arquivoBanco = 'banco.db'


def iniciarConexao():
    conexao = None
    try:
        conexao = sqlite3.connect(arquivoBanco)
    except sqlite3.Error as e:
        print(f'Ops... Deu um erro iniciando a conexão: {e}')
    return conexao


def fecharConexao(conexao):
    if conexao:
        conexao.close()


def criarTabela(conexao, sqlCriarTabela):
    try:
        cursor = conexao.cursor()
        cursor.execute(sqlCriarTabela)
    except sqlite3.Error as e:
        print(f'Ops... Deu um erro criando a tabela: {e}')


def inserirUsuario(conexao, sqlInserirUsuario):
    try:
        cursor = conexao.cursor()
        cursor.execute(sqlInserirUsuario)
        conexao.commit()
    except sqlite3.Error as e:
        print(f'Ops... Deu um erro inserindo dados: {e}')


def buscarUsuarios(conexao, sqlBuscarUsuarios):
    usuarios = None
    try:
        cursor = conexao.cursor()
        cursor.execute(sqlBuscarUsuarios)
        usuarios = cursor.fetchall()
    except sqlite3.Error as e:
        print(f'Ops... Deu um erro exibindo dados: {e}')
    finally:
        return usuarios

sqlInserirUsuarioDudu = 'INSERT INTO usuario (nome, tipo, telefone, email, senha) VALUES ("Wagner", "Aluno", "98120302736120", "wagner.relvas", "123123")'

sqlBuscarUsuarios = 'SELECT * FROM usuario'
# Terminar de ver slides de conexão