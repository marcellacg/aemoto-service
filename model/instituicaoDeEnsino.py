class InstituicaoDeEnsino():
    
    def __init__(self, nome, logradouro, telefone):
        self.nome = nome
        self.logradouro = logradouro
        self.telefone = telefone

    def __repr__(self):
        return '<Nome: {}\n Logradouro: {}\n Telefone: {}>'.format(self.nome, self.logradouro, self.telefone)