from conta import Conta
from controller import create, read, update, delete

def menu():

    print("="*30, "Menu Do Banco", "="*30)
    
    menu = 1
    while(menu != 0):
        menu = int(input("\n1.Criar Conta: \n2.Mostrar Estatisticas: \n3.Update Numero: \n4.Deletar Conta: \n\nR:>"))
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

            case 3:
                conta = Conta()
                conta.numero = 500
                conta.saldo = 800
                conta.titular = "lirinha"
                update(conta)

            case 4:
                conta = Conta()
                conta.numero = 500
                delete(conta)


menu()