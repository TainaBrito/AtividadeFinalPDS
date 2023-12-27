from maquiagemBean import MaquiagemBean
from programaTB import MaquiagensDAO

r = MaquiagemBean()
r.setCodigo(1110)
r.setNome('Paleta de Sombras')
r.setPreco('45,00')
r.setEstado('Disponível')

maq_dao = MaquiagensDAO()

#Inserção na tabela:
#maq_dao.inserir_maquiagem(r)

#Remoção da tabela:
#maq_dao.remover_maquiagem(r)

#Atualização de dados na tabela:
#maq_dao.atualizar_maquiagem(r)

#Visualização da tabela:
#maq_dao.visualizar()
#print(maq_dao.visualizar())
