from flask import Flask, jsonify, Blueprint, request

cliente = Blueprint('cliente',__name__)

@cliente.route('/cliente', methods=['POST'])


def CallServiceSet():
    ci= request.json.get('ci')
    print("Ci introducido= ", ci)
    codRes, menRes, accion, = inicializarVarables(ci,)

    salida = {
        'codRes': codRes,
        'menRes': menRes,
        'accion': accion,
        'ci' : ci
    }

    return jsonify(salida)

def inicializarVarables(ci):
    codRes = 'Sin_ERROR'
    menRes = 'OK'
    accion = 'Login exitoso'
    cilocal = "6127188"
    nombre = "Guillermo"
    apellidos = "ZorrillaRotela"

    try:
        if ci == cilocal:
            print("Success")
            accion = 'Success'
            codRes = 'Sin_ERROR'
            menRes = 'OK'
            ci= '6127188'
            nombre= 'Guillermo'
            apellidos= 'ZorrillaRotela'

        else:
            print("Cliente no esta en el sistema")
            accion = 'Cliente no esta en el sistema'
            codRes = 'ERROR'
            menRes = 'ERROR cliente'
    except Exception as e:
        print("Cliente no esta en el sistema ", e)
        codRes = 'ERROR'
        menRes = 'ERROR cliente'
        accion = 'Cliente no esta en el sistema'
        return codRes, menRes, accion

    return codRes, menRes, accion