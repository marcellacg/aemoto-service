from model.funcionario import Funcionario


class Motorista(Funcionario):

    def __init__(self, rotas, prefeitura, cargo):
        super().__init__(prefeitura, cargo)
        self.rotas = rotas

    def __repr__(self):
        return '<Rotas {} Prefeitura {} Cargo {}>'.format(self.rotas, self.prefeitura, self.cargo)