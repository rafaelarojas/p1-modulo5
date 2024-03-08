from flask import Flask, jsonify, request, redirect, url_for, render_template
from tinydb import TinyDB

app = Flask(__name__)
db = TinyDB("caminhos.json")

@app.route('/novo', methods=['POST'])
def novo_caminho():
    dados = request.form
    x = int(dados.get("x"))
    y = int(dados.get("y"))
    z = int(dados.get("z"))
    r = int(dados.get("r"))
    
    caminho = {x, y, z, r}
    db.insert(caminho)
    
    return jsonify(caminho)

@app.route('/pegar_caminho/<int:caminho_id>')
def pegar_caminho(caminho_id):
    caminho = db.get(doc_id=caminho_id)
    return render_template('index.html', caminho=caminho)

@app.route('/listas_caminhos')
def listas_caminhos():
    caminhos = db.all()
    return render_template('index.html', caminhos=caminhos)

@app.route('/atualizar/<int:caminho_id>', methods=['GET', 'POST'])
def atualizar_caminho(caminho_id):
    caminho = db.get(doc_id=caminho_id)
    
    if request.method == 'POST':
        pontos_atualizados = [
            {'x': float(request.form['x1']), 'y': float(request.form['y1']), 'z': float(request.form['z1']), 'r': float(request.form['r1'])},
        ]
        db.update({'pontos': pontos_atualizados}, doc_ids=[caminho_id])

    return render_template('index.html', caminho=caminho)

@app.route('/deletar/<int:caminho_id>')
def deletar_caminho(caminho_id):
    db.remove(doc_ids=[caminho_id])
    return redirect(url_for('listar_caminhos'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

    from flask import Flask, render_template

app = Flask(__name__)
