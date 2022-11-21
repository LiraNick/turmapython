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
        conta__objeto = conta.split(";")
        #printando objeto
        print(conta__objeto)
        #Variavel referencia objeto
    contas.close()
    return lista_contas

def update(conta_update:Conta):
    lista_contas = []
    arquivo = open("contas.txt", "r")
    for conta in arquivo:
        conta_limpa = conta.strip()
        conta_objeto = conta_limpa.split(";")
        if conta_update.numero == int(conta_objeto[1]):
            lista_contas.append(conta_update)
        else:
            lista_contas.append(conta)
    arquivo.close()    

    arquivo = open("contas.txt", "w")    
    for con in lista_contas:
        arquivo.write(str(con))     
    arquivo.close()    




def delete(conta_update:Conta):
    lista_contas = []
    arquivo = open("contas.txt", "r")
    for conta in arquivo:
        conta_limpa = conta.strip()
        conta_objeto = conta_limpa.split(";")
        if conta_update.numero != int(conta_objeto[1]):
            lista_contas.append(conta)
    arquivo.close()

    arquivo = open("contas.txt", "w")
    arquivo.writelines(str(lista_contas))
    arquivo.close()
    arquivo = open("contas.txt", "w")    
    for con in lista_contas:
        arquivo.write(str(con))     
    arquivo.close()  
