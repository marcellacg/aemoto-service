from model.pessoa import Pessoa

class Nome(Pessoa):
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return self.nome

class Aluno(Nome):

    def __init__(self, nome, instituicaoDeEnsino, curso, matricula):
        super().__init__(nome)
        self.instituicaoDeEnsino = instituicaoDeEnsino
        self.curso = curso
        self.matricula = matricula
    
    def __repr__(self):
        return '<Nome: {}\n Instituição de ensino: {}\n Curso: {}\n Matrícula: {}>'.format(self.nome, self.instituicaoDeEnsino, self.curso, self.matricula)