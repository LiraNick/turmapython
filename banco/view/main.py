from model.pessoafisica import PessoaFisica
from model.pessoajuridica import PessoaJuridica
from controller.juridico import create_pj, read_pj
from controller.fisico import create_psf, read_psf

def menu():
    menu = 1
    while(menu != 0):
        print("="*30, "Menu Principal", "="*30)
        print("\n1.Pessoa Fisica \n2.Pessoa Juridica")
        menu_inical = int(input("Digite o Tipo:"))
        match menu_inical:
            case 1:
                menu = int(input("1.Criar PessoaFisica:> \n2.Listar PessoasFisicas:> \n0.sair:> \n"))
                match menu:
                    case 1:
                        pessoafisica = PessoaFisica()

                        pessoafisica.titular = str(input("Digite o Nome do 1° titular:> "))
                        pessoafisica.cpf = int(input("Digite o Cpf:> "))
                        pessoafisica.saldo_inicial = float(input("Digite o Saldo Inicial:> "))

                        print("Deseja Cadastrar um Segundo Titular:> \n")
                        v=str(input('sim ou nao:> '))
                        if v=='sim':
                            pessoafisica.segundo_titular = str(input("Digite o Nome do 2° Titular:> "))
                        create_psf(pessoafisica)
                    case 2:
                        read_psf()


            case 2:
                menu = int(input("1.Criar PessoaJuridica:> \n2.Listar PessoasJuridias:> \n0.sair:> \n"))
                match menu:
                    case 1:
                        pessoajuridica=PessoaJuridica()

                        pessoajuridica.titular = str(input("Digite o Nome do 1° titular:> "))
                        pessoajuridica.cnpj = input("Digite o Cnpj:> ")
                        pessoajuridica.saldo_inicial = float(input("Digite o Saldo Inicial:> "))

                        print("Deseja Cadastrar um Segundo Titular:> \n")
                        v=str(input('sim ou nao:> '))
                        if v=='sim':
                            pessoajuridica.segundo_titular = str(input("digite o nome do 2° titular: "))
                        create_pj(pessoajuridica)
                    case 2:
                        read_pj()