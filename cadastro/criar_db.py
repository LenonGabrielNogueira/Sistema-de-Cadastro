# impotando o SQLite3
import sqlite3

# criando conexão
try:
    conn = sqlite3.connect('cadastro_alunos.db')
    print(f"Conectado com sucesso!")
except sqlite3.Error as e:
        print(f"Erro ao contectar")
        
# Criando tabela de cursos : 
try:
    with conn:
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS cursos( 
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        nome TEXT, 
                        duracao TEXT, 
                        preco REAL
                    ) """)
        print(f"Tabela cursos criado com sicesso!")
except sqlite3.Error as e:
    print(f"Erro ao crir a tabela!", e) 
    
#Criando tabela de turmas : 
try:
    with conn:
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS turmas(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        cursos_nome TEXT,
                        data_inicio DATE,
                        FOREIGN KEY (cursos_nome) REFERENCES cursos (nome) ON UPDATE CASCADE ON DELETE CASCADE
                    ) """)
        print(f"Tabela turmas criada com sucesso!")
except sqlite3.Error as e:
    print(f"Erro ao criar a tabela turmas!", e) 
    
# Criando tabela de alunos :
try:
    with conn:
        cur = conn.cursor()
        cur.execute( """ CREATE TABLE IF NOT EXISTS alunos( 
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        email TEXT,
                        telefone TEXT,
                        sexo TEXT,
                        imagem TEXT,
                        data_nasc DATE,
                        cpf TEXT,
                        turma_nome TEXT,+
                        FOREIGN KEY (turma_nome) REFERENCES turmas (nome) ON UPDATE CASCADE ON DELETE CASCADE
                    ) """ )
        print(f"Tabela alunos criado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao criar a tabela alunos!", e)