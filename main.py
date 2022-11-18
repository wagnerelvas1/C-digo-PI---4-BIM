from Conexao import *
from BDPlanner import *

criarTabela(conexao, sqlTabelaAgendamento)
criarTabela(conexao, sqlTabelaUsuario)
criarTabela(conexao, sqlTabelaAtividade)
criarTabela(conexao, sqlTabelaCalendario)
criarTabela(conexao, sqlTabelaEndereco)

nome = input('Nome: ')
tipo = input('Tipo: ')
telefone = input('Telefone: ')
email = input('Email: ')
senha = input('Senha: ')

sqlInserirUsuarioNovo = (f'INSERT INTO usuario (nome, tipo, telefone, email, senha) VALUES ("{nome}", "{tipo}", "{telefone}", "{email}", "{senha}")')

inserirUsuario(conexao, sqlInserirUsuarioNovo)

usuarios = buscarUsuarios(conexao, sqlBuscarUsuarios)

fecharConexao(conexao)

for usuario in usuarios:
    print(f'O usuario {usuario[1]} de id = {usuario[0]} é um {usuario[2]}')