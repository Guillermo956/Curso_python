from flask import Flask, jsonify, request, Blueprint

Logout = Blueprint('Logout', __name__)

@Logout.route('/Logout', methods=['POST'])
def logout():
    user= request.json.get('user')
    password= request.json.get('password')
    print("user introducido para Logout= ", user, "password introducido para Logout= ", password)