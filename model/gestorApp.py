from model.pessoa import Pessoa

class GestorApp(Pessoa):
    
    def __init__(self, nome, nascimento, email, telefone):
        super().__init__(nome, nascimento, email, telefone)

    def __repr__(self):
        return '<GestorApp: {}\n Data de Nascimento: {}\n Email: {}\n Telefone: {}>'.format(self.nome, self.nascimento, self.email, self.telefone)