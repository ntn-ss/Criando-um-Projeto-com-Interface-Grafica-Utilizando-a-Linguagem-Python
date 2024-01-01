class Televisor:
    def __init__(self, fab, modelo):
        self.fab = fab 
        self.modelo = modelo 
        self.__canal_atual = None
        self.__lista_de_canais = []
        self.__volume = 20
        
    def getVolume(self):
        return f'O volume agora é {self.__volume}.'

    def getCanal(self):
        return f'O canal agora é {self.__canal_atual}.'
        
    def getListaDeCanais(self):
        for indice, valor in enumerate(self.__lista_de_canais):
            print(f'Canal {indice}: {valor}.')
        
    def aumentaVolume(self, valor):
        self.__volume = self.__volume+valor if self.__volume+valor <= 100 else 100
        print(self.getVolume())

    def diminuiVolume(self, valor):
        self.__volume = self.__volume-valor if self.__volume-valor >= 0 else 0
        print(self.getVolume())
        
    def trocaCanal(self, canal):
        if canal in self.__lista_de_canais:
            self.__canal_atual = canal
            print(self.getCanal())
        else:
            print(f"Antes, sintonize o canal '{canal}'.")
            
    def sintonizaCanal(self, canal):
        if canal not in self.__lista_de_canais:
            self.__lista_de_canais.append(canal)
        else:
            print(f"Canal '{canal}' já sintonizado.")