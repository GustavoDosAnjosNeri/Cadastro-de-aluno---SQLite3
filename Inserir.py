from BDD import *

class Inserir:
    def __init__(self):
        
        #Recebimento dos dados
        p = str(input('Digite o nome: '))
        p1 = int(input('Digite a idade: '))
        p2 = str(input('Digite o cpf: '))

        #Uso de tupla para criar uma lista, esta lista preencherá os campos da tabela na ordem
        lista = (p, p1, p2)
        if p2 ==

        cursor.execute("INSERT INTO alunos(nome, idade, cpf)VALUES(?, ?, ?)", lista)
        conn.commit()
        print('Aluno cadastrado!')