from time import sleep

soma=0
a="="*10
print(f"{a}Cabeçalho{a}\n")

for c in range(0,3,1):
    b= int(input("digite um numero: "))
    soma=soma+b

print("A soma entre os valores digitados deu: {}".format(soma))

print(f"{a}Rodapé{a}")

print(f"{a}Cabeçalho{a}\n")

if soma>10:
    print("maior que 10 e diferente de 10")
elif soma==10:
    print("igual a 10 ")
elif soma< 10:
    print("menor que 10 e diferente de 10")

print(f"{a}Rodapé{a}")

