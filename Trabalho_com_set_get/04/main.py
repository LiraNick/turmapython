from animal import Animal

print("*"*30, "PetShop", "*"*30)

animal = Animal(input("Digite a Espécie:> "),
input("Digite a Raça:> "),
float(input("Digite o Porte:> ")),
input("Digite a Cor:> "))

print("*"*30)
print("a espécie do animal é {} a raça dele é {} e esse é o porte {} e a cor do animal.".format(animal.get_especie(), animal.get_raça(), animal.get_porte(), animal.get_cor()))
print("*"*30)