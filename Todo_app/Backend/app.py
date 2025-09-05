from flask import Flask, request, jsonify
from db import get_cursor_dict
from flask_cors import CORS
import mysql.connector

app = Flask(_name_)
CORS(app)



# Rutas API
@app.route("/api/tareas", methods=["GET"])
def get_tareas():
    cursor.execute("SELECT * FROM tareas")
    return jsonify(cursor.fetchall())

@app.route("/api/tareas", methods=["POST"])
def add_tarea():
    data = request.json
    cursor.execute(
        "INSERT INTO tareas (titulo, descripcion, estado, usuario_id) VALUES (%s, %s, 'pendiente', %s)",
        (data["titulo"], data["descripcion"], data["usuario_id"])
    )
    db.commit()
    return jsonify({"message": "Tarea creada"}), 201

@app.route("/api/tareas/<int:id>", methods=["PUT"])
def update_tarea(id):
    data = request.json
    cursor.execute("UPDATE tareas SET estado=%s WHERE id=%s", (data["estado"], id))
    db.commit()
    return jsonify({"message": "Tarea actualizada"})

@app.route("/api/tareas/<int:id>", methods=["DELETE"])
def delete_tarea(id):
    cursor.execute("DELETE FROM tareas WHERE id=%s", (id,))
    db.commit()
    return jsonify({"message": "Tarea eliminada"})

if _name_ == "_main_":
    app.run(debug=True)