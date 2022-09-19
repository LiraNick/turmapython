#crie uma variavel para receber um numero de 1 a 10.
#mostre a tabuada do numero informado.

num = int(input("Digite um numero de 0 a 10: "))

for c in range(0, 11):
    resultado = (num*c)
    print(f"{num} x {c} = {resultado}")