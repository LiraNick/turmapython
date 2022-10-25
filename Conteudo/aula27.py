from time import sleep

def contador(inicio, fim, passo):
    print("="*30, "CONTADOR", "="*30)
    passo = abs(passo) if passo != 0 else 1
    # definindo o passo com o valor absoluto (deixa sinal positivo), e caso seja zero, recebe 1
    print(f"contagem de {inicio} ate {fim}, de {passo} em {passo}")
    sleep(1.5)

    if  inicio < fim:
        for cont in range(inicio, fim +1, passo):
            print(cont, end="")
            sleep(0.3)
    elif inicio > fim:
        for cont in range(inicio, fim -1, passo):
            print(cont, end="")
            sleep(0.3)
        print("Funcionando")




#chamando a funcao

contador(10, 30, 2)

print ("="*30,"Personalize seu for", "="*30)
contador(int(input("inicio: ")), int(input("fim: ")), int(input("passo: ")))