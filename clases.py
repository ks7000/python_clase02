class Auto:
# aprendiendo clases ***    
    def __init__(self, gasolina):
        self.gasolina = gasolina
    
    def arrancar(self):
        if self.gasolina > 0:
            print "Arranca"
        else:
            print "NO arranca"
    
    
    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -=1
            print "Quedan", self.gasolina, " litros."
        else:
            print "No se mueve"
    
    
mi_auto = Auto(18)

# cuanta gasolina tenemos
print mi_auto.gasolina
mi_auto.arrancar()
mi_auto.conducir()
mi_auto.arrancar()
mi_auto.conducir()
mi_auto.conducir()
mi_auto.conducir()
mi_auto.arrancar()
