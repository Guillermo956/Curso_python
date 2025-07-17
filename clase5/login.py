from flask import Flask, jsonify, request, Blueprint

login = Blueprint('login', __name__)

@login.route('/login', methods=['POST'])

def llamarServicioSet():
    user= request.json.get('user')
    password= request.json.get('password')
    print("user introducido= ", user,"password introducido= ", password)

    codRes, menRes, accion, rol = inicializarVarables(user, password)

    salida = {
        'codRes': codRes,
        'menRes': menRes, 
        'usuario': user,
        'accion': accion,
        'rol': rol
    }

    return jsonify(salida)

def inicializarVarables(user, password):
    codRes = 'Sin_ERROR'
    menRes = 'OK'
    accion = 'Login exitoso'
    rol= "admin"
    userLocal = "Papu2025"
    passwordLocal = "Holaa2023"

    try:
        if user == userLocal and password == passwordLocal:
            print("Login exitoso")
            accion = 'Login exitoso'
        else:
            codRes = 'Error'
            menRes = 'Usuario o contraseña incorrectos'
            accion = 'Login fallido'
            rol = 'N/A'
    except Exception as e:
        print("Error en el login: ", e)
        codRes = 'Error'
        menRes = 'Error en el login'
        accion = 'Error en el login'
        rol = 'N/A'
        return codRes, menRes, accion, rol, user

    return codRes, menRes, accion, rol