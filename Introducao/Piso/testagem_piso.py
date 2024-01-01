from Piso import Piso
from Azulejo import Azulejo

azulejo = Azulejo(90, 30)
piso = Piso(azulejo, 50, 20)

print(azulejo.calcula_area())
print(piso.calculaArea())
print(piso.calculaAzulejos())
print(piso.trocaAzulejo(azulejo))