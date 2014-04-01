from random import shuffle

class Tombola(object):
    '''Sorteia itens sem repetir'''

    def carregar(self, seq):
        self.itens = list(seq)

    def misturar(self, pairswap=None):
        pairswap(self.itens) if pairswap else shuffle(self.itens)

    def sortear(self):
        return self.itens.pop()

    def carregada(self):
        return bool(self.itens)

    def __iter__(self):
        for i in self.itens:
            yield i
