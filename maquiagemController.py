from maquiagemBean import MaquiagemBean
from maquiagemDAO import MaquiagemDAO

class MaquiagemController:

    def __init__(self):
        self.__maquiagem_dao = MaquiagemDAO()
