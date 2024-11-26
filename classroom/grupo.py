import re
from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def _init_(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas if asignaturas else []
        self.listadoAlumnos = estudiantes if estudiantes else []

    def listadoAsignaturas(self, **kwargs):
        for nombre_asignatura in kwargs.values():
            self._asignaturas.append(Asignatura(nombre_asignatura, None))

    def agregarAlumno(self, alumno, otrosAlumnos=None):
        if isinstance(alumno, str):
            self.listadoAlumnos.append(alumno)
        
        if otrosAlumnos and isinstance(otrosAlumnos, list):
            self.listadoAlumnos.extend(otrosAlumnos)

        self.listadoAlumnos.sort(key=self._extract_number)

    def _extract_number(self, alumno):
        match = re.search(r'(\d+)$', alumno)
        return int(match.group(1)) if match else 0

    @classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    def _str_(self):
        return f"Grupo de estudiantes: {self._grupo}"