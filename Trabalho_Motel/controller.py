def checkin():
    hospede = {}
    hospede['Nome'] = str(input('Seu nome: '))
    hospede['sobreNome'] = str(input('Seu sobrenome: '))
    hospede['idade'] = int(input('Sua idade: '))
    hospede['cpf'] = int(input('Seu cpf: '))
    with open('Trabalho_Motel/hotel.txt', 'a') as arquivo:
        arquivo.write(str(hospede)+'\n')

def relatorio():
    with open('Trabalho_Motel/hotel.txt', 'r') as arquivo:  
        print(arquivo.read())

def procurar():
    hospedeFind = str(input("Digite o nome desejado:"))
    index=0
    flag=0
    arquivo = open("hotel/hotel.txt", "r") 
    for line in arquivo:
        index +=1
        if hospedeFind == ['Nome']:
            print(line)
            flag = 1
    if flag == 0:
        print("Hospede não encontrado")




