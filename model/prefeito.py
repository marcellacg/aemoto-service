from model.pessoa import Pessoa


class Prefeito(Pessoa):
    
    def __init__(self, nome, nascimento, email, telefone):
        super().__init__(nome, nascimento, email, telefone)
        self.nome = nome

    def __repr__(self):
        return '<Nome: {}\n Data de nascimento: {}\n Email: {}\n Telefone: {}>'.format(self.nome, self.nascimento, self.email, self.telefone)
