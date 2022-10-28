from helpers.database import db

class Funcionario(db.Model):
    
    __tablename__ = "tb_funcionario"
    
    id = db.Column(db.Integer, primary_key=True)
    prefeitura = db.Column(db.String(90), nullable=False)
    cargo = db.Column(db.String(30), nullable=False)
    
    def __init__(self, prefeitura, cargo):
        self.prefeitura = prefeitura
        self.cargo = cargo

    def __repr__(self):
        return '<Prefeitura: {}\n Cargo: {}>'.format(self.prefeitura, self.cargo)

    