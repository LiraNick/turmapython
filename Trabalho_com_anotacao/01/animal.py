class Animal:
    #Metodo Construtor 
    def __init__(self, especie, raça, porte, cor):
        self.__especie = especie
        self.__raça = raça 
        self.__porte = porte 
        self.__cor = cor 

    @property #getter
    def especie(self):
        return self.__especie
    @especie.setter #setter
    def especie(self, especie):
        self.__especie = especie

    @property
    def raça(self):
        return self.__raça
    @raça.setter
    def raça(self, raça):
        self.__raça = raça

    @property
    def porte(self):
        return self.__porte
    @porte.setter
    def porte(self, porte):
        self.porte = porte

    @property
    def cor(self):
        return self.__cor
    @cor.setter
    def cor(self, cor):
        self.cor = cor

    def __str__(self):
        return f"Especie:> {self.especie}\nRaça:> {self.raça}\nPorte:> {self.porte}\nCor:> {self.cor}"
