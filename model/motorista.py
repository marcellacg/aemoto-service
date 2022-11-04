from model.funcionario import Funcionario
from helpers.database import db


class Motorista(Funcionario):

    __tablename__ = "tb_motorista"


    funcionario_parent = db.Column(db.Integer, db.ForeignKey("tb_funcionario.id"))
    

    def __init__(self, rotas, funcionario):
        self.funcionario = funcionario
        self.rotas = rotas

    def __repr__(self):
        return '<Rotas: {}\n>'.format(self.rotas)