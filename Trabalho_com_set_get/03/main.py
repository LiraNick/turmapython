from carro import Carro

print("*"*30, "Concessionária", "*"*30)

carro = Carro(input("Digite a Marca:> "), 
input("Digite o Modelo:> "),
input("Digite a Cor:> "),
input("Digite a Categoria:> "))

print("*"*30)
print("a Marca do carro é {} e é do modelo {} de cor {} e da categoria {}.".format(carro.get_marca(), carro.get_modelo(), carro.get_cor(), carro.get_categoria()))
print("*"*30)