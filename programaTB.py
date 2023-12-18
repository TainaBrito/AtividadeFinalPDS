import psycopg2

class MaquiagensDAO:

    def _init_(self):
        self.conexao = psycopg2.connect(database="TBMakes", user="adm_tbmakes", password="admtbmakes", host="tbmakes.cnbkkiavari1.us-east-1.rds.amazonaws.com", port="5432")

        self.cursor = self.conexao.cursor()

    def remover_maquiagens(self,maquiagens):
        sql = f"delete from maquiagens where codigo = {maquiagens.getCodigo()}"

        self.cursor.execute(sql)
        self.conexao.commit()

    def atualizar_maquiagens(self, maquiagens):
        sql = f"update maquiagens set nome = '{maquiagens.getNome()}', marca = '{maquiagens.getMarca()}', preco = '{maquiagens.getPreço()}' where codigo = {maquiagens.getCodigo()}"

        self.cursor.execute(sql)
        self.conexao.commit()
        
    def visualizar(self):
            sql = "select * from maquiagens"
            self.cursor.execute(sql)

            resultado = self.cursor.fetchall()
            texto = ""

            for linha in resultado:
                texto = texto + f"Código: {str(linha[0])} \nNome: {str(linha[1])} \nMarca: {str(linha[2])} \nPreço: {str(linha[3])} \n \n"
    
            return texto