from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.mision import Mision
from flask_app.models.usuario import Usuario

@app.route("/dashboard")
def dashboard():
    if "usuario_id" not in session:
        return redirect("/")
    usuario = Usuario.get_by_id({
        "id":session["usuario_id"]
    })
    misiones = Mision.get_all()
    return render_template("dashboard.html",usuario=usuario, misiones=misiones
    )
    
@app.route("/nueva")
def nueva():
    if "usuario_id" not in session:
        return redirect("/")
    return render_template("nueva_mision.html")
@app.route("/crear_mision", methods=["POST"])
def crear_mision():
    if not Mision.validar(request.form):
        return redirect("/nueva")
    data = {
        "nombre": request.form["nombre"],
        "fecha": request.form["fecha"],
        "voluntariados_necesarios": request.form["voluntariados_necesarios"],
        "descripcion": request.form["descripcion"],
        "usuarios_id": request.form["usuarios_id"]
    }
    Mision.save(data)
    return redirect("/dashboard")
