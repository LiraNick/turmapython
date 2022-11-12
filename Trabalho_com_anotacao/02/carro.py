class Carro:
    #Metodo Construtor 
    def __init__(self, marca, modelo, cor, categoria):
        self.__marca = marca
        self.__modelo = modelo 
        self.__cor = cor 
        self.__categoria = categoria 

    @property #getter
    def marca(self):
        return self.__marca
    @marca.setter #setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def modelo(self):
        return self.__modelo
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def cor(self):
        return self.__cor
    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @property
    def categoria(self):
        return self.__categoria
    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria

    def __str__(self):
        return f"Marca:> {self.marca}\nModelo:> {self.modelo}\nCor:> {self.cor}\nCategoria:> {self.categoria}"
