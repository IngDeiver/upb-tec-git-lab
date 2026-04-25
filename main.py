from flask import Flask,request

app = Flask(__name__)

usuarios = [
    {"id": 1, "nombre": "Pablito"},
    {"id": 2, "nombre": "Julian"},
    {"id": 3, "nombre": "Pedro"},
    {"id": 4, "nombre": "luis"}
    
]

# controlador para endpoint /usuarios
@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return usuarios

@app.route("/usuarios/<int:id>", methods=["GET"])
def obtenerPorId(id):
    for usuario in usuarios:
       if(usuario["id"] == id):
           return usuario
    return {"message": "User not found!"}, 404


@app.route("/usuarios/<int:id>", methods=["DELETE"])
def removePorId(id):
    for usuario in usuarios:
       if(usuario["id"] == id):
           usuarios.remove(usuario)
           return  {"message": "User removed"}
    return {"message": "User NOT FOUND"}, 404

@app.route("/usuarios", methods=["POST"])
def create():
    data = request.json
    usuario ={
            "id": len(usuarios) +1,
            "nombre": data["nombre"]
        }
    usuarios.append(usuario)
    return usuario,201
   


app.run(debug=True)