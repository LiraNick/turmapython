def fazerCheckin(cliente):
    with open('hotel/hotel.txt', 'a') as arquivo:
        arquivo.write(str(cliente)+"\n")


def relatorioHospedes():
    with open('hotel/hotel.txt') as arquivo:  
        print(arquivo.read())


def procurarHospedes(clienteFind):
    index=0
    flag=0
    arquivo = open("hotel/hotel.txt", "r") 
    for line in arquivo:
        index +=1
        if clienteFind == ['nome']:
            print(line)
            flag =1
    if flag == 0:
        print("Cliente não encontrado")


def fazerCheckout(clientefind):
    try:
        with open('hotel/hotel.txt', 'r') as fr:
        # reading line by line
            lines = fr.readlines()
            index = 0
            clienteFind=str(input("Digite o nome desejado:"))
            with open('months.txt', 'w') as fw:
                for line in lines:
                    index += 1
                    if clienteFind == ['nome']:
                        fw.write(line)
                    
    except:
        print("Oops! algo deu errado!")      
