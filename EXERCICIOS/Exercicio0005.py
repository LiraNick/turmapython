#EXERCICIO-03 crie um documento instanciando uma classe chamada pessoa, crie a função construtor, com a variável referência que acessa os atributos da classe no espaço alocado de memória.  defina os atributos diretamente na função construtor nome, SobreNome, idade, cpf, crie um segundo documento main com variável pessoa 1, pessoa 2, pessoa 3 , insira valores diferentes para cada objeto, imprima no terminal o espaço  alocado de memória do objeto principal , do objeto principal  e de cada variável de referência para o objeto!
class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        print(f"Imprimindo variavel de referencia{self}")


        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

