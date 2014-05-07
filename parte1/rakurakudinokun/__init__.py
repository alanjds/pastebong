"""
Modulo do simulador Rakuraku Dinokun
"""
import random

from jogos import sqrt

def get_ovo():
    """
    Cria um ovo de Rakuraku Dinokun
    """
    return Ovo()


def oops():
    "Retorna a string 'oops'"
    return 'Oops'


TIPOS_DE_DINO = [
    'Brontossauro',
    'Tiranossauro',
    'Estegossauro',
]

class Ovo(object):
    "Ovo de Rakuraku Dinokun"
    _rachado = False

    def __init__(self):        
        self.tipo = random.choice(TIPOS_DE_DINO)

    def __unicode__(self):
        return u'Ovo de ' + self.tipo

    def __repr__(self):
        if not self._rachado:
            tipo = 'desconhecido'
        else:
            tipo = self.tipo
        return '<Ovo: "%s">' % tipo

    def rachar(self):
        "Racha o ovo e sai um Rakuraku"
        self._rachado = True
