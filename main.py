from Conexao import *
from BDPlanner import *

criarTabela(conexao, sqlTabelaAgendamento)
criarTabela(conexao, sqlTabelaUsuario)
criarTabela(conexao, sqlTabelaAtividade)
criarTabela(conexao, sqlTabelaCalendario)
criarTabela(conexao, sqlTabelaEndereco)

inserirUsuario(conexao, sqlInserirUsuarioDudu)

usuarios = buscarUsuarios(conexao, sqlBuscarUsuarios)

fecharConexao(conexao)

for usuario in usuarios:
    print(f'O usuario {usuario[1]} de id = {usuario[0]} é um {usuario[2]}')