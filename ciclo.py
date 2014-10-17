# -*- coding: utf-8 -*-
import click

@click.command()
@click.option('--anio_fin', default=2021, prompt ='¿Hasta cuál año desea imprimir?', help=u'Permite definir hasta cuál año se ejecuta el ciclo')
def ciclo(anio_fin):
    anio = 2001
    while anio <= anio_fin:
      print u"Año", str(anio), str(anio_fin)
      anio += 1

if __name__ == '__main__':
    ciclo()
