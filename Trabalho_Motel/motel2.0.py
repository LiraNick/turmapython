import datetime
from time import sleep
from controller import checkin
from controller import relatorio
from controller import procurar

now = datetime.datetime.now()
hour = now.hour
def menu():
    if hour < 12:
        saudacao = "Bom dia, flor do dia"
    elif hour < 18:
        saudacao = "Boa tarde, forasteiro"
    else:
        saudacao = "Boa noite, meu consagrado"

    print('-'*20, 'HOTEL', '-'*20 )
    print("\n{}!\n".format(saudacao))

    opcao = 1

    while (opcao!=5):
        print("1 -> Fazer Check-in")
        print("2 -> Relatório Hospedes")
        print("3 -> Procurar Hospedes")
        print("4 -> Fazer Check-Out")
        print("5 -> Finalizar Atendimento")
        

        opcao = int(input("Opção: "))
        
        if(opcao==1):
            checkin()
        if(opcao==2):
            relatorio()
        if(opcao==3):
            procurar()
        if(opcao==4):
            checkout()
        else:()

menu()



