class Transporte(object):
    carga = []
    capacidade = 0
    posicao = {
        'x': 0,
        'y': 0,
        'z': 0,
    }

    def move(self):
        raise NotImplementedError()

    def carrega(self, elemento):
        if self.capacidade > 0:
            self.carga.append(elemento)
            print 'Carregado "%s"' % elemento
            self.capacidade -= 1
        else:
            raise RuntimeError('Veiculo cheio')

    def descarrega(self, elemento):
        raise NotImplementedError()


class Aereo(Transporte):
    capacidade = 1

    def move(self):
        return 'Girou a helice'


class Maritimo(Transporte):
    capacidade = 3
    submerso = False

    def move(self):
        print 'Girou a turbina'

    def afundar(self):
        self.submerso = True
        print 'Afundou'

    def subir(self):
        self.submerso = False
        print 'Subiu'

    def carrega(self, elemento):
        if self.submerso:
            self.subir()
            super(Maritimo, self).carrega(elemento)
            self.afundar()
        else:
            super(Maritimo, self).carrega(elemento)


class Hibrido(Aereo, Maritimo):
    capacidade = 2

    def move(self):
        if self.submerso:
            print Maritimo.move(self)
        else:
            print Aereo.move(self)

class Terrestre(Transporte):
    capacidade = 1

    def move(self):
        print 'Girou a roda'


class Anfibio(Maritimo, Terrestre):
    def move(self):
        Maritimo.move(self)
        Terrestre.move(self)
