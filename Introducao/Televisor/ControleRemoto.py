class ControleRemoto:
    def __init__(self, tv):
        self.tv = tv
    
    def aumentaVolume(self, valor):
        self.tv.aumentaVolume(valor)
    
    def diminuiVolume(self, valor):
        self.tv.diminuiVolume(valor)
    
    def trocaCanal(self, canal):
        self.tv.trocaCanal(canal)
        
    def sintonizaCanal(self, canal):
        self.tv.sintonizaCanal(canal)
        
    def listaDeCanais(self):
        self.tv.getListaDeCanais()