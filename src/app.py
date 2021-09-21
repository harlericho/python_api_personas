from flask import Flask, jsonify, request
from flask_cors import CORS
import models.persona


# configuraciones
persona = models.persona

app= Flask(__name__)
CORS(app)

# rutas de la api
@app.route('/')
def index():
    try:
        datos = persona.listadoPersona()
        list=[]
        for i in datos:
            file ={
                'id':i[0],
                'dni':i[1],
                'nombres':i[2],
                'fecha': i[3],
                'correo':i[4],
            }
            list.append(file)
        return jsonify({'datos': list})
    except Exception as e:
        return jsonify({'error': e})

@app.route('/<int:id>', methods=['GET'])
def search(id):
    try:
        datos = persona.listadoPersonaID(id)
        if datos != None:
            file ={
                'id':datos[0],
                'dni':datos[1],
                'nombres':datos[2],
                'fecha':datos[3],
                'correo':datos[4],
            }
            return jsonify({'datos': file})
        else:
            return jsonify({'datos': 'No existe ese dato con ese ID'})
    except Exception as e:
        return jsonify({'error': e})


@app.route('/', methods=['POST'])
def create():
    try:
        json = request.json
        if request.method == 'POST':
            dni = json['dni']
            nombres = json['nombres']
            fecha = json['fecha']
            correo = json['correo']
        if persona.validarDni1(dni):
            return jsonify({'dni':'Dni ya existe en la base'})
        elif persona.validarCorreo1(correo):
            return jsonify({'correo':'Correo ya existe en la base'})
        else:
            data = persona.guardarPersona(dni,nombres,fecha,correo)
            if data[0] =='dni':
                return jsonify({'dni': data[1]})
            elif data[0] =='correo':
                return jsonify({'correo': data[1]})
            elif data[0] =='nombres':
                return jsonify({'nombres': data[1]})
            elif data[0] =='fecha':
                return jsonify({'fecha': data[1]})
            else:
                return jsonify({'datos': data})
    except Exception as e:
        return jsonify({'error': e})


@app.route('/<int:id>', methods=['PUT'])
def update(id):
    try:
        file = persona.listadoPersonaID(id)
        if file != None:
            json = request.json
            if request.method == 'PUT':
                dni = json['dni']
                nombres = json['nombres']
                fecha = json['fecha']
                correo = json['correo']
            validar = persona.validarDni2(dni,id)
            validar1= persona.validarCorreo2(correo,id)
            if validar >=2:
                return jsonify({'dni':'Dni ya existe en la base'})
            elif validar1 >=2:
                return jsonify({'correo':'Correo ya existe en la base'})
            else:
                data =persona.actualizarPersona(dni,nombres,fecha,correo,id)
                if data[0] =='dni':
                    return jsonify({'dni': data[1]})
                elif data[0] =='correo':
                    return jsonify({'correo': data[1]})
                elif data[0] =='nombres':
                    return jsonify({'nombres': data[1]})
                elif data[0] =='fecha':
                    return jsonify({'fecha': data[1]})
                else:
                    return jsonify({'datos':data})
        else:
            return jsonify({'datos': 'No existe ese dato con ese ID'})
    except Exception as e:
        return jsonify({'error': e})

@app.route('/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        file = persona.listadoPersonaID(id)
        if file != None:
            data = persona.eliminarPersona(id)
            return jsonify({'datos':data})
        else:
            return jsonify({'datos': 'No existe ese dato con ese ID'})
    except Exception as e:
        return jsonify({'error': e})


# Inicio del servicio
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)