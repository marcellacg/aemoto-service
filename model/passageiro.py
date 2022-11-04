from model.aluno import Aluno
from helpers.database import db


class Passageiro(Aluno, db.Model):

    __tablename__ = "tb_passageiro"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    cidadeOrigem = db.Column(db.String(90), nullable=False)
    cidadeDestino = db.Column(db.String(90), nullable=False)

    aluno_parent = db.Column(db.Integer, db.ForeignKey('tb_aluno.id'))
    
    def __init__(self, aluno, cidadeOrigem, cidadeDestino):
        self.aluno = aluno
        self.cidadeOrigem = cidadeOrigem
        self.cidadeDestino = cidadeDestino

    def __repr__(self):
        return '<Aluno: {}\n Cidade Origem: {}\n Cidade Destino {} >'.format(self.aluno, self.cidadeOrigem, self.cidadeDestino)