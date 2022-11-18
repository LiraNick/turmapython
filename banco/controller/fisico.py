from model.pessoafisica import PessoaFisica

pessoafisica = PessoaFisica()
def create_psf(conta):
    contas = open("pessoafisica.txt", "a")
    contas.write(str(conta)+"\n")
    contas.close()

def read_psf():
    lista_contas = []
    contas = open("pessoafisica.txt", "r")
    
    for conta in contas:
        conta = conta.strip()
        conta_objeto = conta.split(";")
        print(conta_objeto)
        pessoafisica.agencia = conta_objeto[0]
        pessoafisica.numero_agencia = conta_objeto[1]
        pessoafisica.segundo_titular = conta_objeto[2]
        pessoafisica.titular = conta_objeto[3]
        pessoafisica.cpf = conta_objeto[4]
        pessoafisica.saldo_inicial = conta_objeto[5]

        lista_contas.append(conta)
        contas.close
        return lista_contas
