menu_inicial = 1
    while menu_inicial != 0:
        print(f"{poli}MENU{poli}\n")
        menu_inicial = int(input("1. Pessoa fisica \n2. Pessoa juridica\n0.sair\n"))
        match menu_inicial:
            case 1:
                menu = int(input("1. criar pessoaFisica \n2. mostrar pessoaFisicas\n0.sair\n"))
                match menu:
                    case 1:
                        pessoaFisica=PessoaFisica()

                        pessoaFisica.titular = str(input("digite o nome do 1° titular: "))
                        pessoaFisica.cpf = str(input("digite o cpf: "))
                        pessoaFisica.saldoInicial = int(input("digite o saldo inicial: "))

                        print("deseja cadastrar um segundo titular: \n")
                        v=str(input('sim ou nao'))
                        if v=='sim':
                            pessoaFisica.segundoTitular = str(input("digite o nome do 2° titular: "))
                        create_pf(pessoaFisica)
                    case 2:
                        read_pf()


            case 2:
                menu = int(input("1. criar pessoas juridicas \n2. mostrar pessoas juridicas\n0.sair\n"))
                match menu:
                    case 1:
                        pessoaJuridica=PessoaJuridica()

                        pessoaJuridica.titular = str(input("digite o nome do 1° titular: "))
                        pessoaJuridica.cnpj = str(input("digite o cnpj: "))
                        pessoaJuridica.saldoInicial = int(input("digite o saldo inicial: "))
                        print("deseja cadastrar um segundo titular: \n")
                        v=str(input('sim ou nao'))
                        if v=='sim':
                            pessoaJuridica.segundoTitular = str(input("digite o nome do 2° titular: "))
                        create_pj(pessoaJuridica)
                    case 2:
                        read_pj()