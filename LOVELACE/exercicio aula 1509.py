from time import sleep
situacao='reprovado'
nome=0
sobrenome=0
idade=0
dicionario_alunos = {"Nome": nome,"sobrenome":sobrenome, "idade": idade, "situacao":situacao}
while dicionario_alunos['situacao']!='aprovado':
    nome=str(input("digite um nome: "))
    sobrenome=str(input("digite um sobrenome: "))
    idade=int(input("digite uma idade: "))
    lista_notas=[]
    dicionario_alunos = {"Nome": nome,"sobrenome":sobrenome, "idade": idade, "situacao":situacao}
    situacao = 'reprovado'
    for lista in range(0,2,1):
        nota = int(input("Digite sua nota: "))
        lista_notas.append(nota)

    media = sum(lista_notas)/len(lista_notas)

    if media>=7:
        for c in range(0,3):
            #sleep(2)
            print("*")
        dicionario_alunos['situacao']='aprovado'
print(dicionario_alunos['situacao'])

    


#print(f"{dicionario_alunos['Nome']} {dicionario_alunos['sobrenome']} {dicionario_alunos['idade']} {dicionario_alunos['situacao']}")
