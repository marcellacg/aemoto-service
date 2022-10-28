from helpers.database import db

class InstituicaoDeEnsino(db.Model):

    __tablename__ = "tb_instituicaoDeEnsino"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(11), nullable=False)
    logradouro = db.Column(db.String(200), nullable=False)
    
    def __init__(self, nome, logradouro, telefone):
        self.nome = nome
        self.logradouro = logradouro
        self.telefone = telefone

    def __repr__(self):
        return '<Nome: {}\n Logradouro: {}\n Telefone: {}>'.format(self.nome, self.logradouro, self.telefone)