def salvar(nome):
    with open("Modulo02/pessoas.txt", "a") as arquivo:
        arquivo.write(f"{nome}\n")

def listar():
    nomes = []
    with open("Modulo01/pessoas.txt", "r") as arquivo:
        for name in arquivo:
            name = name.strip()
            nomes.append(name)

    return nomes

#salvar("LirinhaBoladao")
print("lista de nomes", listar())