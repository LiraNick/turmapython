from ast import Import
from datetime import datetime
from time import sleep
from controller import checkin
from controller import relatorio
from controller import procurar

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
                    checkin()
                case 2:
                    relatorio()
                case 3:
                    hospedeFind=str(input("Digite o nome desejado:"))
                    procurar()
                case 4:
                    hospedeFind=str(input("Digite o nome desejado:"))
                    ()
                case _:
                    print("valeu cachorro ate uma proxima!")

