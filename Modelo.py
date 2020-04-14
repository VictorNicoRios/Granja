def main():
    #Se define las variables y métodos que comparten todos los animales
    class Animal:
        def __init__(self, in_Peso, in_Hambre, in_Sed, in_Vacunado):
            self.Raza='Vaca'
            self.Peso=in_Peso
            self.Hambre=in_Hambre
            self.Sed=in_Sed
            self.Vacunado=in_Vacunado
    class Vaca(Animal):
        def __init__(self, in_Peso, in_Hambre, in_Sed, in_Vacunado):
                super().__init__(in_Peso, in_Hambre, in_Sed, in_Vacunado)
        def MostrarNombre(self):
            print(self.Raza)
    
    #Se define las características que comparten las estaciones de atención automáticas
    #class EstaciónAutomática():
     #   class Comedero():
      #  class Bebedero():
       # class Vacunatorio():
    vacaobjeto=Vaca(500, True, 0, False)
    vacaobjeto.MostrarNombre()
    
main()