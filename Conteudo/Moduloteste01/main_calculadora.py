#from controller import soma, subtracao, divisao, multiplicacao
import controller

def menu():
    print(("="*10),"MENU", ("="*10))

    cond = "sim"
    while cond =="sim":
        n1 = int(input("Digite o primeiro numero:"))
        n2 = int(input("Digite o segundo numero:"))

        opcao = int(input("1-soma \n2-subtracao \n3-divisao \n4-multiplicacao\n operacao>"))

        match opcao:
            case 1:
                print(f"O resultado da soma é {controller.soma(n1,n2)}")
            case 2:
                print(f"O resultado da subtracao é {controller.subtracao(n1,n2)}")
            case 3:
                print(f"O resultado da divisao é {controller.divisao(n1,n2)}")
            case 4:
                print(f"O resultado da multiplicacao é {controller.multiplicacao(n1,n2)}")
            case _:
                print("Digite uma opcao valida")

        soma = controller.soma(n1,n2)
        subtracao = controller.subtracao(n1,n2)
        divisao = controller.divisao(n1,n2)
        multiplicacao = controller.multiplicacao(n1,n2)


        cond = str(input("Deseja continuar?\nsim\nnão\n:>"))

menu()

print("Você saiu da aplicacao!")