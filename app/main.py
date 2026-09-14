from flask import Flask, jsonify

app = Flask(__name__)

def add_numbers(a, b):
    """Fonction utilitaire pour démontrer les tests unitaires."""
    return a + b

@app.route('/')
def home():
    return "Bienvenue sur l'App de Démo CI/CD !"

@app.route('/api/add/<int:a>/<int:b>')
def api_add(a, b):
    result = add_numbers(a, b)
    return jsonify({"input_a": a, "input_b": b, "result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
