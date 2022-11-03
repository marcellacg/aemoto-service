from helpers.database import db

class Pessoa(db.Model):

    __tablename__ = "tb_pessoa"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    nascimento = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    telefone = db.Column(db.String(11), nullable=False)

    aluno_child = db.relationship("Aluno", uselist=False)
    prefeito_child = db.relationship("Prefeito", uselist=False)
    endereco_child = db.relationship("Endereco", uselist=False)
    funcionario_child = db.relationship("Funcionario", uselist=False)
    gestor_child = db.relationship("GestorApp", uselist=False)

    def __init__(self, nome, nascimento, email, telefone):
        self.nome = nome
        self.nascimento = nascimento
        self.email = email
        self.telefone = telefone

    def __repr__(self):
        return '<Nome: {}\n Data de Nascimento: {}\n Email: {}\n Telefone: {}>'.format(self.nome, self.nascimento, self.email, self.telefone)