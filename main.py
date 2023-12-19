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
