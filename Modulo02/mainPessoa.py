from controller import salvar, listar

def menu():
    print("="*20, "menu", "="*20)

    cond = "sim"
    while cond == "sim":
        nome = salvar
        var = str(input("deseja continuar \n sim \n não \n :>"))

menu ()

print("A lista de nomes inseridos\n")