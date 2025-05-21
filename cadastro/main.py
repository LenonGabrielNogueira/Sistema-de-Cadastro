# Impotando Dependecias do Tkinter no projeto : 
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from tkcalendar import Calendar, DateEntry
from datetime import date

# Importando Dependencias Pillow no projeto : 
from PIL import ImageTk, Image

# Impotando Dependencias Arquivo CRUD :
from crud_cad import *

# Cores usadas no projeto : 
co0 = "#2e2d2b" # Preto;
co1 = "#feffff" # Branco;
co2 = "#e5e5e5" # Cinza;
co3 = "#00a095" # Verde;
co4 = "#403d3d" # Letra;
co5 = "#003452" # Azul;
co6 = "#ef5350" # Vermelho;

co7 = "#038cfc" # Azul;
co8 = "#263238" # + Verde;
co9 = "#e9edf5" # + Verde;


# Criando Janela Vazia -----------------:
janela = Tk()
janela.title("")
janela.geometry('850x620')
janela.configure(background= co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")


# Criando Cabeçalho da Janela ------------------------ : 
frame_logo = Frame(janela, width=850, height=52, bg=co5)
frame_logo.grid(row=0, column=0, pady=0, sticky=NSEW)

# Criando Conteudo da Janela ------------------------- :
ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_dados = Frame(janela, width=850, height=65, bg=co1)
frame_dados.grid(row=2, column=0, pady=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_detalhes = Frame(janela, width=850, height=200, bg=co1)
frame_detalhes.grid(row=4, column=0, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=850, height=200, bg=co1)
frame_tabela.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)


# Manipulando o Frame Logo ---------------------------- :
app_lg = Image.open('views/logo.png')
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="Cadastro de Alunos", width=850, compound=LEFT, relief=RAISED, anchor=NW, font="Ivy 15 bold", bg=co6, fg=co1)
app_logo.place(x=0, y=0)

# Função para Cadastrar Alunos ----------------------- :
def alunos():
    print(f"Alunos")
    
# Função para Adicionar Cursos e Turmas ------------- :
def adicionar():
    # Criando Frames para a Tabela : 
    frame_tabela_curso = Frame(frame_tabela, width=300, height=200, bg=co1)
    frame_tabela_curso.grid(row=0, column=0, pady=0, padx=10, sticky=NSEW)

    frame_tabela_turma = Frame(frame_tabela, width=300, height=200, bg=co1)
    frame_tabela_turma.grid(row=0, column=2, pady=0, padx=10, sticky=NSEW)
    
    frame_tabela_linha = Frame(frame_tabela, width=30, height=200, bg=co1)
    frame_tabela_linha.grid(row=0, column=1, pady=0, padx=10, sticky=NSEW)
    
    # Detalhes da Turma ----------------------------------------- :
    
    l_nome = Label(frame_detalhes, text="Nome do Curso *", height=1, anchor=NW, font="Ivy 10", bg=co1, fg=co4)
    l_nome.place(x=4, y=10)
    e_nome_curso = Entry(frame_detalhes, width=35, justify='left', relief='solid')
    e_nome_curso.place(x=7, y=40)
    
    l_duracao = Label(frame_detalhes, text="Duração *", height=1, anchor=NW, font='Ivy 10', bg=co1, fg=co4)
    l_duracao.place(x=4, y=70)
    e_duracao = Entry(frame_detalhes, width=20, justify='left', relief="solid")
    e_duracao.place(x=7, y=100)
    
    l_preco = Label(frame_detalhes, text="Preço *", height=1, anchor=NW, font="Ivy 10", bg=co1, fg=co4)
    l_preco.place(x=4, y=130)
    e_preco = Entry(frame_detalhes, width=10, justify="left", relief="solid")
    e_preco.place(x=7, y=160)
    
    # Criando Botoes do Frame Tabela :
    botao_carregar = Button(frame_detalhes, anchor=CENTER, text="Salvar".upper(), width=10, overrelief=RIDGE, font='Ivy 7 bold', bg=co3, fg=co1)
    botao_carregar.place(x=107, y=160)
    
    botao_atualizar = Button(frame_detalhes, anchor=CENTER, text="Atualizar".upper(), width=10, overrelief=RIDGE, font='Ivy 7 bold', bg=co6, fg=co1)
    botao_atualizar.place(x=187, y=160)
    
    botao_deletar = Button(frame_detalhes, anchor=CENTER, text="Deletar".upper(), width=10, overrelief=RIDGE, font='Ivy 7 bold', bg=co7, fg=co1)
    botao_deletar.place(x=267, y=160)
    
    # Tabela de Cursos ---------------------------- :
    def mostrar_cursos():
        app_nome = Label(frame_tabela_curso, text="Tabela de Cursos", height=1, pady=0, padx=0, relief="flat", anchor=NW, font='Ivy 10 bold', bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)
        
        # Criando Visualização de Dados :
        lista_dados = ['ID', 'Cursos', 'Duração', 'Preço']
        df_lista = ver_cursos()
        global arvore_cursos
        
        arvore_cursos = ttk.Treeview(frame_tabela_curso, selectmode='extended', columns=lista_dados, show='headings')
        # Barra Vertical :
        vsb = ttk.Scrollbar(frame_tabela_curso, orient='vertical', command=arvore_cursos.yview)
        # Barra Horizontal :
        hsb = ttk.Scrollbar(frame_tabela_curso, orient="horizontal", command=arvore_cursos.xview)
        
        arvore_cursos.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        arvore_cursos.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela_curso.grid_rowconfigure(0, weight=12)
        
        hd = ['nw', 'nw', 'e', 'e']
        h = [30, 150, 80, 60]
        n = 0
        
        for coluna in lista_dados:
            arvore_cursos.heading(coluna, text=coluna.title(), anchor=NW)
            # Ajuste da Coluna :
            arvore_cursos.column(coluna, width=h[n], anchor=hd[n])
            n += 1
        
        for item in df_lista:
            arvore_cursos.insert('', 'end', values=item)
    
    mostrar_cursos() 
    
    # Linha de Separação Detalhes: 
    L_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
    L_linha.place(x=374, y=10)
    L_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co1, fg=co1)
    L_linha.place(x=372, y=10)
    
    # Linha de Separação Tabela: 
    L_linha = Label(frame_tabela_linha, relief=GROOVE, text='h', width=1, height=140, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
    L_linha.place(x=6, y=10)
    L_linha = Label(frame_tabela_linha, relief=GROOVE, text='h', width=1, height=140, anchor=NW, font=('Ivy 1'), bg=co1, fg=co1)
    L_linha.place(x=4, y=10)
    
    # Detalhes da Turma -------------------------------------- :
    
    l_nome = Label(frame_detalhes, text='Nome da Turma *', height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.place(x=404, y=10)
    e_nome_turma = Entry(frame_detalhes, width=35, justify='left', relief='solid')
    e_nome_turma.place(x=407, y=40)
    
    l_turma = Label(frame_detalhes, text='Curso *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_turma.place(x=404, y=70)
    
    # Selecionando os Cursos do Banco ---- :
     
    cursos = ['curso 1', 'curso 2']
    curso = []
    
    for item in cursos:
        curso.append(item)
    
    c_curso = ttk.Combobox(frame_detalhes, width=20, font=('Ivy 10 bold'))
    c_curso['values'] = (cursos)
    c_curso.place(x=404, y=100)
    
    l_data_inicio = Label(frame_detalhes, text='Data de Inicio', height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_data_inicio.place(x=406, y=130)
    data_inicio = DateEntry(frame_detalhes, width=10, background='darkblue', foreground='white', borderwidth=2, year=2023)
    data_inicio.place(x=407, y=160)
    
     # Criando Botoes do Frame Cursos :
    botao_carregar = Button(frame_detalhes, anchor=CENTER, text="Salvar".upper(), width=10, overrelief=RIDGE, font='Ivy 7 bold', bg=co3, fg=co1)
    botao_carregar.place(x=507, y=160)
    
    botao_atualizar = Button(frame_detalhes, anchor=CENTER, text="Atualizar".upper(), width=10, overrelief=RIDGE, font='Ivy 7 bold', bg=co6, fg=co1)
    botao_atualizar.place(x=587, y=160)
    
    botao_deletar = Button(frame_detalhes, anchor=CENTER, text="Deletar".upper(), width=10, overrelief=RIDGE, font='Ivy 7 bold', bg=co7, fg=co1)
    botao_deletar.place(x=667, y=160)
    
    # Função para Ver as Turmas ---------------------- :
    def mostrar_turmas():
        app_nome = Label(frame_tabela_turma, text="Tabela de Turmas", height=1, pady=0, padx=0, relief='flat', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        app_nome.grid(row=0, column=0, padx=10, sticky=NSEW)
        
        # Criando Visualização de Dados :
        lista_dados = ['ID', 'Nome da Turma', 'Curso', 'Inicio']
        df_lista = ver_turmas()
        global arvore_turmas
        
        arvore_turmas = ttk.Treeview(frame_tabela_turma, selectmode='extended', columns=lista_dados, show='headings')
        # Barra Vertical :
        vsb = ttk.Scrollbar(frame_tabela_turma, orient='vertical', command=arvore_turmas.yview)
        # Barra Horizontal :
        hsb = ttk.Scrollbar(frame_tabela_turma, orient="horizontal", command=arvore_turmas.xview)
        
        arvore_turmas.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        arvore_turmas.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela_turma.grid_rowconfigure(0, weight=12)
        
        hd = ['nw', 'nw', 'e', 'e']
        h = [30, 130, 150, 80]
        n = 0
        
        for coluna in lista_dados:
            arvore_turmas.heading(coluna, text=coluna.title(), anchor=NW)
            # Ajuste da Coluna :
            arvore_turmas.column(coluna, width=h[n], anchor=hd[n])
            n += 1
        
        for item in df_lista:
            arvore_turmas.insert('', 'end', values=item)
    
    mostrar_turmas() 
    
    
    
    
    
# Função para Salvar os Dados --------------------- :
def salvar():
    print(f"Salvar")

# Manipulando o Frame Detalhes ----------------------- :
def controle(dado):
    # Cadastro de Alunos :
    if dado == 'cadastro':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()
        
        # Chamando a Função Alunos -:
        alunos()
        
    # Adicionar Dados :
    if dado == 'adicionar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
            
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        
        # Chamando a Função Adicionar :
        adicionar()
        
    # Salvando Dados :
    if dado == 'salvar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
            
        for widget in frame_tabela.winfo_children():
            widget.destroy()
            
        # Chamando a Função Salvar:
        salvar()
        
# Criando Botoes ------------------------------ :
app_img_cad = Image.open("views/adicionado.png")
app_img_cad = app_img_cad.resize((18,18))
app_img_cad = ImageTk.PhotoImage(app_img_cad)
app_cad = Button(frame_dados, command=lambda:controle('cadastro'), image=app_img_cad, text="Cadastro", width=100, compound=LEFT, overrelief=RIDGE, font="Ivy 11", bg=co1, fg=co0)
app_cad.place(x=10, y=30)


app_img_add = Image.open("views/update.png")
app_img_add = app_img_add.resize((18,18))
app_img_add = ImageTk.PhotoImage(app_img_add)
app_add = Button(frame_dados, command=lambda:controle('adicionar'), image=app_img_add, text="Adicionar", width=100, compound=LEFT, overrelief=RIDGE, font="Tvy 11", bg=co1, fg=co0)
app_add.place(x=123, y=30)


app_img_salvar = Image.open("views/salvou.png")
app_img_salvar = app_img_salvar.resize((18,18))
app_img_salvar = ImageTk.PhotoImage(app_img_salvar)
app_salvar = Button(frame_dados, command=lambda:controle('salvar'), image=app_img_salvar, text="Salvar", width=100, compound=LEFT, overrelief=RIDGE, font="Ivy 11", bg=co1, fg=co0)
app_salvar.place(x=236, y=30)


janela.mainloop()
