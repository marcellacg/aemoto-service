from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from model.endereco import Endereco
from model.pessoa import Pessoa
from model.aluno import Aluno
from model.funcionario import Funcionario
from model.gestorApp import GestorApp
from model.instituicaoDeEnsino import InstituicaoDeEnsino
from model.motorista import Motorista
from model.passageiro import Passageiro
from model.pessoa import Pessoa
from model.cidade import Cidade
from model.prefeito import Prefeito
from model.prefeitura import Prefeitura
from model.rota import Rota
from model.uf import Uf
from model.veiculo import Veiculo

from helpers.database import db, migrate

# CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://marcella:409014@localhost:5432/aemotor'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)



# pessoa = Pessoa("Joao", "25/10/2000", "email@joao", "58725-5852")
# pessoa2 = Pessoa("Pedro", "15/03/1960", "email@pedro", "0000-0000")

# aluno = Aluno("Maria", "25/01/2009", "maria@email", "8525-4521", "IFPB", "TSI", "25233521")
# #print(aluno)
# cidade = Cidade("Guarabira", "GBA")
# endereco = Endereco("58200-000", "43", "Casa", "Próximo a DyliJoias", "Rua dos Anjos")

# prefeitura = Prefeitura("José", "email@jose", "1587-5152", "Jaime")
# funcionario = Funcionario(prefeitura, "Técnico")
# #print(funcionario)

# veiculo = Veiculo("Guarabira", "20", "Ônibus", "FPG-8971")
# #gestor = GestorApp("Severino", "12/02/1999", "seve@sevs", "8752-5541")
# gestor = GestorApp(pessoa2)
# #print(gestor)
# instituicao = InstituicaoDeEnsino("IFPB", "Rua Professor Carlos Leonardo Arcoverde", "98195-6465")
# rota = Rota("Guarabira", "30", "Riachão", "Van", "Inácia", "08:00h", "09:00h")
# motorista = Motorista(rota, funcionario)
# #print(motorista)
# passageiro = Passageiro(aluno, "Tacima", "Guarabira")
# #print(passageiro)

# prefeito = Prefeito(pessoa)
# #print(prefeito)

# uf = Uf("Paraíba", "PB")
