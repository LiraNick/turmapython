from ast import Import
from datetime import datetime
from time import sleep

from controller import fazerCheckin, relatorioHospedes, procurarHospedes, fazerCheckout


def menu():
    print(("="*20),"Motelzin", ("="*20))
    #menu
    menu=1
    agora=datetime.now(tz=None)
    if agora.hour >=5 and agora.hour<13:
        print("\nBom dia")
    if agora.hour >=13 and agora.hour<18:
        print("\nBoa tarde")
    else:
        print("\nBoa noite")
    while(menu!=0):
        print("Por Favor Escolha a opção desejada:\n")
        menu=int(input("1.Fazer checkin\n2.Relatorio hospedes\n3.Procurar hospedes\n4.Fazer checkout\n0.Finalizar atendimento\noperacao>:"))
        match menu:
                case 1:
                    cliente={}
                    cliente["nome"]=str(input("Digite seu nome:"))
                    cliente["cpf"]=int(input("Digite seu cpf:"))
                    cliente["idade"]=int(input("Digite sua idade:"))
                    cliente["telefone"]=int(input("Digite seu telefone:"))
                    fazerCheckin(cliente)
                case 2:
                    relatorioHospedes()
                case 3:
                    clienteFind=str(input("Digite o nome desejado:"))
                    procurarHospedes(clienteFind)
                case 4:
                    clienteFind=str(input("Digite o nome desejado:"))
                    fazerCheckout(clienteFind)
                case _:
                    print("Digite uma opcao valida")

menu()