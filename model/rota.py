from helpers.database import db

class Rota(db.Model):

    __tablename__ = "tb_rota"

    id = db.Column(db.Integer, primary_key=True)
    nomeDestino = db.Column(db.String(200), nullable=False)
    qtdalunos = db.Column(db.String(11), nullable=False)
    prefeitura = db.Column(db.String(200), nullable=False)
    veiculo = db.Column(db.String(30), nullable=False)
    passageiro = db.Column(db.String(50), nullable=False)
    horaSaida = db.Column(db.datetime(), nullable=False)
    horaChegada = db.Column(db.datetime(), nullable=False)
    
    def __init__(self, nomeDestino, qtdalunos, prefeitura, veiculo, passageiro, horaSaida, horaChegada):
        self.nomeDestino = nomeDestino
        self.qtdalunos = qtdalunos
        self.prefeitura = prefeitura        
        self.veiculo = veiculo
        self.passageiro = passageiro
        self.horaSaida = horaSaida
        self.horaChegada = horaChegada

    def __repr__(self):
        return '<Nome destino: {}\n  Quantidade de Alunos: {}\n Prefeitura: {}\n Veiculo: {}\n Passageiro: {}\n Hora de Saída: {}\n Hora de chegada: {}\n>'.format(self.nomeDestino, self.qtdalunos, self.prefeitura, self.veiculo, self.passageiro, self.horaSaida, self.horaChegada)