#importanto sqlite3
import sqlite3 as sql 

#Criando conexao e cursor.
conn = sql.connect('Aluno_db1.db')
cursor = conn.cursor()

#Variavel usada no laço de repetição(vai ser alterada)
escolha = 0

#Classe para criar o database
class Criar():
    cursor.execute('CREATE TABLE IF NOT EXISTS alunos (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER, cpf TEXT)')
    conn.commit()

#Classe para inserir dados
class Inserir:
    def __init__(self):
        
        #Recebimento dos dados
        p = str(input('Digite o nome: '))
        p1 = int(input('Digite a idade: '))
        p2 = str(input('Digite o cpf: '))

        #Uso de tupla para criar uma lista, esta lista preencherá os campos da tabela na ordem
        lista = (p, p1, p2)

        cursor.execute("INSERT INTO alunos(nome, idade, cpf)VALUES(?, ?, ?)", lista)
        conn.commit()
        print('Aluno cadastrado!')

#Classe principal para escolher as ações
class Principal:

    #Laço de repetição
    while escolha != 3:
        escolha = int(input('Deseja ver os alunos? DIGITE 1\nDeseja cadastar um aluno? DIGITE 2\nDeseja sair do sistema? DIGITE 3'))
        
        #Leitura dos dados
        if escolha == 1:
            cursor.execute('SELECT * FROM alunos')
            print(cursor.fetchall())

        #Chamada da primeira classe
        elif escolha == 2:
            inserir = Inserir()

        #Fechar database, junto do laço
        elif escolha == 3:
            conn.close()
            print('Servidor finalizado!')
            break;