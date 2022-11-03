from helpers.database import db

class Prefeitura(db.Model):

    __tablename__ = "tb_prefeitura"

    id = db.Column(db.Integer, primary_key=True)
    secretarios = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefone = db.Column(db.String(11), unique=True, nullable=False)
    nomePrefeito = db.Column(db.String(100), unique=True, nullable=False)

    prefeito_child = db.relationship("Prefeito", uselist=False)
    cidade_parent = db.Column(db.Integer, db.ForeignKey("tb_cidade.id"))
    rota_parent = db.Column(db.Integer, db.ForeignKey("tb_rota.id"))
    gestores = db.relationship('GestorApp', backref='GestorApp', lazy=True)
    funcionarios = db.relationship('Funcionario', backref='Funcionario', lazy=True)

    def __init__(self, secretarios, email, telefone, nomePrefeito):
        self.secretarios = secretarios
        self.email = email
        self.telefone = telefone
        self.nomePrefeito = nomePrefeito

    def __repr__(self):
        return '<Secretarios: {}\n Email: {}\n Telefone: {}\n Nome do Prefeito: {}'.format(self.secretarios, self.email, self.telefone, self.nomePrefeito)