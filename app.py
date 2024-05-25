from flask import Flask, jsonify, request


app = Flask(__name__)

# Rota para obter todos os itens
@app.route('/api/items', methods=['GET'])
def get_items():
    #return jsonify(data)
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

"""# Rota para obter um item por ID
@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

# Rota para adicionar um novo item
@app.route('/api/items', methods=['POST'])
def add_item():
    new_item = request.json
    new_item["id"] = len(data) + 1
    data.append(new_item)
    return jsonify(new_item), 201

# Rota para atualizar um item existente
@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in data if item["id"] == item_id), None)
    if item:
        updated_item = request.json
        item.update(updated_item)
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

# Rota para deletar um item
@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global data
    data = [item for item in data if item["id"] != item_id]
    return '', 204"""