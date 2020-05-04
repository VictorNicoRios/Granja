from Clases import *


#                                                          <---Modelo--->


#<--Animales-->

Vaquita = Vaca('Lola')
Cerdito = Cerdo('Piggy')
Gallinita = Gallina('Turuleca')


#<--Dispositivos de Atención Automática-->

ComederoA1 = ComederoAutomatico(500)
ComederoM1 = ComederoManual(5, 350)
Bebedero1 = Bebedero()
Vacunatorio1 = Vacunatorio()


#<--Estaciones de Servicio-->

Estación_de_Servicio_Auto = EstaciónDeServicio(ComederoA1, Bebedero1, Vacunatorio1)
Estación_de_Servicio_Manual = EstaciónDeServicio(ComederoM1, Bebedero1, Vacunatorio1)


#                                                           <---test--->

Estación_de_Servicio_Auto.AtenderA(Vaquita)

Estación_de_Servicio_Manual.AtenderA(Cerdito)

Estación_de_Servicio_Auto.AtenderA(Gallinita)