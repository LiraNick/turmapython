#OK - crie uma variável recebendo o conceito de polimorfismo com o sinal de igual.
#OK - crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string cabecalho adicione quebra de linha, ao final.
#OK - crie um laco de repeticao recebendo uma condição que irá executar apenas números pares esses números devem percorrer até 1500.
#OK - crie uma função de impressão após laco com a descrição parabéns você conseguiu!
#OK - crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string utilize como rodapé, definindo o fim do laço repetição!

poli = "="*20

print(f"\n {poli} CABECALHO {poli} \n")

for cont in range(0, 1500, 1):
    if cont %2 == 0:
        print(cont)

print("Parabéns! Você conseguiu!")

print(f"\n {poli} RODAPE {poli} \n")