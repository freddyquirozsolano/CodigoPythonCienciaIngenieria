# Instalar paquetes de sistemas
pip install requests  # HTTP requests
pip install flask  # Web framework
pip install sqlalchemy  # ORM base de datos
pip install pyyaml  # Trabajar con YAML

# Ejemplo: API REST con Flask
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify({
        'status': 'online',
        'version': '1.0.0'
    })

@app.route('/api/calcular_imc', methods=['POST'])
def calcular_imc():
    datos = request.json
    peso = datos.get('peso')
    altura = datos.get('altura')
    
    if peso and altura:
        imc = peso / (altura ** 2)
        return jsonify({'imc': round(imc, 2)})
    return jsonify({'error': 'Datos incompletos'}), 400

if __name__ == '__main__':
    app.run(debug=True)