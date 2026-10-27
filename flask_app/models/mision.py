from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Mision:

    db = "Voluntariado"

    def __init__(self,data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.fecha = data["fecha"]
        self.voluntariados_necesarios = data["voluntariados_necesarios"]
        self.descripcion = data["descripcion"]
        self.usuarios_id = data["usuarios_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    @classmethod 
    def get_all(cls):
        query  = """SELECT * FROM misiones"""
        resultado = connectToMySQL(cls.db).query_db(query)
        misiones = []
        for fila in  resultado:
            misiones.append(cls(fila)) 
        return misiones
    @classmethod 
    def save(cls,data):
        query  = """INSERT INTO misiones
        (nombre,fecha,voluntariado_necesarios,descripcion, usuarios_id, created_at,updated_at) VALUES (%(nombre)s, %(fecha)s, %(voluntariados_necesarios)s, %(descripcion)s, %(usuarios_id)s, NOW(), NOW())
        
        """
        return connectToMySQL(cls.db).query_db(query,data)
    @staticmethod
    def validar(data):
        is_valid = True
        
        if len(data["nombre"]) < 1:
            flash("El nombre es obligatorio")
            is_valid = False
        if len(data["fecha"]) < 1:
            flash("El fecha es obligatorio")
            is_valid = False
        if len(data["descripcion"]) < 1:
            flash("El descripcion es obligatorio")
            is_valid = False
        if int(data["voluntariados_necesarios"]) < 2 or 
        int(data["voluntariados_necesarios"]) > 20:
        flash("Los v deben ser en 2 y 20")
        is_valid = False
        return is_valid