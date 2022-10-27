from model.aluno import Aluno


class Passageiro(Aluno):
    
    def __init__(self, nome, cidadeOrigem, cidadeDestino, instituicaoDeEnsino, curso, matricula):
        super().__init__(nome, instituicaoDeEnsino, curso, matricula)
        self.nome = nome
        self.cidadeOrigem = cidadeOrigem
        self.cidadeDestino = cidadeDestino

    def __repr__(self):
        return '<Nome {} Cidade Origem {} Cidade Destino {} Instituição de Ensino {} Curso {} Matricula {}>'.format(self.nome, self.cidadeOrigem, self.cidadeDestino, self.instituicaoDeEnsino, self.curso, self.matricula)