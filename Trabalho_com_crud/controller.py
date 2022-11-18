from conta import Conta

def create(conta):
    #Variavel d referencia para txt
    contas = open("contas.txt", "a")
    #Variavel d referencia de escrita
    contas.write(str(conta)+"\n")
    #Variavel d referancia fechando o arquivo
    contas.close

def read(): 
    #Lista vazia
    lista_contas = []
    #Variavel d referencia para txt
    contas = open("contas.txt", "r")
    #for com varavel percorrendo arquivo txt
    for conta in contas:
        #Variavel recebendo funcao internalizada para retirar espacos
        conta = conta.strip()
        #Variavel recebendo funcao internalizada de condicao para o indice
        conta__objeto = conta.split("; ")
        #printando objeto
        '''print(conta__objeto)'''
        #Variavel referencia objeto
        conta = Conta() 
        #setter recebendo um indice
        conta.titular = conta__objeto[0]
        #setter recebendo um indice
        conta.numero = conta__objeto[1]
        #setter recebendo um indice
        conta.saldo = conta__objeto[2]
        
        lista_contas.append(conta)
    contas.close
    return lista_contas

