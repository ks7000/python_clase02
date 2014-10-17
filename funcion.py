# -*- encoding=utf-8 -*-
import click

@click.command()
@click.option('--nombre', default=u'Hugo', prompt=u'Introduzca su nombre, por favor', help='Si usted introduce su nombre lo imprimimos por pantalla.')
@click.option('--apellido', default=u'Chávez', prompt=u'Introduzca su apellido, por favor', help='Si usted introduce su apellido lo imprimimos por pantalla.')
def nombres(nombre, apellido):
    nombre_completo = nombre , apellido
    print "Mi nombre completo es ", nombre , " ", apellido
    return nombre_completo

if __name__ == '__main__':
    nombres()

