from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$')

class Usuario:
    db = "Voluntariado"
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    @classmethod
    def save(cls,data):
        query = """
        INSERT INTO usuarios (nombre,apellido,email,password,created_at,updated_at) VALUES
        (%(nombre)s, %(apellido)s, %(email)s, %(password)s, NOW(),NOW());
        
        """
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        resultado = connectToMySQL(cls.db).query_db(query,data)
        
        if len(resultado) < 1:
            return False
        return cls(resultado[0])
    @classmethod
    def get_by_id(cls,data):
        query  = "SELECT * FROM usuarios WHERE id = %(id)s"
        resultado = connectToMySQL(cls.db).query_db(query,data)
        if len(resultado) < 1:
            return False
        return cls(resultado[0])
    @staticmethod
    def validar_registro(data):
        is_valid = True
        if len(data["nombre"]) < 1:
            flash("Nombre debe tener almenos 2 caracteres")
            is_valid = False
        if len(data["apellido"]) < 1:
            flash("apellido debe tener almenos 2 caracteres")
            is_valid = False
       
        if not EMAIL_REGEX.match(data["email"]):
            flash("Email invalido")
            is_valid = False
        usuario = Usuario.get_by_email({
            "email": data["email"]
            })
        if usuario:
            flash("correo ya ingresado")
            is_valid = False
        if len(data["password"]) < 8:
            flash("la contr")
            is_valid = False
        if data["password"] != data ["confirmar_password"]:
            flash("las contraseñas no son iguales")
            is_valid = False
        return is_valid