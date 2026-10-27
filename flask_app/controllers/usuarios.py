from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/registro", methods=["POST"])
def registro():
    print("Entro a regisrro")
    if not Usuario.validar_registro(request.form):
        print("validaar")
        return redirect("/")
    
    pass_hasheado = bcrypt.generate_password_hash(
        request.form["password"]
    )
    
    
    data = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"],
        "password": pass_hasheado
    }
    
    usuario_id = Usuario.save(data)
    print("usuario id ", usuario_id)
    session["usuario_id"] = usuario_id
    
    return redirect("/dashboard")

@app.route("/login", methods=["POST"])
def login():
    usuario = Usuario.get_by_email({
        "email": request.form["email"]
    })
    if not usuario:
        flash("email o constraseña incorrecto")
        return redirect("/")
    if not bcrypt.check_password_hash(
        usuario.password,
        request.form["password"]
    ):
        flash("email o contrasela incorecto")
    session["usuario_id"] = usuario.id
    return redirect("/dashboard")

@app.route("/cerrar_sesion")
def cerrar_sesion():
    session.clear()
    return redirect("/")