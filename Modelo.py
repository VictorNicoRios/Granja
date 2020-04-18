class Animal:
    def __init__(self, in_Nombre, in_Raza, in_Peso, in_Hambre, in_Sed, in_Vacunado):
        self.Nombre = in_Nombre
        self.Raza = in_Raza
        self.Peso_Kg = in_Peso
        self.Hambre = in_Hambre
        self.Sed = in_Sed
        self.Vacunado = in_Vacunado

    def MostrarNombre(self):
        print(self.Nombre)

    def Beber(self):
        if self.Raza == 'Vaca':
            self.Sed = False
            self.Peso_Kg-=0.500

    def Vacunar(self):
        self.Vacunado = True

class Vaca(Animal):
    #Se definen las clases de cada animal con unos valores pre-establecidos para enviarle a la superclase Animales.
    #Cada animal sólo espera que le ingresen su nombre al crearlo
    def __init__(self, in_Nombre_Vaca):
        self.Nombre = in_Nombre_Vaca
        self.Raza = 'Vaca'
        self.Peso_Kg = 200
        self.Hambre = True
        self.Sed = True
        self.Vacunado = False
        super().__init__(self.Nombre, self.Raza, self.Peso_Kg, self.Hambre, self.Sed, self.Vacunado)
    
    def Comer(self, Peso_X_Racion_Kg, Cant_lo_que_alimenta):
        print('*La vaca come*')
        #Para saber cúanto pesa lo que come se le manda el peso de la unidad de comida x la cantidad de unidades que va a comer.
        #El peso de lo que come se agrega al peso de la vaca
        self.Peso_Kg += (Peso_X_Racion_Kg * Cant_lo_que_alimenta)/3
        self.Hambre = (Peso_X_Racion_Kg * Cant_lo_que_alimenta) <= 200
        self.Sed = (Peso_X_Racion_Kg * Cant_lo_que_alimenta) >= 200

class Gallina(Animal):
    def __init__(self, in_Nombre_Gallina):
        self.Nombre = in_Nombre_Gallina
        self.Raza = 'Gallina'
        self.Peso_Kg = 2.5
        self.Hambre = True
        self.Sed = True
        self.Vacunado = False
        super().__init__(self.Nombre, self.Raza, self.Peso_Kg, self.Hambre, self.Sed, self.Vacunado)

class Cerdo(Animal):
    def __init__(self, in_Nombre_Cerdo):
        self.Nombre = in_Nombre_Cerdo
        self.Raza = 'Cerdo'
        self.Peso_Kg = 80
        self.Hambre = True
        self.Sed = True
        self.Vacunado = False
        super().__init__(self.Nombre, self.Raza, self.Peso_Kg, self.Hambre, self.Sed, self.Vacunado)

class Comedero:
    def __init__(self, in_Tipo_Comedero, in_Raciones_Restantes, in_Cant_Raciones, in_Cant_Maxima):
        self.Tipo_Comedero=in_Tipo_Comedero
        self.Raciones_Restantes=in_Raciones_Restantes
        self.Peso_X_Racion_Kg=0.500
        self.Cant_lo_que_alimenta=in_Cant_Raciones
        self.Cant_Maxima = in_Cant_Maxima

class ComederoManual(Comedero):
    def __init__(self, in_Cant_Alimenta, in_Peso_Soportado):
        self.Cant_lo_que_alimenta=in_Cant_Alimenta
        self.Peso_Animal_Soportado=in_Peso_Soportado
        super().__init__('Normal', 20, self.Cant_lo_que_alimenta, 0)

    #Sólo pide al objeto que va a alimentar (para saber su peso y ejecutar su función comer)
    def AlimentarAnimal(self, In_Animal):
        #Si la variable Peso_Kg (Peso en Kg del animal) es mayor al peso máximo de animal que soporta el comedero (valor que se definió al instanciarlo)
        if In_Animal.Peso_Kg <= self.Peso_Animal_Soportado:
            #Ejecuta la función comer de ese objeto
            In_Animal.Comer(self.Peso_X_Racion_Kg, self.Cant_lo_que_alimenta)
        else:
            print('*Peso de animal no soportado para este comedero*')
    
    def Recargar_Comedero(self):
        if self.Raciones_Restantes < 10:
            self.Raciones_Restantes += 30
            print('*Comedero Manual: Se han recargado 30 raciones*')
        else:
            print('Este comedero tadavía tiene raciones suficientes, por tanto no se recarga')
    
class ComederoAutomatico(Comedero):
    def __init__(self, in_Cant_Maxima):
        self.Cant_Maxima=in_Cant_Maxima
        super().__init__('Automatico', self.Cant_Maxima, 0, self.Cant_Maxima)

    def AlimentarAnimal(self, In_Animal):
    #Se ejecuta si el objeto animal introducido tiene hambre
        if In_Animal.Hambre == True:
            self.Cant_lo_que_alimenta = In_Animal.Peso_Kg/100
            In_Animal.Comer(self.Peso_X_Racion_Kg, self.Cant_lo_que_alimenta)
        else:
            print('*Comedero Automático: No puedo alimentar a este animal porque no tiene hambre*')

    def Recargar_Comedero(self):
        if self.Raciones_Restantes < 15:
            self.Raciones_Restantes == self.Cant_Maxima
            print('Se han recargado al máximo de raciones')
        else:
            print('Este comedero tadavía tiene raciones suficientes, por tanto no se recarga')

class Bebedero:
    def __init__(self):
        super().__init__()

class Vacunatorio:
    def __init__(self):
        super().__init__()

newvaca=Vaca('Lola')
newcomederocomun=ComederoManual(500, 200)
newvaca.MostrarNombre()
newcomederocomun.AlimentarAnimal(newvaca)
print(newvaca.Sed)
print(newvaca.Hambre)
print(newvaca.Peso_Kg)
newcomederocomun.AlimentarAnimal(newvaca)
newauto=ComederoAutomatico(50)
newauto.AlimentarAnimal(newvaca)