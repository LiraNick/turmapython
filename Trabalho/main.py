from conta import Conta
from controller import create, read

def menu():

    print("="*30, "Menu Do Banco", "="*30)
    
    menu = 1
    while(menu != 0):
        menu = int(input("\n1.Criar Conta: \n2.Mostrar Estatisticas da Conta: \n3.Sair: \n\nR:>"))
        match menu:

            case 1:
                conta = Conta()

                conta.titular=str(input("Digite Seu Nome:> "))
                conta.numero=int(input("Digite o Numero:> "))
                conta.saldo=float(input("Digite Seu Saldo:> "))
                create(conta)

            case 2:
                
                lista_contas = read()
                #print(lista_contas)
                #print("="*30)
                for c in lista_contas:
                    print(c)

            case _:
                print("Tchau gatão")
                break


menu()