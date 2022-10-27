from model.pessoa import Pessoa

class GestorApp(Pessoa):
    
    def __init__(self, admin, nascimento, email, telefone):
        super().__init__(nascimento, email, telefone)
        self.admin = admin

    def __repr__(self):
        return '<Admin: {}\n Data de Nascimento: {}\n Email: {}\n Telefone: {}>'.format(self.admin, self.nascimento, self.email, self.telefone)