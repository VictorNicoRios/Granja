class Oveja():
    def __init__(self):
        self.Lana=True
    def comer(self):
        print('estoy comiendo')

class Pastor():
    def Trasquilar(self, objeto):
        objeto.Lana=False
    def AlimentarOveja(self, objeto):
        objeto.comer()

ovejita=Oveja()
print('Tiene lana?: ', ovejita.Lana)
granjero=Pastor()
granjero.Trasquilar(ovejita)
print('Tiene lana?: ', ovejita.Lana)
granjero.AlimentarOveja(ovejita)
