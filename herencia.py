# -*- encoding=utf-8 -*-
from clases import Auto
import click


class Helicoptero(Auto):
    pass

@click.command()
@click.option('--litros', default=7, prompt=u'¿Con cuántos litros desea comenzar?', help=u'Introduzca por favor el número de litros de gasolina para el helicóptero')
def inicio(litros):
    mi_helicoptero = Helicoptero(litros)
    mi_helicoptero.arrancar()
    mi_helicoptero.conducir()
    mi_helicoptero.arrancar()
    mi_helicoptero.conducir()
    mi_helicoptero.arrancar()
    mi_helicoptero.conducir()
    mi_helicoptero.arrancar()
    mi_helicoptero.conducir()

if __name__ == '__main__':
    inicio()
