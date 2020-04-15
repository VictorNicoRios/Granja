#Se define las variables y métodos que comparten todos los animales
class Animal:
    def __init__(self, in_Nombre, in_Raza, in_Peso, in_Hambre, in_Sed, in_Vacunado):
        self.Nombre=in_Nombre
        self.Raza=in_Raza
        self.Peso_Kg=in_Peso
        self.Hambre=in_Hambre
        self.Sed=in_Sed
        self.Vacunado=in_Vacunado
    
    def MostrarNombre(self):
        print(self.Raza)

    def Comer(self):
        if self.Raza == 'Vaca':
            print('comer desde vaca')
    
    def Beber(self):
        self.Sed=False
    
    def Vacunar(self):
        self.Vacunado=True
    
class Vaca(Animal):
    def __init__(self, in_Nombre_Vaca):
        self.Nombre = in_Nombre_Vaca
        self.Raza = 'Vaca'
        self.Peso_Kg = 200
        self.Hambre = True
        self.Sed = True
        self.Vacunado = False
        super().__init__(self.Nombre, self.Raza, self.Peso, self.Hambre, self.Sed, self.Vacunado)

class Gallina(Animal):
    def __init__(self, in_Nombre_Gallina, in_Raza, in_Peso, in_Hambre, in_Sed, in_Vacunado):
        self.Nombre = in_Nombre_Gallina
        self.Raza = 'Gallina'
        self.Peso_Kg = 2.5
        self.Hambre = True
        self.Sed = True
        self.Vacunado = False
        super().__init__(self.Nombre, self.Raza, self.Peso_Kg, self.Hambre, self.Sed, self.Vacunado)

class Cerdo(Animal):
    def __init__(self, in_Nombre_Cerdo, in_Raza, in_Peso, in_Hambre, in_Sed, in_Vacunado):
        self.Nombre = in_Nombre_Cerdo
        self.Raza = 'Cerdo'
        self.Peso_Kg = 80
        self.Hambre = True
        self.Sed = True
        self.Vacunado = False
        super().__init__(self.Nombre, self.Raza, self.Peso_Kg, self.Hambre, self.Sed, self.Vacunado)
