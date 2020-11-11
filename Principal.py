from Inserir import *

#Variavel usada no laço de repetição(vai ser alterada)
escolha = 0

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