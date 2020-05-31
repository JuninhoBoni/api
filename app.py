from flask import Flask, jsonify, request
import json

app = Flask(__name__)

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
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'erro', 'menssagem': 'id ' + str(id) + ' não existe'}
        except Exception:
            mensagem = 'ERRO DESCONHECIDO, ENTRE EM CONTATO COM O DESNVOVEDOR DA API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'menssagem': 'id excluido'})


# lista todos os dados e realiza inclusão
@app.route('/dev/', methods=['POST', 'GET'])
def lista_dados():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify({'status': 'sucesso', 'menssagem': 'registro inserido '+str(posicao)})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)
    
if __name__ == '__main__':
    app.run(debug=True)
