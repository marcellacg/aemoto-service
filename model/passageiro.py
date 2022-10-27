from model.aluno import Aluno


class Passageiro():
    
    def __init__(self, aluno, cidadeOrigem, cidadeDestino):
        self.aluno = aluno
        self.cidadeOrigem = cidadeOrigem
        self.cidadeDestino = cidadeDestino

    def __repr__(self):
        return '<Aluno {} Cidade Origem {} Cidade Destino {} >'.format(self.aluno, self.cidadeOrigem, self.cidadeDestino)