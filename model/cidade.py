class Cidade():

    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
    
    
    def __repr__(self):
        return '<Nome: {}\n Sigla: {}>'.format(self.nome, self.sigla)