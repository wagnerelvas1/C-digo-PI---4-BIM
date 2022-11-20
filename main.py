from Conexao import *
from BDPlanner import *

criarTabela(conexao, sqlTabelaUsuario)
criarTabela(conexao, sqlTabelaAtividade)

nome = input('Nome: ')
tipo = input('Tipo: ')
telefone = input('Telefone: ')
email = input('Email: ')
senha = input('Senha: ')

sqlInserirUsuarioNovo = (f'INSERT INTO usuario (nome, tipo, telefone, email, senha) VALUES ("{nome}", "{tipo}", "{telefone}", "{email}", "{senha}")')


titulo = input('Titulo: ')
descricao = input('Descrição: ')
aaabbb = int(input('numero: '))
bbbccc = int(input('idUsuario: '))

sqlInserirAtividadeNova = (f'INSERT INTO atividade (titulo, descricao, prazo, data, horario, fk_idUsuario) VALUES ("{titulo}", "{descricao}", "{aaabbb}", "{aaabbb}", "{aaabbb}", "{bbbccc}")')


inserirUsuario(conexao, sqlInserirUsuarioNovo)

inserirAtividade(conexao, sqlInserirAtividadeNova)

usuarios = buscarUsuarios(conexao, sqlBuscarUsuarios)

atividades = buscarAtividades(conexao, sqlBuscarAtividades)

fecharConexao(conexao)

for usuario in usuarios:
    print(f'O usuario {usuario[1]} de id = {usuario[0]} é um {usuario[2]}')

for atividade in atividades:
    print(f'A atividade {atividade[1]} de descrição = {atividade[2]}')