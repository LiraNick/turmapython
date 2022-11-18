from model.pessoajuridica import PessoaJuridica

pessoajuridica = PessoaJuridica()
def create_pj(conta):
    contas = open("pessoajuridica.txt", "a")
    contas.write(str(conta)+"\n")
    contas.close()

def read_pj():
    lista_contas = []
    contas = open("pessoajuridica.txt", "r")
    
    for conta in contas:
        conta = conta.strip()
        conta_objeto = conta.split(";")
        print(conta_objeto)
        pessoajuridica.agencia = conta_objeto[0]
        pessoajuridica.numero_agencia = conta_objeto[1]
        pessoajuridica.segundo_titular = conta_objeto[2]
        pessoajuridica.titular = conta_objeto[3]
        pessoajuridica.cnpj = conta_objeto[4]
        pessoajuridica.saldo_inicial = conta_objeto[5]

        lista_contas.append(conta)
        
        
    contas.close()
    return lista_contas