from flask import request, jsonify, make_response
from .models import db, Materias, Municipios, TipoDocumentacion
from . import app

# CRUD para MATERIAS

# Crear una nueva materia
@app.route('/app/create/materia', methods=['POST'])
def create_materia():
    data = request.json

    if Materias.query.filter_by(ID_MATERIA=data['id_materia']).first():
        return make_response(jsonify({'message': 'Ya existe una Materia con este ID.'}), 400)

    nueva_materia = Materias(ID_MATERIA=data['id_materia'], NOMBRE_MATERIA=data['nombre_materia'])
    db.session.add(nueva_materia)
    try:
        db.session.commit()
        return jsonify({'message': 'Materia creada exitosamente!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# Obtener todas las materias
@app.route('/app/get/materias', methods=['GET'])
def get_materias():
    materias = Materias.query.all()
    return jsonify([{'id_materia': m.ID_MATERIA, 'nombre_materia': m.NOMBRE_MATERIA} for m in materias])


# Obtener una materia por ID
@app.route('/app/get/materia/<int:id_materia>', methods=['GET'])
def get_materia(id_materia):
    materia = Materias.query.get(id_materia)
    if materia:
        return jsonify({'id_materia': materia.ID_MATERIA, 'nombre_materia': materia.NOMBRE_MATERIA})
    else:
        return make_response(jsonify({'message': 'Materia no encontrada!'}), 404)


# Actualizar una materia
@app.route('/app/update/materia/<int:id_materia>', methods=['PUT'])
def update_materia(id_materia):
    materia = Materias.query.get(id_materia)
    if not materia:
        return make_response(jsonify({'message': 'Materia no encontrada!'}), 404)

    data = request.json
    materia.NOMBRE_MATERIA = data['nombre_materia']
    try:
        db.session.commit()
        return jsonify({'message': 'Materia actualizada exitosamente!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# Eliminar una materia
@app.route('/app/delete/materia/<int:id_materia>', methods=['DELETE'])
def delete_materia(id_materia):
    materia = Materias.query.get(id_materia)
    if not materia:
        return make_response(jsonify({'message': 'Materia no encontrada!'}), 404)

    try:
        db.session.delete(materia)
        db.session.commit()
        return jsonify({'message': 'Materia eliminada exitosamente!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500



# CRUD para MUNICIPIOS


# Crear un nuevo municipio
@app.route('/app/create/municipio', methods=['POST'])
def create_municipio():
    data = request.json
    if Municipios.query.filter_by(ID_MUNICIPIO=data['id_municipio']).first():
        return make_response(jsonify({'message': 'Ya existe un Municipio con ese ID.'}), 400)

    nuevo_municipio = Municipios(ID_MUNICIPIO=data['id_municipio'], NOMBRE_MUNICIPIO=data['nombre_municipio'])
    db.session.add(nuevo_municipio)
    try:
        db.session.commit()
        return jsonify({'message': 'Municipio creado exitosamente!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# Obtener todos los municipios
@app.route('/app/get/municipios', methods=['GET'])
def get_municipios():
    municipios = Municipios.query.all()
    return jsonify([{'id_municipio': m.ID_MUNICIPIO, 'nombre_municipio': m.NOMBRE_MUNICIPIO} for m in municipios])


# Obtener un municipio por ID
@app.route('/app/get/municipio/<int:id_municipio>', methods=['GET'])
def get_municipio(id_municipio):
    municipio = Municipios.query.get(id_municipio)
    if municipio:
        return jsonify({'id_municipio': municipio.ID_MUNICIPIO, 'nombre_municipio': municipio.NOMBRE_MUNICIPIO})
    else:
        return make_response(jsonify({'message': 'Municipio no encontrado!'}), 404)


# Actualizar un municipio
@app.route('/app/update/municipio/<int:id_municipio>', methods=['PUT'])
def update_municipio(id_municipio):
    municipio = Municipios.query.get(id_municipio)
    if not municipio:
        return make_response(jsonify({'message': 'Municipio no encontrado!'}), 404)

    data = request.json
    municipio.NOMBRE_MUNICIPIO = data['nombre_municipio']
    try:
        db.session.commit()
        return jsonify({'message': 'Municipio actualizado exitosamente!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# Eliminar un municipio
@app.route('/app/delete/municipio/<int:id_municipio>', methods=['DELETE'])
def delete_municipio(id_municipio):
    municipio = Municipios.query.get(id_municipio)
    if not municipio:
        return make_response(jsonify({'message': 'Municipio no encontrado!'}), 404)

    try:
        db.session.delete(municipio)
        db.session.commit()
        return jsonify({'message': 'Municipio eliminado exitosamente!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# CRUD para TIPO_DOCUMENTACION

# Crear un nuevo tipo de documentación
@app.route('/app/create/tipo_documentacion', methods=['POST'])
def create_tipo_documentacion():
    data = request.json
    if TipoDocumentacion.query.filter_by(ID_TIPO_DOCUMENTO=data['id_tipo_documento']).first():
        return make_response(jsonify({'message': 'Y aexiste un Tipo de Documento con este ID.'}), 400)

    nuevo_tipo = TipoDocumentacion(ID_TIPO_DOCUMENTO=data['id_tipo_documento'], NOMBRE_TIPO_DOCUMENTO=data['nombre_tipo_documento'])
    db.session.add(nuevo_tipo)
    try:
        db.session.commit()
        return jsonify({'message': 'Tipo de Documentación creado exitosamente!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# Obtener todos los tipos de documentación
@app.route('/app/get/tipos_documentacion', methods=['GET'])
def get_tipos_documentacion():
    tipos = TipoDocumentacion.query.all()
    return jsonify([{'id_tipo_documento': t.ID_TIPO_DOCUMENTO, 'nombre_tipo_documento': t.NOMBRE_TIPO_DOCUMENTO} for t in tipos])


# Obtener un tipo de documentación por ID
@app.route('/app/get/tipo_documentacion/<int:id_tipo_documento>', methods=['GET'])
def get_tipo_documentacion(id_tipo_documento):
    tipo = TipoDocumentacion.query.get(id_tipo_documento)
    if tipo:
        return jsonify({'id_tipo_documento': tipo.ID_TIPO_DOCUMENTO, 'nombre_tipo_documento': tipo.NOMBRE_TIPO_DOCUMENTO})
    else:
        return make_response(jsonify({'message': 'Tipo de Documentación no encontrado!'}), 404)


# Actualizar un tipo de documentación
@app.route('/app/update/tipo_documentacion/<int:id_tipo_documento>', methods=['PUT'])
def update_tipo_documentacion(id_tipo_documento):
    tipo = TipoDocumentacion.query.get(id_tipo_documento)
    if not tipo:
        return make_response(jsonify({'message': 'Tipo de Documentación no encontrado!'}), 404)

    data = request.json
    tipo.NOMBRE_TIPO_DOCUMENTO = data['nombre_tipo_documento']
    try:
        db.session.commit()
        return jsonify({'message': 'Tipo de Documentación actualizado exitosamente!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# Eliminar un tipo de documentación
@app.route('/app/delete/tipo_documentacion/<int:id_tipo_documento>', methods=['DELETE'])
def delete_tipo_documentacion(id_tipo_documento):
    tipo = TipoDocumentacion.query.get(id_tipo_documento)
    if not tipo:
        return make_response(jsonify({'message': 'Tipo de Documentación no encontrado!'}), 404)

    try:
        db.session.delete(tipo)
        db.session.commit()
        return jsonify({'message': 'Tipo de Documentación eliminado exitosamente!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


