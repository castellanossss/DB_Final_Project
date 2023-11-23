from app import db
from sqlalchemy import Float
from sqlalchemy.dialects.oracle import FLOAT


class Materias(db.Model):
    __tablename__ = "MATERIAS"

    ID_MATERIA = db.Column(db.Integer, primary_key=True)
    NOMBRE_MATERIA = db.Column(db.String(100), nullable=False)

class Municipios(db.Model):
    __tablename__ = "MUNICIPIOS"

    ID_MUNICIPIO = db.Column(db.Integer, primary_key=True)
    NOMBRE_MUNICIPIO = db.Column(db.String(50), nullable=False)

class TipoDocumentacion(db.Model):
    __tablename__ = "TIPO_DOCUMENTACION"

    ID_TIPO_DOCUMENTO = db.Column(db.Integer, primary_key=True)
    NOMBRE_TIPO_DOCUMENTO = db.Column(db.String(50), nullable=False)

class Eps(db.Model):
    __tablename__ = "EPS"

    ID_EPS = db.Column(db.Integer, primary_key=True)
    TIPO_EPS = db.Column(db.String(50), nullable=False)
    NOMBRE_EPS = db.Column(db.String(100), nullable=False, unique=True)

class Grados(db.Model):
    __tablename__ = "GRADOS"

    ID_GRADO = db.Column(db.Integer, primary_key=True)
    NOMBRE_GRADO = db.Column(db.String(50), nullable=False)

class Personas(db.Model):
    __tablename__ = "PERSONAS"

    ID_PERSONA = db.Column(db.Integer, primary_key=True)
    ID_EPS_PERSONA = db.Column(db.Integer, db.ForeignKey("EPS.ID_EPS"), nullable=False)
    ID_MUNICIPIO_PERSONA = db.Column(db.Integer, db.ForeignKey("MUNICIPIOS.ID_MUNICIPIO"), nullable=False)
    ID_TIPO_DOCUMENTO_PERSONA = db.Column(db.Integer, db.ForeignKey("TIPO_DOCUMENTACION.ID_TIPO_DOCUMENTO"), nullable=False)
    ID_GRADO_PERSONA = db.Column(db.Integer, db.ForeignKey("GRADOS.ID_GRADO"))
    CODIGO_PERSONA = db.Column(db.Integer)
    NOMBRE_PERSONA = db.Column(db.String(100), nullable=False)
    APELLIDO_PERSONA = db.Column(db.String(100), nullable=False)
    DIRECCION_RESIDENCIA_PERSONA = db.Column(db.String(100), nullable=False)
    FECHA_NACIMIENTO_PERSONA = db.Column(db.Date)
    PERFIL_PROFESOR = db.Column(db.String(250))
    TIPO_PERSONA = db.Column(db.String(3), nullable=False)

    __table_args__ = (
        db.CheckConstraint(TIPO_PERSONA.in_(['EST', 'ACU', 'PRO', 'ADM', 'DIR'])),
    )

class Cursos(db.Model):
    __tablename__ = "CURSOS"

    ID_CURSO = db.Column(db.Integer, primary_key=True)
    ID_GRADO_CURSO = db.Column(db.Integer, db.ForeignKey("GRADOS.ID_GRADO"), nullable=False)
    NOMBRE_CURSO = db.Column(db.String(50), nullable=False)

class RegistroPersona(db.Model):
    __tablename__ = "REGISTRO_PERSONA"

    ID_REGISTRO = db.Column(db.Integer, primary_key=True)
    ID_PERSONA_REGISTRO = db.Column(db.Integer, db.ForeignKey("PERSONAS.ID_PERSONA"), nullable=False)
    FECHA_VINCULACION_COLEGIO = db.Column(db.Date, nullable=False)
    FECHA_DESVINCULACION_COLEGIO = db.Column(db.Date)

class AcudientesEstudiantes(db.Model):
    __tablename__ = "ACUDIENTES_ESTUDIANTES"

    ID_ACUDIENTE = db.Column(db.Integer, db.ForeignKey("PERSONAS.ID_PERSONA"), primary_key=True)
    ID_ESTUDIANTE = db.Column(db.Integer, db.ForeignKey("PERSONAS.ID_PERSONA"), primary_key=True)

    __table_args__ = (
        db.CheckConstraint('ID_ACUDIENTE != ID_ESTUDIANTE'),
    )

class MateriaCurso(db.Model):
    __tablename__ = "MATERIA_CURSO"

    ID_MATERIA_CURSO = db.Column(db.Integer, primary_key=True)
    ID_CURSO = db.Column(db.Integer, db.ForeignKey("CURSOS.ID_CURSO"), nullable=False)
    ID_MATERIA = db.Column(db.Integer, db.ForeignKey("MATERIAS.ID_MATERIA"), nullable=False)
    ID_PERSONA = db.Column(db.Integer, db.ForeignKey("PERSONAS.ID_PERSONA"), nullable=False)

class EstudianteCurso(db.Model):
    __tablename__ = "ESTUDIANTE_CURSO"

    ID_MATERIA_CURSO = db.Column(db.Integer, db.ForeignKey("MATERIA_CURSO.ID_MATERIA_CURSO"), primary_key=True)
    ID_PERSONA = db.Column(db.Integer, db.ForeignKey("PERSONAS.ID_PERSONA"), primary_key=True)
    CALIFICACION_CURSO = db.Column(Float().with_variant(FLOAT(binary_precision=9), 'oracle'), nullable=True)
