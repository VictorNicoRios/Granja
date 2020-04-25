#<--Animales-->

class Animal:
    def __init__(self, in_Nombre, in_Raza, in_Peso, in_Hambre, in_Sed, in_Vacunado):
        self.Nombre = in_Nombre
        self.Raza = in_Raza
        self.Peso_Kg = in_Peso
        self.Hambre = in_Hambre
        self.Sed = in_Sed
        self.Vacunado = in_Vacunado

    def MostrarNombre(self):
        print('El nombre de este animal es: "',self.Nombre,'"')

    def MostrarHambre(self):
        print('¿El animal "',self.Nombre,'" tiene hambre?:', self.Hambre)

    def MostrarSed(self):
        print('¿El animal "',self.Nombre,'" tiene sed?:', self.Sed)

    def MostrarPeso(self):
        print('El peso del animal "',self.Nombre,'" es:', self.Peso_Kg)

    def MostrarVacunado(self):
        print('¿El animal "',self.Nombre,'" está vacunado?:', self.Vacunado)

    def Beber(self):
        self.Sed = False

    def Vacunar(self):
        print('Vacunando a "',self.Nombre,'"')
        self.Vacunado = 1==1

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
    
    def Comer(self, in_Peso_de_Racion):
        print('[',self.Nombre,']: *Come*')
        #Para saber cúanto pesa lo que come se le manda el peso de la unidad de comida x la cantidad de unidades que va a comer.
        #El peso de lo que come se agrega al peso de la vaca
        self.Peso_Kg += (in_Peso_de_Racion)/3
        self.Hambre = self.Peso_Kg <= 200
        self.Sed = (in_Peso_de_Racion) >= 200

    def BeberVaca(self):
        self.Beber()
        self.Peso_Kg -= 0.500
    
    def Vacunar(self):
        if self.Vacunado==False:
            return super().Vacunar()
        else:
            print('El animal "',self.Nombre,'" ya está vacunado, no conviene vacunarlo nuevamente')

    def Caminata(self):
        self.Peso_Kg-=3

class Cerdo(Animal):
    def __init__(self, in_Nombre_Cerdo):
        self.Nombre = in_Nombre_Cerdo
        self.Raza = 'Cerdo'
        self.Peso_Kg = 80
        self.Hambre = True
        self.Sed = True
        self.Vacunado = False
        self.Kg_Comidos=0
        self.Maximo_Comido=0
        self.Veces_Seguidas_Comio=0
        super().__init__(self.Nombre, self.Raza, self.Peso_Kg, self.Hambre, self.Sed, self.Vacunado)
    
    def Comer(self, in_Peso_de_Racion):
        self.Kg_Comidos=in_Peso_de_Racion
        if in_Peso_de_Racion>0.200:
            self.Peso_Kg+=in_Peso_de_Racion-0.200
        self.Hambre=self.Kg_Comidos<=1
        if in_Peso_de_Racion >= self.Maximo_Comido:
            self.Maximo_Comido=in_Peso_de_Racion
        self.Veces_Seguidas_Comio+=1
        if self.Veces_Seguidas_Comio>3 & self.Sed==False:
            self.Sed=1==1
    
    def MaxComido(self):
        print('La vez que "',self.Nombre,'" más comió le dieron:',self.Maximo_Comido)
    
    def Vacunar(self):
        return super().Vacunar()
    
    def Beber(self):
        self.Sed=1!=1
        self.Veces_Seguidas_Comio=0
        self.Hambre=1==1

class Gallina(Animal):
    def __init__(self, in_Nombre_Gallina):
        self.Nombre = in_Nombre_Gallina
        self.Raza = 'Gallina'
        self.Peso_Kg = 4
        self.Hambre = True
        self.Sed = False
        self.Vacunado = False
        self.Veces_Comio = 0
        super().__init__(self.Nombre, self.Raza, self.Peso_Kg, self.Hambre, self.Sed, self.Vacunado)
    
    def Comer(self):
        print('*Comiendo...*')
        self.Veces_Comio+=1
    
    def Vacunar(self):
        print('Este animal no conviene vacunarlo')

#<--Atención automática-->

#-Comedero

class Comedero:
    def __init__(self, in_Tipo_Comedero, in_Raciones_Restantes, in_Cant_Raciones, in_Cant_Maxima):
        self.Tipo_Comedero=in_Tipo_Comedero
        self.Raciones_Restantes=in_Raciones_Restantes
        self.Peso_X_Racion_Kg=0.500
        self.Cant_Raciones=in_Cant_Raciones
        self.Cant_Maxima = in_Cant_Maxima
        self.Peso_Racion_Dada=self.Peso_X_Racion_Kg*self.Cant_Raciones

class ComederoManual(Comedero):
    def __init__(self, in_Cant_Alimenta, in_Peso_Soportado):
        self.Cant_Raciones=in_Cant_Alimenta
        self.Peso_Animal_Soportado=in_Peso_Soportado
        super().__init__('Normal', 20, self.Cant_Raciones, 0)

    #Sólo pide al objeto que va a alimentar (para saber su peso y ejecutar su función comer)
    def AlimentarAnimal(self, In_Animal):
        #Si la variable Peso_Kg (Peso en Kg del animal) es mayor al peso máximo de animal que soporta el comedero (valor que se definió al instanciarlo)
        if In_Animal.Peso_Kg <= self.Peso_Animal_Soportado:
            #Ejecuta la función comer de ese objeto
            print('*Alimentando al animal "', In_Animal.Nombre, '"*')
            In_Animal.Comer(self.Peso_Racion_Dada)
        else:
            print('[Comedero Manual]: Peso del animal "', In_Animal.Nombre, '" no soportado para este comedero')
    
    def Recargar_Comedero(self):
        if self.Raciones_Restantes < 10:
            self.Raciones_Restantes += 30
            print('[Comedero Manual]: Se han recargado 30 raciones')
        else:
            print('[Comedero Manual]: Este comedero tadavía tiene raciones suficientes (Raciones restantes:',self.Raciones_Restantes, '), por tanto no se recarga')
    
class ComederoAutomatico(Comedero):
    def __init__(self, in_Cant_Maxima):
        self.Cant_Maxima=in_Cant_Maxima
        super().__init__('Automatico', self.Cant_Maxima, 0, self.Cant_Maxima)

    def AlimentarAnimal(self, In_Animal):
    #Se ejecuta si el objeto animal introducido tiene hambre
        if In_Animal.Hambre == True:
            self.Cant_Raciones = In_Animal.Peso_Kg/100
            In_Animal.Comer(self.Peso_X_Racion_Kg, self.Cant_Raciones)
        else:
            print('[Comedero Automático]: No puedo alimentar al animal "',In_Animal.Nombre,'" porque no tiene hambre')

    def Recargar_Comedero(self):
        if self.Raciones_Restantes < 15:
            self.Raciones_Restantes == self.Cant_Maxima
            print('[Comedero Automático]: Se han recargado al máximo de raciones')
        else:
            print('[Comedero Automático]: Este comedero tadavía tiene raciones suficientes, por tanto no se recarga')

class Bebedero:
    def __init__(self):
        super().__init__()

class Vacunatorio:
    def __init__(self):
        super().__init__()

newvaca = Vaca('Lola')
cerdito = Cerdo('Piggy')
Gallinita = Gallina('Dory')
newcomederocomun = ComederoManual(500, 200)
newauto = ComederoAutomatico(50)

newvaca.MostrarNombre()
newcomederocomun.AlimentarAnimal(newvaca)
newvaca.MostrarHambre()
newvaca.MostrarSed()
newvaca.MostrarPeso()
newcomederocomun.AlimentarAnimal(newvaca)

newauto.AlimentarAnimal(newvaca)
newvaca.Vacunar()
newvaca.Vacunar()

cerdito.Beber()
newcomederocomun.AlimentarAnimal(cerdito)
cerdito.MaxComido()
cerdito.Comer(5)
cerdito.MaxComido()
