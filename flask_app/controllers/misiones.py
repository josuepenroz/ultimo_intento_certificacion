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
        "usuarios_id": session["usuario_id"]
    }
    Mision.save(data)
    return redirect("/dashboard")
@app.route("/ver/<int:id>")
def ver_mision(id):
    if "usuario_id" not in session:
        return redirect("/")
    mision = Mision.get_by_id({
        "id":id
    })
    return render_template(
        "ver_mision.html" ,mision=mision
    )
@app.route("/actualizar/<int:id>", methods=["POST"])
def actualizar(id):
    data = {
        "id":  id,
        "nombre":  request.form["nombre"],
        "fecha":  request.form["fecha"],
        "voluntariados_necesarios":  request.form["voluntariados_necesarios"],
        "descripcion":  request.form["descripcion"],
    }
    Mision.updated(data)
    return redirect("/dashboard")
@app.route("/borrar/<int:id>")
def borrar(id):
    Mision.delete({
        "id":id
        })
    return redirect("/dashboard")
