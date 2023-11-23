from flask import request, jsonify, make_response
from .models import db, Materias, Municipios, TipoDocumentacion, Eps, Grados, Cursos
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

    nuevo_tipo = TipoDocumentacion(ID_TIPO_DOCUMENTO=data['id_tipo_documento'],
                                   NOMBRE_TIPO_DOCUMENTO=data['nombre_tipo_documento'])
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
    return jsonify(
        [{'id_tipo_documento': t.ID_TIPO_DOCUMENTO, 'nombre_tipo_documento': t.NOMBRE_TIPO_DOCUMENTO} for t in tipos])


# Obtener un tipo de documentación por ID
@app.route('/app/get/tipo_documentacion/<int:id_tipo_documento>', methods=['GET'])
def get_tipo_documentacion(id_tipo_documento):
    tipo = TipoDocumentacion.query.get(id_tipo_documento)
    if tipo:
        return jsonify(
            {'id_tipo_documento': tipo.ID_TIPO_DOCUMENTO, 'nombre_tipo_documento': tipo.NOMBRE_TIPO_DOCUMENTO})
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


# CRUD para EPS

# Crea una nueva EPS
@app.route('/app/create/eps', methods=['POST'])
def create_eps():
    data = request.json
    if Eps.query.filter_by(ID_EPS=data['id_eps']).first():
        return make_response(jsonify({'message': 'Ya existe una EPS con esta id.'}), 400)

    nuevo_tipo = Eps(ID_EPS=data['id_eps'],
                     TIPO_EPS=data['tipo_de_eps'],
                     NOMBRE_EPS=data['nombre_de_la_eps'])
    db.session.add(nuevo_tipo)
    try:
        db.session.commit()
        return jsonify({'message': 'Eps creada exitosamente!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# Obtener todas las eps
@app.route('/app/get/eps', methods=['GET'])
def get_epss():
    tipos = Eps.query.all()
    return jsonify([{'id_eps': e.ID_EPS, 'tipo_de_eps': e.TIPO_EPS, 'nombre_eps': e.NOMBRE_EPS} for e in tipos])


# Obtener eps por ID
@app.route('/app/get/eps/<int:id_eps>', methods=['GET'])
def get_eps(id_eps):
    tipo = Eps.query.get(id_eps)
    if tipo:
        return jsonify({'id_eps': tipo.ID_EPS, 'tipo_de_eps': tipo.TIPO_EPS, 'nombre_eps': tipo.NOMBRE_EPS})
    else:
        return make_response(jsonify({'message': 'Tipo de Eps no encontrada!'}), 404)


# Actualizar una eps

@app.route('/app/update/eps/<int:id_eps>', methods=['PUT'])
def update_eps(id_eps):
    tipo = Eps.query.get(id_eps)
    if not tipo:
        return make_response(jsonify({'message': 'Nombre de Eps no encontrado!'}), 404)

    data = request.json
    tipo.NOMBRE_EPS = data['nombre_eps']
    try:
        db.session.commit()
        return jsonify({'message': 'Nombre de Eps actualizado exitosamente!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# Eliminar Eps
@app.route('/app/delete/eps/<int:id_eps>', methods=['DELETE'])
def delete_eps(id_eps):
    tipo = Eps.query.get(id_eps)
    if not tipo:
        return make_response(jsonify({'message': 'Tipo de Eps no encontrado!'}), 404)

    try:
        db.session.delete(tipo)
        db.session.commit()
        return jsonify({'message': 'Tipo de Eps eliminado exitosamente!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# CRUD para Grados

# Crear un nuevo Grado
@app.route('/app/create/grado', methods=['POST'])
def create_grado():
    data = request.json

    if Grados.query.filter_by(ID_GRADO=data['id_grado']).first():
        return make_response(jsonify({'message': 'Ya existe un Grado con este ID.'}), 400)

    nuevo_grado = Grados(ID_GRADO=data['id_grado'], NOMBRE_GRADO=data['nombre_grado'])
    db.session.add(nuevo_grado)
    try:
        db.session.commit()
        return jsonify({'message': 'Grado creada exitosamente!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# Obtener todos los  grados
@app.route('/app/get/grados', methods=['GET'])
def get_grados():
    grados = Grados.query.all()
    return jsonify([{'id_grado': g.ID_GRADO, 'nombre_grado': g.NOMBRE_GRADO} for g in grados])


# Obtener un Grado por ID
@app.route('/app/get/grado/<int:id_grado>', methods=['GET'])
def get_grado(id_grado):
    grado = Grados.query.get(id_grado)
    if grado:
        return jsonify({'id_grado': grado.ID_GRADO, 'nombre_grado': grado.NOMBRE_GRADO})
    else:
        return make_response(jsonify({'message': 'Grado no encontrado!'}), 404)


# Actualizar un grado
@app.route('/app/update/grado/<int:id_grado>', methods=['PUT'])
def update_grado(id_grado):
    grado = Grados.query.get(id_grado)
    if not grado:
        return make_response(jsonify({'message': 'Grado no encontrado!'}), 404)

    data = request.json
    grado.NOMBRE_GRADO = data['nombre_grado']
    try:
        db.session.commit()
        return jsonify({'message': 'Grado actualizada exitosamente!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# Eliminar un grado
@app.route('/app/delete/grado/<int:id_grado>', methods=['DELETE'])
def delete_grado(id_grado):
    grado = Grados.query.get(id_grado)
    if not grado:
        return make_response(jsonify({'message': 'Grado no encontrada!'}), 404)

    try:
        db.session.delete(grado)
        db.session.commit()
        return jsonify({'message': 'Grado eliminada exitosamente!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# CRUD para Cursoso

# Crear un nuevo Cursoso
@app.route('/app/create/curso', methods=['POST'])
def create_curso():
    data = request.json

    if Cursos.query.filter_by(ID_GRADO=data['id_curso']).first():
        return make_response(jsonify({'message': 'Ya existe un Curso con este ID.'}), 400)

    nuevo_curso = Cursos(ID_CURSO=data['id_curso'], ID_GRADO_CURSO=data['id_grado_curso'], NOMBRE_CURSO=data['nombre_curso'])
    db.session.add(nuevo_curso)
    try:
        db.session.commit()
        return jsonify({'message': 'Curso creada exitosamente!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# Obtener todos los  Cursos
@app.route('/app/get/cursos', methods=['GET'])
def get_cursos():
    cursos = Cursos.query.all()
    return jsonify([{'id_curso': c.ID_CURSO, 'id_grado_curso': c.ID_GRADO_CURSO, 'nombre_curso':c.NOMBRE_CURSO} for c in cursos])


# Obtener un Cursos por ID
@app.route('/app/get/curso/<int:id_curso>', methods=['GET'])
def get_curso(id_curso):
    curso = Cursos.query.get(id_curso)
    if curso:
        return jsonify({'id_curso': curso.ID_CURSO, 'id_grado_curso': curso.ID_GRADO_CURSO, curso.NOMBRE_CURSO:'nombre_curso'})
    else:
        return make_response(jsonify({'message': 'Curso no encontrado!'}), 404)


# Actualizar un Curso
@app.route('/app/update/curso/<int:id_curso>', methods=['PUT'])
def update_curso(id_curso):
    curso = Cursos.query.get(id_curso)
    if not curso:
        return make_response(jsonify({'message': 'Curso no encontrado!'}), 404)

    data = request.json
    curso.NOMBRE_CURSO = data['nombre_curso']
    try:
        db.session.commit()
        return jsonify({'message': 'Curso actualizada exitosamente!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# Eliminar un Curso
@app.route('/app/delete/curso/<int:id_curso>', methods=['DELETE'])
def delete_curso(id_curso):
    curso = Cursos.query.get(id_curso)
    if not curso:
        return make_response(jsonify({'message': 'Curso no encontrada!'}), 404)

    try:
        db.session.delete(curso)
        db.session.commit()
        return jsonify({'message': 'Cursos eliminada exitosamente!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


