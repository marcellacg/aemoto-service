from helpers.database import db

class Funcionario(db.Model):
    
    __tablename__ = "tb_funcionario"
    __mapper_args__ = {'polymorphic_identity': 'funcionario', 'concrete': True}
    
    id = db.Column(db.Integer, primary_key=True)
    prefeitura = db.Column(db.String(90), nullable=False)
    cargo = db.Column(db.String(30), nullable=False)

    
    pessoa_parent = db.Column(db.Integer, db.ForeignKey("tb_pessoa.id"))
    prefeitura_id = db.Column(db.Integer, db.ForeignKey('tb_prefeitura.id'), nullable=False)
    motorista_child = db.relationship("Motorista", uselist=False)

    pessoa = db.relationship("Pessoa",foreign_keys=[pessoa_parent])
    

    def __init__(self, prefeitura, cargo):
        self.prefeitura = prefeitura
        self.cargo = cargo

    def __repr__(self):
        return '<Prefeitura: {}\n Cargo: {}>'.format(self.prefeitura, self.cargo)

    