class MaquiagemBean:

    def __init__(self):
        self.__codigo = None
        self.__nome = None
        self.__preco = None
        self.__estado = None

    def getCodigo(self):
        return self.__codigo

    def getNome(self):
        return self.__nome

    def getPreco(self):
        return self.__preco

    def getEstado(self):
        return self.__estado
