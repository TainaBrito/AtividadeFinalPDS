from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date
import time
import customtkinter
import psycopg2

TelaLogin = customtkinter.CTk()
TelaLogin.title("TB Makes")
TelaLogin.geometry("490x560+500+130")
TelaLogin.iconbitmap('Sistema\\imagens\\TBMakes-icone.ico')
TelaLogin.resizable(False, False)
customtkinter.set_appearance_mode("Light")

#Funções
def JanelaPrincipal():

    TelaLogin.destroy()
    time.sleep(0.3)

    janela = customtkinter.CTk()
    janela.title('TB Makes')
    janela.iconbitmap('Sistema\\imagens\\TBMakes-icone.ico')
    janela.resizable(False, False)

    gerenciadorAba = ttk.Notebook(janela)

    conexao = psycopg2.connect(database="tbmakes", user="adm_tbmakes", password="admtbmakes", host="tbmakes.cnbkkiavari1.us-east-1.rds.amazonaws.com", port="5432")
    cursor = conexao.cursor()
    
#Cadastrar Produtos na Tabela
def cadastrar_produto():
        
     messagebox.showinfo(title="Sucesso!",message="O produto foi cadastrado com sucesso!")

    codigo = aba1_CodigoEntry.get()
        nome = aba1_NomeEntry.get()
        preco = aba1_PrecoEntry.get()
        estado = aba1_EstadoEntry.get()

        aba1_CodigoEntry.delete(0,'end')
        aba1_NomeEntry.delete(0,'end')
        aba1_PrecoEntry.delete(0,'end')
        aba1_EstadoEntry.delete(0,'end')

        sql1 = f"insert into Maquiagens values ({codigo},'{nome}','{preco}','{estado}', '{date.today()}')"
        cursor.execute(sql1)
        conexao.commit()

#Remover produtos
def remover_produto():
        
    messagebox.showinfo(title="Sucesso!",message="O produto foi removido com sucesso!")
    codigo = aba4_CodigoEntry.get()
    aba4_CodigoEntry.delete(0,'end')
    sql2 = f"delete from Maquiagens where codigo = {codigo}"
    cursor.execute(sql2)
    conexao.commit()
    
#Limpar Dados das abas
def Limpar_aba1():
    
    aba1_CodigoEntry.delete(0,'end')
    aba1_NomeEntry.delete(0,'end')
    aba1_PrecoEntry.delete(0,'end')
    aba1_EstadoEntry.delete(0,'end')

def Limpar_aba3():
    
    aba3_CodigoEntry.delete(0,'end')
    aba3_NomeEntry.delete(0,'end')  
    aba3_PrecoEntry.delete(0,'end')
    aba3_EstadoEntry.delete(0,'end')
    
def Limpar_aba4():
    
    aba4_CodigoEntry.delete(0,'end')

#Atualizar Produtos
def atualizar_produto():
    messagebox.showinfo(title="Sucesso!",message="O produto foi atualizado com sucesso!")

    codigo = aba3_CodigoEntry.get()
    nova_Funcao = aba3_FuncaoEntry.get()
    novo_Preco = aba3_PrecoEntry.get()
    novo_Nome = aba3_NomeEntry.get()
    
    aba3_CodigoEntry.delete(0,'end')
    aba3_NomeEntry.delete(0,'end')  
    aba3_PrecoEntry.delete(0,'end')
    aba3_EstadoEntry.delete(0,'end')

    sql = f"update Maquiagens set nome = '{novo_Nome}', preco ='{novo_Preco}', estado = '{novo_Estado}' where codigo = {codigo}"
    cursor.execute(sql)
    conexao.commit()
    
#Visualizar Produtos
def visualizar_produto():
    sql = "select * from Maquiagens"
    
    cursor.execute(sql)
    result =  cursor.fetchall()
    
    texto = " " #Variavel Auxiliar
    
    for linha in result:
    
        texto = texto+f"\n Código do Produto: {str(linha[0])}\n Nome: {str(linha[1])}\n Preço: {str(linha[2])}\n Estado: {str(linha[3])}\n Data de Entrada: {str(linha[4])}\n ---------------------------"
    
    aba2_Texto.delete(1.0,'end')
    aba2_Texto.insert(END, texto)

#Aba 1- Cadastrar Produto
aba1 = ttk.Frame(gerenciadorAba)
gerenciadorAba.add(aba1,text="  Cadastrar Produto  ")
gerenciadorAba.pack(expand=1, fill="both")
    
#Elementos da Aba 1
bt_limpar1 = PhotoImage(file="Sistema\\imagens\\bt-limpar.png")
bt_cadastrar = PhotoImage(file="Sistema\\imagens\\bt-cadastrar.png")

img_fundo = PhotoImage(file="Sistema\\imagens\\fundo-cadastrar.png")
lab_fundo = Label(aba1, image=img_fundo)
lab_fundo.pack()

aba1_CodigoEntry = Entry(aba1,bd=0,width=55)
aba1_CodigoEntry.place(x = 269, y = 207)

aba1_PrecoEntry = Entry(aba1,bd=0,width=55)
aba1_PrecoEntry.place(x = 269, y = 271)

aba1_NomeEntry = Entry(aba1,bd=0,width=55)
aba1_NomeEntry.place(x = 269, y = 335)

aba1_EstadoEntry = Entry(aba1,bd=0,width=55)
aba1_EstadoEntry.place(x = 269 , y = 399)

aba1_CadastrarButton = Button(aba1,bd=0,bg="#000B37", width=222, height=60, image=bt_cadastrar, command = cadastrar_maquina)
aba1_CadastrarButton.place(x = 430 , y = 475)
aba1_LimparDados = Button(aba1,bd=0,bg="#000B37", width=222, height=60, image=bt_limpar1, command = Limpar_aba1)
aba1_LimparDados.place(x = 140, y = 475)

    
