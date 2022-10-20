from controller import SomaSalario

def menu():
    print("="*15, "CALCULADORA DE SALARIO", "="*15, "\n")

    var = "sim"
    while var == "sim":
        n1 = float(input("Digite seu primeiro salario: "))
        n2 = float(input("Digite seu segundo salario: "))
        n3 = float(input("Digite seu terceiro salario: "))
        n4 = float(input("Digite seu quarto salario: "))

        resultado = SomaSalario(n1, n2, n3, n4)
        print("a soma dos salarios é: {:.2f}".format(resultado))

        var = str(input("Você deseja continuar \nSim \nNão\n:>"))

menu()
print("Você saiu do programa")