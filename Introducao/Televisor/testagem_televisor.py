from ControleRemoto import ControleRemoto
from Televisor import Televisor

minha_tv = Televisor('CCE', 'Lixo')
meu_controle = ControleRemoto(minha_tv)

meu_controle.aumentaVolume(50)

meu_controle.trocaCanal('Gazeta')
meu_controle.sintonizaCanal('Gazeta')
meu_controle.trocaCanal('Gazeta')
meu_controle.sintonizaCanal('Gazeta')

meu_controle.sintonizaCanal('Record')
meu_controle.sintonizaCanal('SBT')
meu_controle.sintonizaCanal('Rede TV')
meu_controle.listaDeCanais()

meu_controle.aumentaVolume(1000000)
meu_controle.diminuiVolume(1000001)
meu_controle.aumentaVolume(20)