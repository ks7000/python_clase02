class Auto:
# aprendiendo clases ***    
    def __init__(self, gasolina):
        self.gasolina = gasolina
    
    def decorar(f):
        def inner(*args, **kwargs):
            f(*args, **kwargs)
            print "Se ha ejecutado %s" % f.__name__
        return inner
    
    @decorar
    def arrancar(self):
        if self.gasolina > 0:
            print "Arranca"
        else:
            print "NO arranca"
    
    @decorar
    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -=1
            print "Quedan", self.gasolina, " litros."
        else:
            print "No se mueve"

mi_decorador = decorar(arrancar())
