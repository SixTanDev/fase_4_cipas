"""
Práctica CIPAS - Programación 213023

Crear una clase llamada Estudiante usando programación orientada a objetos.

La clase debe tener los siguientes atributos:
- nombre
- edad
- codigo
- carrera
-prueba

Debe incluir:
- un constructor __init__
- validaciones para evitar datos vacíos
- validación para que la edad sea mayor que cero
- un método mostrar_datos que retorne la información del estudiante
- un método presentarse que retorne un mensaje de presentación
- manejo de excepciones usando try y except

El objetivo es practicar clases, objetos, métodos, validaciones y manejo básico de errores antes de subir el proyecto a GitHub.

"""
class Estudiante:
    def __init__(self, nombre, edad, codigo, carrera):
        if not nombre or not codigo or not carrera:
            raise ValueError("Los campos nombre, código y carrera no pueden estar vacíos.")
        if edad <= 0:
            raise ValueError("La edad debe ser mayor que cero.")

        self.nombre = nombre
        self.edad = edad
        self.codigo = codigo
        self.carrera = carrera

    def mostrar_datos(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Código: {self.codigo}, Carrera: {self.carrera}"

    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre} y estudio {self.carrera}."


# Ejemplo de uso
estudiantes = []

datos_estudiantes = [
    ("Juan Pérez", 20, "12345", "Ingeniería en Sistemas"),
    ("", 22, "67890", "Medicina"),
    ("Ana Gómez", 5, "54321", "Derecho"),
    ("Luis Ramírez", -1, "98765", "Arquitectura"),
]

for datos in datos_estudiantes:
    try:
        estudiante = Estudiante(*datos)
        estudiantes.append(estudiante)
    except ValueError as e:
        print(f"Error al crear el estudiante: {e}")

for estudiante in estudiantes:
    print(estudiante.mostrar_datos())
    print(estudiante.presentarse())