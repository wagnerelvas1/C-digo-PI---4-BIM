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


def inserirAluno(conexao, sqlInserirAluno):
    try:
        cursor = conexao.cursor()
        cursor.execute(sqlInserirAluno)
        conexao.commit()
    except sqlite3.Error as e:
        print(f'Ops... Deu um erro inserindo dados: {e}')


def buscarAlunos(conexao, sqlBuscarAlunos):
    alunos = None
    try:
        cursor = conexao.cursor()
        cursor.execute(sqlBuscarAlunos)
        alunos = cursor.fetchall()
    except sqlite3.Error as e:
        print(f'Ops... Deu um erro exibindo dados: {e}')
    finally:
        return alunos
