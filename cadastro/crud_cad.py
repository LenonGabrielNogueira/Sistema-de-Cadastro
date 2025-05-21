# Impotando o SQLLite3 : 
import sqlite3 

# Conexão com Banco de Dados :
try:
    conn = sqlite3.connect("cadastro_alunos.db")
    print("Conectado com Banco de Dados com sucesso!")
except sqlite3.Error as e:
    print("Erro ao se conctar com Banco de Dados, ", e)
    
# Manipulando Tabela de Cursos -------------------------- : 

# Criar Cursos (Inserir CRUD) CREATE :
def criar_cursos(lista_cursos):
    with conn:
        cur = conn.cursor()
        chave = " INSERT INTO cursos (nome, duracao, preco) VALUES (?,?,?) "
        cur.execute(chave, lista_cursos)
#criar_cursos(['Python', 'Semanas', 50])


# Vizualização de Tabela Cursos (Selecionar CRUD) READ : 
def ver_cursos():
    lista = []
    with conn:
        cur = conn.cursor()
        cur.execute(" SELECT * FROM cursos ")
        linha = cur.fetchall()
        
        for lista_cursos in linha:
            lista.append(lista_cursos)
    return lista
#print(ver_cursos())


# Atualizar da Tabela Cursos (Atualiar CRUD) UPDATE : 
def atualizar_cursos(up):
    with conn:
        cur = conn.cursor()
        chave = " UPDATE cursos SET nome=?, duracao=?, preco=? WHERE id=? " 
        cur.execute(chave, up)
l = ["Python", "Duas Semanas", 50, 1]


# Apangando dados da Tabela Cursos (Deletar CRUD) DELETE : 
def deletar_cursos(det):
    with conn:
        cur = conn.cursor()
        chave = " DELETE FROM cursos WHERE id=? "
        cur.execute(chave, det)
#deletar_cursos([9])


# Manipulando Tabela de Turmas ------------------------ :

# Criando Turmas (Inserir CRUD) CREATE : 
def criar_turmas(tur):
    with conn:
        cur = conn.cursor()
        chave = " INSERT INTO turmas (nome, cursos_nome, data_inicio) VALUES (?,?,?) "
        cur.execute(chave, tur)


# Vizualização Tabela Turmas (Selecionar CRUD) READ :
def ver_turmas():
    lista = []
    with conn:
        cur = conn.cursor()
        cur.execute(" SELECT * FROM turmas ")
        linha = cur.fetchall()
        
        for i in linha:
            lista.append(i)
    return lista


# Atualizando Tabela Turmas (Atualizar CRUD) UPDATE :
def atualizar_turmas(up):
    with conn:
        cur = conn.cursor()
        chave = " UPDATE turmas SET nome=?, cursos_nome=?, data_inicio=? WHERE id=? "
        cur.execute(chave, up)
        
        
# Apagando Tabela Turmas (Deletar CRUD) DELETE : 
def deletar_turmas(det):
    with conn:
        cur = conn.cursor()
        chave = " DELETE turmas WHERE id=? "
        cur.execute(chave, det)



# Manipulando Tabela de Alunos -------------------------------- :

# Criar Dados na Tabela Alunos (Inserir CRUD) CREATE:
def criar_alunos(aluno):
    with conn:
        cur = conn.cursor()
        chave = " INSERT INTO alunos (nome, email, telefone, sexo, imagem, data_nacs, cpf, turma_nome) VALUES (?,?,?,?,?,?,?,?) "
        cur.execute(chave, aluno)
        
        
# Vizualizando Dados da Tabela Alunos (Selecionar CRUD) READ : 
def ver_alunos():
    lista = []
    with conn:
        cur = conn.cursor()
        cur.execute(" SELECT * FROM alunos ")
        linha = cur.fetchall()
        
        for i in linha:
            lista.append(i)
    return lista


# Atualizando Dados da Tabela Alunos (Atualizar CRUD) UPDATE : 
def atualizar_aluno(aluno):
    with conn:
        cur = conn.cursor()
        chave = " UPDATE turmas SET nome=?, email=?, telefone=?, imagem=?, data_nacs=?, cpf=?, turma_nome=? WHERE id=? "
        cur.execute(chave, aluno)
        
        
# Apagando Dados da Tabela Alunos (Deletar CRUD) DELETE : 
def deletar_aluno(aluno):
    with conn:
        cur = conn.cursor()
        chave = " DELETE FROM alunos WHERE id=? "
        cur.execute(chave, aluno)

 
         