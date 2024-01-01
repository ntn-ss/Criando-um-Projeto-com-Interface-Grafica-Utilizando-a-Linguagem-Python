from Esfera import Esfera

bola1 = Esfera('Vermelha', 4)
bola2 = Esfera('Azul', 8)

bola1.calcula_area()
bola1.calcula_volume()

bola2.calcula_area()
bola2.calcula_volume()

Esfera.calcula_area(bola1)
Esfera.calcula_volume(bola2)