from animal import Animal

print("*"*30, "Petshop", "*"*30)

animal = Animal(input("Digite a espeice:> "),
input("Digite a Raça:> "),
float(input("Digite o Porte:> ")),
input("Digite a Cor:> "))

print("*"*30)
print(f"a espécie do animal é {animal.especie} a raça dele é {animal.raça} e esse é o porte {animal.porte} e a cor do animal é {animal.cor}.")
print("*"*30) 