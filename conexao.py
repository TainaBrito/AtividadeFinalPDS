def abrir_conexao():
    try:
        conexao = psycopg2.connect(
            database="tbmakes",
            user="adm_tbmakes",
            password="admtbmakes",
            host="tbmakes.cnbkkiavari1.us-east-1.rds.amazonaws.com",
            port="5432"
        )
        cursor = conexao.cursor()
        print("Conexão bem-sucedida!")
        return conexao, cursor

    except psycopg2.Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        raise 
     # Releva a exceção para que ela possa ser tratada onde a função de conexão é chamada

def fechar_conexao(conexao, cursor):
    if conexao:
        conexao.close()
        print("Conexão fechada.")