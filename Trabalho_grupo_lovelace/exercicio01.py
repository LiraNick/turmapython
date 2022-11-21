# crie uma variável do tipo inteiro recebendo dados,

# crie uma variável fazendo o cálculo do resto da divisão, usando máscara de substituição e realize a atribuição do valor.

# logo em seguida crie uma estrutura de condição onde irá imprimir no terminal se o cálculo da divisão e impar ou par


inteiro = int(input("Digite um valor: "))
a = inteiro%2

if a == 0:
    print("O valor é {}, portanto o numero é par".format(inteiro))
else:
    print("O valor é {}, portanto o numero é impar".format(inteiro)) 
    