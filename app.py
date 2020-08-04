from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import main as database
basedatos = database.DataBase()

@app.route('/listaTarea', methods=['GET'])
def listaTarea():
    ##return jsonify({"Tareas asignadas":basedatos.select_all_tareas()}) 
    tareas = basedatos.select_all_tareas()
    return jsonify({"tareas": tareas, "message": "Tareas's Records"})          

@app.route('/buscarTarea/<tarea_id>')
def buscarTarea(tarea_id):
    tareasFound = basedatos.select_tareas(tarea_id)
    if tareasFound != None:
        return jsonify(tareasFound)
    else:
        return jsonify({"message":"Tarea no encontrada"})


@app.route('/guardarTarea', methods=['POST'])
def guardarTarea():
    newTareas = basedatos.insert_tareas(request.json['descripcion'],request.json['fecha'],request.json['usuario'],request.json['estado'])
    print(request.json)
    print(newTareas)
    return newTareas

@app.route('/actualizarTarea', methods=['PUT'])
def actualizarTarea():
    tareaActual = basedatos.update_tareas(request.json['id'],request.json['descripcion'],request.json['fecha'],request.json['usuario'],request.json['estado'])
    print(request.json)
    print(tareaActual)
    return jsonify(tareaActual)

@app.route('/borrarTarea/<id>', methods=['DELETE'])
def borrarTarea(id):
    tareaBorrada = basedatos.delete_tareas(id)
    #print(request.json)
    print(tareaBorrada)
    return jsonify(tareaBorrada)

if __name__ == '__main__': 
    app.run(debug=True, port=5000)