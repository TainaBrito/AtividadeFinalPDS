from maquiagemBean import MaquiagemBean
from programaTB import MaquiagensDAO

class MaquiagemController:

    def __init__(self):
        self.__maquiagem_dao = MaquiagemDAO()

    def inserir(self, cod, n, p, est):
        maquiagem = MaquiagemBean()
        maquiagem.setCodigo(cod)
        maquiagem.setNome(n)
        maquiagem.setPreco(p)
        maquiagem.setEstado(est)

        self.__maquiagem_dao.inserir_maquiagem(maquiagem)

    def remover(self, cod):
        maquiagem = MaquiagemBean()
        maquiagem.setCodigo(cod)
        self.__maquiagem_dao.remover_maquiagem(maquiagem)

    def visualizar(self):
        return self.__maquiagem_dao.visualizar()

    def atualizar(self, cod, n, p, est):
        maquiagem = MaquiagemBean()
        maquiagem.setCodigo(cod)
        maquiagem.setNome(n)
        maquiagem.setPreco(p)
        maquiagem.setEstado(est)

        self.__maquiagem_dao.atualizar_maquiagem(maquiagem)