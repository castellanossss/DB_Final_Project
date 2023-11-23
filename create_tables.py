from app import app, db
from app.models import Materias, Municipios, TipoDocumentacion, Eps, Grados, Personas, Cursos, RegistroPersona, \
    AcudientesEstudiantes, MateriaCurso, EstudianteCurso

def create_tables():
    """Crea las tablas en la base de datos."""
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_tables()
