#importanto sqlite3
import sqlite3 as sql

#Criando conexao e cursor.
conn = sql.connect('Aluno_db2.db')
cursor = conn.cursor()

#Classe para criar o database
class Criar():
    cursor.execute('CREATE TABLE IF NOT EXISTS alunos (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER, cpf TEXT)')
    conn.commit()
