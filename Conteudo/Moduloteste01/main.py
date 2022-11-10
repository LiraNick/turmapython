import controller

print(("="*10),"CALCULADORA", ("="*10))


print("4. Divisão ")
print("3. Multiplicação")
print("2. Subtrair")
print("1. Somar")
print("0. Sair")

print(("="*13),"RODAPE", ("="*13))

var = 1

while (var!=0):
    
    var = int(input("digite a operação selecionada:"))
    match var:
        case 1:
            n1=float(input("digite o primeiro valor:"))
            n2=float(input("digite o segundo valor:"))
            print(controller.soma(n1,n2))
        case 2:
            n1=float(input("digite o primeiro valor:"))
            n2=float(input("digite o segundo valor:"))
            print(controller.subtracao(n1,n2))
        case 3:
            n1=float(input("digite o primeiro valor:"))
            n2=float(input("digite o segundo valor:"))
            print(controller.multiplicacao(n1,n2))
        case 4:
            n1=float(input("digite o primeiro valor:"))
            n2=float(input("digite o segundo valor:"))
            print(controller.divisao(n1,n2))
        case _:
            pass