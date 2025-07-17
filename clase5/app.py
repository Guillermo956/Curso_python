from flask import Flask, jsonify, request
from login import login
from Logout import Logout
app = Flask(__name__)
##se expone el blueprint de login
app.register_blueprint(login)
app.register_blueprint(Logout)
@app.route('/', methods=['GET'])

def unida():
    return 'server flask is runing on port 5000'

if __name__ == '__main__':
    app.run(debug=True,port=5000, host='0.0.0.0')

'''
el 0.0.0.0 es un comodin que permite que la aplicacion sea accesible desde cualquier direccion IP
'''