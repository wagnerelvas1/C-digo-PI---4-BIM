import sqlite3 as sql3

arquivoBanco = 'banco.db'


def iniciarConexao():
    conexao = None
    try:
        conexao = sql3.connect(arquivoBanco)
    except sql3.Error as e:
        print(f'Ops... Deu um erro iniciando a conexão: {e}')
    return conexao


def fecharConexao(conexao):
    if conexao:
        conexao.close()


def criarTabela(conexao, sqlCriarTabela):
    try:
        cursor = conexao.cursor()
        cursor.execute(sqlCriarTabela)
    except sql3.Error as e:
        print(f'Ops... Deu um erro criando a tabela: {e}')


def inserirAtividade(conexao, sqlInserirAtividade):
    try:
        cursor = conexao.cursor()
        cursor.execute(sqlInserirAtividade)
        conexao.commit()
    except sql3.Error as e:
        print(f'Ops... Deu um erro inserindo dados: {e}')


def buscarAtividades(conexao, sqlBuscarAtividades):
    atividades = None
    try:
        cursor = conexao.cursor()
        cursor.execute(sqlBuscarAtividades)
        atividades = cursor.fetchall()
    except sql3.Error as e:
        print(f'Ops... Deu um erro exibindo dados: {e}')
    finally:
        return atividades


def inserirUsuario(conexao, sqlInserirUsuario):
    try:
        cursor = conexao.cursor()
        cursor.execute(sqlInserirUsuario)
        conexao.commit()
    except sql3.Error as e:
        print(f'Ops... Deu um erro inserindo dados: {e}')


def buscarUsuarios(conexao, sqlBuscarUsuarios):
    usuarios = None
    try:
        cursor = conexao.cursor()
        cursor.execute(sqlBuscarUsuarios)
        usuarios = cursor.fetchall()
    except sql3.Error as e:
        print(f'Ops... Deu um erro exibindo dados: {e}')
    finally:
        return usuarios

def executarComando(conexao, sqlComando):
    try:
        cursor = conexao.cursor()
        cursor.execute(sqlComando)
    except sql3.Error as e:
        print(f'Ops... Deu um erro executando comando: {e}')


sqlBuscarUsuarios = 'SELECT * FROM usuario'

sqlBuscarAtividades = 'SELECT * FROM atividade'
