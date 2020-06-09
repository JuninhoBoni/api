from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades

import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://<SVC_Sist_Homol_SQL>:<svc321>@<127.0.0.1>:<1433>/<AKREDITASI_HOM>'
api = Api(app)

desenvolvedores = [
    {
        'id': 0,
        'nome': 'juninho',
        'habilidades': ['Python', 'Flask']
    },
    {
        'id': 1,
        'nome': 'juninho2',
        'habilidades': ['Python2', 'Flask2']
    }
]

# devolve dados pelo id, altera e deleta um dado
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'erro', 'menssagem': 'id ' + str(id) + ' não existe'}
        except Exception:
            mensagem = 'ERRO DESCONHECIDO, ENTRE EM CONTATO COM O DESNVOVEDOR DA API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'menssagem': 'id excluido'}

# lista todos os dados e realiza inclusão
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return {'status': 'sucesso', 'menssagem': 'registro inserido '+str(posicao)}

api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)