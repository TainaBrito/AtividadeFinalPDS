import psycopg2

class MaquiagensDAO:

    def _init_(self):
        self.conexao = psycopg2.connect(database="TB Makes", user="adm_tbmakes", password="admtbmakes", host="TBMakes.cnbkkiavari1.us-east-1.rds.amazonaws.com", port="5432")

        self.cursor = self.conexao.cursor()