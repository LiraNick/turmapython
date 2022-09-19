# crie uma variável do tipo inteiro recebendo dados,

# crie uma variável fazendo o cálculo do resto da divisão, usando máscara de substituição e realize a atribuição do valor.

# logo em seguida crie uma estrutura de condição onde irá imprimir no terminal se o cálculo da divisão e impar ou par


inteiro = 10
a = inteiro%2
print("Resto da divisao é {}\n".format(a))

if a == 0:
    print("O resultado da divisão é {}, portanto o numero é par".format(a))
else:
    print("O resultado da divisão é {}, portanto o numero é impar".format(a)) 
    