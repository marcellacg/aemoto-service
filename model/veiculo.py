from helpers.database import db

class Veiculo(db.Model):

    __tablename__ = "tb_veiculo"

    id = db.Column(db.Integer, primary_key=True)
    cidade = db.Column(db.String(80), nullable=False)
    qtdPassageiros = db.Column(db.String(10), nullable=False)
    tipoVeiculo = db.Column(db.String(20), nullable=False)
    placa = db.Column(db.String(20), nullable=False)

    motorista_parent = db.Column(db.Integer, db.ForeignKey("tb_motorista.id"))
    
    def __init__(self, cidade, qtdPassageiros, tipoVeiculo, placa):
        self.cidade = cidade
        self.qtdPassageiros = qtdPassageiros
        self.tipoVeiculo = tipoVeiculo
        self.placa = placa

    def __repr__(self):
        return '<Cidade: {}\n Quantidade de passageiros: {}\n Tipo do veículo: {}\n Placa: {}>'.format(self.cidade, self.qtdPassageiros, self.tipoVeiculo, self.placa)