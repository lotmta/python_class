'''
NAME
	CellSim.py
    
VERSION
    1.0
    
AUTHOR
	Lot Hernandez	
    
DESCRIPTION
    Simula el crecimiento de una poblacion de celulas

CATEGORY
	Genomic Sequence
    
USAGE
    py RNAtoPROTEIN.py -n (Nombre) -d (Dias) -p (PoblacionIn) -t (TasaCrecimiento) -m (PoblacionMaxima)
    py RNAtoPROTEIN.py -n (Nombre) -d (Dias) -p (PoblacionIn) -t (TasaCrecimiento) 

'''
import argparse

parser = argparse.ArgumentParser(
    description="")

parser.add_argument("-n", "--nombre",
                    help="Introduce el nombre de tus celulas",
                    required=True)
parser.add_argument("-d", "--dias",
                    help="Introduce el numero de dias que van a pasar en tu simulacion",
                    required=True)
parser.add_argument("-p", "--poblacion",
                    help="Introduce el tamano de tu poblacion inicial",
                    required=True)
parser.add_argument("-t", "--tasa",
                    help="Introduce la tasa de crecimiento por dia",
                    required=True)
parser.add_argument("-m", "--maxpob",
                    help="Introduce el tamano maximo de tu poblacion",
                    required=False)
args = parser.parse_args()

# Clase para poblacion de celulas que pueden crecer sin limite
class SimCelulas():
    nombre = ''
    dias = 0
    poblacion = 0
    tasa = 0

    def __init__(self, nombre, dias, poblacion, tasa):
        self.nombre = nombre
        self.dias = dias
        self.poblacion = poblacion
        self.tasa = tasa

    # Funcion para calcular el crecimiento de la poblacion sin limite
    def simulacion(self):
        for dia in self.dias:
            self.poblacion += self.tasa * self.poblacion


# Clase para poblacion de celulas que tienen un tamano limite
class SimCelulasMaxPob(SimCelulas):
    if(args.maxpob):
        maxpob = float(args.maxpob)

    # Funcion para calcular el crecimiento de la poblacion tomando en cuenta el limite de esta
    def simulacion(self):
        for dia in self.dias:
            self.poblacion += self.tasa * self.poblacion * ( ( self.maxpob - self.poblacion ) / self.maxpob )

# Se checa si el usuario introdujo una poblacion maxima o no, para ver a que clase meter la poblacion de celulas
if (args.maxpob):
    CelUsr = SimCelulasMaxPob(args.nombre, args.dias, float(args.poblacion), float(args.tasa))
else:
    CelUsr = SimCelulas(args.nombre, args.dias, float(args.poblacion), float(args.tasa))

# Se lleva a cabo la simulacion
CelUsr.simulacion()

# Se imprime el resultado
print("La poblacion de "+ CelUsr.nombre +" despues de " + CelUsr.dias +" dias sera de tamano:" )
print(CelUsr.poblacion)


