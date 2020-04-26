#                                                          <----- Campo de Jorgito ----->


#                                                                  <--Animales-->

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

    def AnimalBeber(self):
        self.Sed = False

    def AnimalVacunar(self):
        self.Vacunado = 1==1

class Vaca(Animal):
    #Se definen las clases de cada animal con unos valores pre-establecidos para enviarle a la superclase Animales.
    #Cada animal sólo espera que le ingresen su nombre al crearlo
    def __init__(self, in_Nombre_Vaca):
        self.Nombre = in_Nombre_Vaca
        self.Raza = 'Vaca'
        self.Peso_Kg = 300
        self.Hambre = True
        self.Sed = True
        self.Vacunado = False
        super().__init__(self.Nombre, self.Raza, self.Peso_Kg, self.Hambre, self.Sed, self.Vacunado)
    
    def Comer(self, in_Peso_de_Racion):
        #Para saber cúanto pesa lo que come se le manda el peso de la unidad de comida x la cantidad de unidades que va a comer.
        #El peso de lo que come se agrega al peso de la vaca
        self.Peso_Kg += (in_Peso_de_Racion)/3
        self.Hambre = self.Peso_Kg <= 200
        self.Sed = (in_Peso_de_Racion) >= 200
        print('[Vaca: ', self.Nombre, ']: *Comió*')

    def Beber(self):
        self.AnimalBeber()
        self.Peso_Kg -= 0.500
        print('[Vaca: ', self.Nombre, ']: *Bebió*')
    
    def Vacunar(self):
        if self.Vacunado==False:
            self.AnimalVacunar()
            print('[Vaca: ', self.Nombre, ']: *Vacunado*')
        else:
            print('El animal "',self.Nombre,'" ya está vacunado, no conviene vacunarlo nuevamente')
            return SystemError

    def Caminar(self):
        self.Peso_Kg-=3
        print('[Vaca: ', self.Nombre, ']: *Caminó*')

class Cerdo(Animal):
    def __init__(self, in_Nombre_Cerdo):
        self.Nombre = in_Nombre_Cerdo
        self.Raza = 'Cerdo'
        self.Peso_Kg = 180
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
        print('[Cerdo: ', self.Nombre, ']: *Comió*')
    
    def MostrarMaxComido(self):
        print('La vez que el cerdo "',self.Nombre,'" más comió le dieron:',self.Maximo_Comido)
    
    def Vacunar(self):
        self.AnimalVacunar()
        print('[Cerdo: ',self.Nombre,']: *Vacunado*')
    
    def Beber(self):
        self.AnimalBeber()
        self.Veces_Seguidas_Comio=0
        self.Hambre=1==1
        print('[Cerdo: ',self.Nombre, ']: *Bebió*')

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
    
    def Comer(self, in_Peso_de_Racion):
        self.Veces_Comio+=1
        print('[Gallina: ', self.Nombre, ']: *Comió*')
    
    def Vacunar(self):
        print('[Gallina: ', self.Nombre, ']: *Este animal no conviene vacunarlo*')
        return SystemError

    def Beber(self):
        self.AnimalBeber()
        print('[Gallina: ', self.Nombre, ']: *Bebió*')

#                                                            <--Atención automática-->

class Comedero:
    def __init__(self, in_Tipo_Dispositivo, in_Raciones_Restantes, in_Cant_Raciones, in_Cant_Maxima):
        self.TipoDispositivo = in_Tipo_Dispositivo
        self.Raciones_Restantes=in_Raciones_Restantes
        self.Peso_X_Racion_Kg=0.500
        self.Cant_Raciones=in_Cant_Raciones
        self.Cant_Maxima = in_Cant_Maxima
        self.Peso_Racion_Dada=self.Peso_X_Racion_Kg*self.Cant_Raciones

class ComederoManual(Comedero):
    #"in_Cant_Alimenta" o "Cant_Raciones" es la cantidad de comida que alimentará el dispositivo y varía en cada comedero
    def __init__(self, in_Cant_Alimenta, in_Peso_Soportado):
        self.Cant_Raciones=in_Cant_Alimenta
        self.Peso_Animal_Soportado=in_Peso_Soportado
        super().__init__('Comedero Manual', 50, self.Cant_Raciones, 0)

    #Sólo pide al objeto que va a alimentar (para saber su peso y ejecutar su función comer)
    def AtenderAnimal(self, In_Animal):
        #Si la variable Peso_Kg (Peso en Kg del animal) es mayor al peso máximo de animal que soporta el comedero (valor que se definió al instanciarlo)
        if In_Animal.Peso_Kg <= self.Peso_Animal_Soportado:
            #Ejecuta la función comer de ese objeto
            print('[',self.TipoDispositivo,']: *Alimentando al animal "', In_Animal.Nombre, '"*')
            In_Animal.Comer(self.Peso_Racion_Dada)
        else:
            print('[Comedero Manual]: Peso del animal "', In_Animal.Nombre, '" no soportado para este comedero. Por favor, elija otro comedero')
            return TypeError
    
    def Recargar_Comedero(self):
        if self.Raciones_Restantes < 10:
            self.Raciones_Restantes += 30
            print('[Comedero Manual]: Se han recargado 30 raciones')
        else:
            print('[Comedero Manual]: Este comedero tadavía tiene raciones suficientes (Raciones restantes:',self.Raciones_Restantes, '), por tanto no se recarga')
    
class ComederoAutomatico(Comedero):
    def __init__(self, in_Cant_Maxima):
        self.Cant_Maxima=in_Cant_Maxima
        super().__init__('Comedero Automatico', self.Cant_Maxima, 0, self.Cant_Maxima)

    def AtenderAnimal(self, In_Animal):
    #Se ejecuta si el objeto animal introducido tiene hambre
        if In_Animal.Hambre == True:
            self.Cant_Raciones = In_Animal.Peso_Kg/100
            print('[', self.TipoDispositivo,']: *Alimentando al animal "', In_Animal.Nombre, '"*')
            In_Animal.Comer(self.Peso_Racion_Dada)
        else:
            print('[Comedero Automático]: No puedo alimentar al animal "',In_Animal.Nombre,'" porque no tiene hambre')

    def Recargar_Comedero(self):
        if self.Raciones_Restantes < 15:
            self.Raciones_Restantes == self.Cant_Maxima
            print('[Comedero Automático]: Se han recargado al máximo de raciones')
        else:
            print('[Comedero Automático]: Este comedero tadavía tiene raciones suficientes, por tanto no se recarga')
            return TypeError

class Bebedero:
    def __init__(self):
        self.TipoDispositivo = 'Bebedero'

    def AtenderAnimal(self, inAnimal):
        inAnimal.Beber()

class Vacunatorio:
    def __init__(self):
        self.TipoDispositivo = 'Vacunatorio'

    def AtenderAnimal(self, inAnimal):
        inAnimal.Vacunar()


#                                                            <--Estación de Servicio-->

class EstaciónDeServicio():
    def __init__(self, inComedero, inBebedero, inVacunatorio):
        self.Maquinas = [inComedero, inBebedero, inVacunatorio]

    def AgregarMáquina(self, inMaquina):
        self.Maquinas.append(inMaquina)

    def AtenderA(self, inAnimal):
        for x in range(len(self.Maquinas)):
            try:
                if self.Maquinas[x].TipoDispositivo == 'Comedero Manual':
                    print('[Estación de Servicio]: *Intentando alimentar a "',inAnimal.Nombre, '" en "', self.Maquinas[x].TipoDispositivo, '*')
                    try:
                        self.Maquinas[x].AtenderAnimal(inAnimal)
                        if self.Maquinas[x].Raciones_Restantes <= 0:
                            self.Maquinas[x].Recargar_Comedero()
                    
                    except TypeError:
                        print('[Estación de Servicio]: Operación fallida')

                elif self.Maquinas[x].TipoDispositivo == 'Comedero Automatico':
                    print('[Estación de Servicio]: *Intentando alimentar a "',inAnimal.Nombre, '" en "', self.Maquinas[x].TipoDispositivo, '*')
                    try:
                        self.Maquinas[x].AtenderAnimal(inAnimal)
                        if self.Maquinas[x].Raciones_Restantes <= 0:
                            self.Maquinas[x].Recargar_Comedero()
                    
                    except TypeError:
                        print('[Estación de Servicio]: Operación fallida')

                else:
                    self.Maquinas[x].AtenderAnimal(inAnimal)
            
            except SystemError:
                print('[Estación de Servicio]: Operación fallida')
    
        if inAnimal.Raza=='Vaca':
            inAnimal.Caminar()
        
        if inAnimal.Raza=='Cerdo':
            inAnimal.MostrarMaxComido()


#                                                                  <---test--->

Vaquita=Vaca('Lola')
Cerdito=Cerdo('Piggy')
Gallinita=Gallina('Turuleca')

ComederoA1 = ComederoAutomatico(500)
ComederoM1 = ComederoManual(5, 350)
Bebedero1 = Bebedero()
Vacunatorio1 = Vacunatorio()

Estación_YPF = EstaciónDeServicio(ComederoA1, Bebedero1, Vacunatorio1)
Estación_Shell = EstaciónDeServicio(ComederoM1, Bebedero1, Vacunatorio1)

Estación_YPF.AtenderA(Vaquita)

Estación_Shell.AtenderA(Cerdito)

Estación_YPF.AtenderA(Gallinita)