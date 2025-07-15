from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def unida():
    return 'hola desde mi casa no desde la unida'

if __name__ == '__main__':
    app.run(debug=True,port=5000, host='0.0.0.0')

'''
el 0.0.0.0 es un comodin que permite que la aplicacion sea accesible desde cualquier direccion IP
'''