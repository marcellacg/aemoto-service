class Rota():
    
    
    def __init__(self, nomeDestino, qtdalunos, prefeitura, veiculo, passageiro, horaSaida, horaChegada):
        self.nomeDestino = nomeDestino
        self.qtdalunos = qtdalunos
        self.prefeitura = prefeitura        
        self.veiculo = veiculo
        self.passageiro = passageiro
        self.horaSaida = horaSaida
        self.horaChegada = horaChegada

    def __repr__(self):
        return '<Nome destino {}  Quantidade de Alunos {} Prefeitura {} Veiculo {} Passageiro {} Hora de Saída {} Hora de chegada {}>'.format(self.nomeDestino, self.qtdalunos, self.prefeitura, self.veiculo, self.passageiro, self.horaSaida, self.horaChegada)