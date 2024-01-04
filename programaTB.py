import psycopg2

class MaquiagensDAO:

    def _init_(self):
        self.conexao = psycopg2.connect(database="temp", user="aluno_20201214010015", password="1212", host="177.136.200.206", port="5439")

        self.cursor = self.conexao.cursor()

    def inserir_maquiagens(self, Maquiagens):
        sql = f"insert into Maquiagens values ({Maquiagens.getCodigo()}, '{Maquiagens.getNome()}', '{Maquiagens.getPreco()}', '{Maquiagens.getEstado()}')"

        self.cursor.execute(sql)
        self.conexao.commit()

    def remover_maquiagens(self,Maquiagens):
        sql = f"delete from Maquiagens where codigo = {Maquiagens.getCodigo()}"

        self.cursor.execute(sql)
        self.conexao.commit()

    def atualizar_maquiagens(self, Maquiagens):
        sql = f"update Maquiagens set nome = '{Maquiagens.getNome()}', estado = '{Maquiagens.getEstado()}', preco = '{Maquiagens.getPreço()}' where codigo = {Maquiagens.getCodigo()}"

        self.cursor.execute(sql)
        self.conexao.commit()
        
    def visualizar(self):
            sql = "select * from Maquiagens"
            self.cursor.execute(sql)

            resultado = self.cursor.fetchall()
            texto = ""

            for linha in resultado:
                texto = texto + f"Código: {str(linha[0])} \nNome: {str(linha[1])} \nEstado: {str(linha[2])} \nPreço: {str(linha[3])} \n \n"
    
            return texto
