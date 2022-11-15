from carro import Carro

print("*"*30, "Concessionária", "*"*30)

carro = Carro(input("Digite a Marca:> "),
input("Digite o Modelo:> "),
input("Digite a Cor:> "),
input("Digite a Categoria:> "))

print("*"*30)
print(f"a marca do carro é {carro.marca} e o modelo do carro é {carro.modelo} da cor {carro.cor} e essa é a categoria é {carro.categoria}.")
print("*"*30)  
