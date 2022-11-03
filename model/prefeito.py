from model.pessoa import Pessoa
from helpers.database import db

class Prefeito(Pessoa):

    __tablename__ = "tb_prefeito"

    pessoa_parent = db.Column(db.Integer, db.ForeignKey("tb_pessoa.id"))
    prefeitura_parent = db.Column(db.Integer, db.ForeignKey("tb_prefeitura.id"))

    def __init__(self, pessoa):
        self.pessoa = pessoa

    def __repr__(self):
        return '<Prefeito: {} >'.format(self.pessoa)
