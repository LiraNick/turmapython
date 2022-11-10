class Animal:
    def __init__(self, especie, raça, porte, cor):
        self.__especie = especie
        self.__raça = raça
        self.__porte = porte
        self.__cor = cor 

    def set_especie(self, especie):
        self.__especie = especie
    def get_especie(self):
        return self.__especie

    def set_raça(self, raça):
        self.__raça = raça
    def get_raça(self):
        return self.__raça

    def set_porte(self, porte):
        self.__porte = porte
    def get_porte(self):
        return self.__porte

    def set_cor(self, cor):    
        self.__cor = cor
    def get_cor(self):
        return self.__cor

    def __str__(self):
        return f"Espécie:> {self.get_especie()}\nRaça:> {self.get_raça()}\nPorte:> {self.get_porte()}"