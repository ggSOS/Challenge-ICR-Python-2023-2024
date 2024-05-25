from flask import Flask, jsonify, request


app = Flask(__name__)

# rota para obter todos os itens
@app.route('/api/items', methods=['GET'])
def get_items():
    try:
        arquivo = open('dadosPacientes.json', 'r', encoding='utf-8')
        data = arquivo.read()
        arquivo.close()
    except:
        arquivo = open('pacienteTeste.json', 'r', encoding='utf-8')
        data = arquivo.read()
        arquivo.close()
    
    return data

if __name__ == '__main__':
    app.run(debug=True)
