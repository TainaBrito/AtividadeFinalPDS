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
TelaLogin.iconbitmap('Sistema\\imagens\\C:\Users\20201214010015\Downloads\WhatsApp Image 2023-12-22 at 07.16.55.jpeg')
TelaLogin.resizable(False, False)
customtkinter.set_appearance_mode("Light")

#Funções
def JanelaPrincipal():

    TelaLogin.destroy()
    time.sleep(0.3)

    janela = customtkinter.CTk()
    janela.title('TB Makes')
    janela.iconbitmap('Sistema\\imagens\\C:\Users\20201214010015\Downloads\WhatsApp Image 2023-12-22 at 07.16.55.jpeg')
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

aba1_CadastrarButton = Button(aba1,bd=0,bg="#000B37", width=222, height=60, image=bt_cadastrar, command = cadastrar_produto)
aba1_CadastrarButton.place(x = 430 , y = 475)
aba1_LimparDados = Button(aba1,bd=0,bg="#000B37", width=222, height=60, image=bt_limpar1, command = Limpar_aba1)
aba1_LimparDados.place(x = 140, y = 475)

#Aba2 - Visualizar Dados
    aba2 = ttk.Frame(gerenciadorAba)
    gerenciadorAba.add(aba2, text="  Visualizar Produtos  ")
    gerenciadorAba.pack(expand=1, fill="both")

    #Elementos da Aba 2
    fundo_visualizar = PhotoImage(file="Sistema\\imagens\\fundo-visualizar.png")
    lab_fundo = Label(aba2, image=fundo_visualizar)
    lab_fundo.pack()

    bt_visualizar = PhotoImage(file="Sistema\\imagens\\bt-visualizar.png")

    aba2_VisualizarButton = Button(aba2,bg="#000B37", width=236, height=50, image = bt_visualizar, bd=0, command = visualizar_produto)
    aba2_VisualizarButton.place(x = 102, y = 397)
    aba2_Texto = Text(aba2,bd=5)
    aba2_Texto.place(x = 453 , y = 95,width=280,height=410)
    
    #Aba3 - Atualizar Produtos
    aba3 = ttk.Frame(gerenciadorAba)
    gerenciadorAba.add(aba3, text="  Atualizar Produtos  ")
    gerenciadorAba.pack(expand=1, fill="both")
    
    #Elementos da Aba 3
    
    fundo_atualizar = PhotoImage(file="Sistema\\imagens\\fundo-atualizar.png")
    lab_fundo = Label(aba3, image=fundo_atualizar)
    lab_fundo.pack()

    bt_limpar3 = PhotoImage(file="Sistema\\imagens\\bt-limpar.png")
    bt_atualizar = PhotoImage(file="Sistema\\imagens\\bt-atualizar.png")

    aba3_CodigoEntry = Entry(aba3,bd=0,width=55)
    aba3_CodigoEntry.place(x = 269, y = 207)

    aba3_NomeEntry = Entry(aba3,bd=0,width=55)
    aba3_NomeEntry.place(x = 269, y = 271)

    aba3_PrecoEntry = Entry(aba3,bd=0,width=55)
    aba3_PrecoEntry.place(x = 269, y = 335)

    aba3_EstadoEntry = Entry(aba3,bd=0,width=55)
    aba3_EstadoEntry.place(x = 269 , y = 399)

    aba3_AtualizarButton = Button(aba3,bd=0,bg="#000B37", width=222, height=60, image=bt_atualizar, command = atualizar_produto)
    aba3_AtualizarButton.place(x = 430 , y = 475)
    aba3_LimparDados = Button(aba3,bd=0,bg="#000B37", width=222, height=60, image=bt_limpar3, command = Limpar_aba3)
    aba3_LimparDados.place(x = 140, y = 475)
    
    #Aba4 - Remover Produto
    aba4 = ttk.Frame(gerenciadorAba)
    gerenciadorAba.add(aba4, text="Remover Produto")
    gerenciadorAba.pack(expand=1, fill="both")

    fundo_remover = PhotoImage(file="Sistema\\imagens\\fundo-remover.png")
    lab_fundo = Label(aba4, image=fundo_remover)
    lab_fundo.pack()

    #Elementos da Aba 4
    
    aba4_CodigoEntry = Entry(aba4,bd=0)
    aba4_CodigoEntry.place(x = 304, y = 284,width=313, height=38)

    bt_remover = PhotoImage(file="Sistema\\imagens\\bt-remover.png")
    bt_limpar4 = PhotoImage(file="Sistema\\imagens\\bt-limpar.png")

    aba4_RemoverButton = Button(aba4, width=222, height=50, bd=0,bg="#000B37", image = bt_remover, command = remover_produto )
    aba4_RemoverButton.place(x = 434 , y = 419)
    aba4_LimparDados = Button(aba4,width=222, height=50, bd=0,bg="#000B37", image = bt_limpar4 , command = Limpar_aba4)
    aba4_LimparDados.place(x = 144, y = 419)

    #Definir as dimensões da janela
    janela.geometry("800x600+300+100")
    janela.mainloop()
  
def Login():
    tbsenha = "admin"
    tbusuario = "admin"

    usuario = en_usuario.get()
    senha = en_senha.get()

    if(usuario == tbusuario and senha == tbsenha):
        JanelaPrincipal()
    else:
        messagebox.showinfo(title="Erro!",message="O usuário ou senha inserida está errada!\nTente novamente.")
        en_usuario.delete(0,'end')
        en_senha.delete(0,'end')  

# Variáveis globais
esconda_senha = StringVar()

# Importar imagens
img_fundo = PhotoImage(file="Sistema\\imagens\\fundo-login2.png")
img_botao = PhotoImage(file="Sistema\\imagens\\bt-login.png")

# Criação de labels
lab_fundo = Label(TelaLogin, image=img_fundo)
lab_fundo.pack()

# Criação de caixas de entrada
en_usuario = Entry(TelaLogin, bd=0, font=("Calibri", 15),justify=CENTER)
en_usuario.place(width=189, height=37, x=179, y=266)

en_senha = Entry(TelaLogin, textvariable=esconda_senha, show="*", bd=0, font=("Calibri", 15),justify=CENTER)
en_senha.place(width=189, height=36, x=179, y=324)

# Criação de botões
bt_entrar = Button(TelaLogin, bd=0, image=img_botao, command = Login)
bt_entrar.place(width=160, height=40, x=165, y=390)

TelaLogin.mainloop()

    
