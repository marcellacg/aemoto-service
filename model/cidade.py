from helpers import db

class Cidade(db.Model):

    __tablename__ = "tb_cidade"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sigla = db.Column(db.String(6), nullable=False)


    prefeitura_child = db.relationship("Prefeitura", uselist=False)
    uf_child = db.relationship("Uf", uselist=False)
    

    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
    
    
    def __repr__(self):
        return '<Nome: {}\n Sigla: {}>'.format(self.nome, self.sigla)