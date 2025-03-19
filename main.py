from fastapi import FastAPI
from models.user_model import Usuario
from controllers.user_controller import UserController

app = FastAPI(title="Usuarios",
              version="0.0.1",
              description="Visualizar, incluir, edita e apagar usuarios")

@app.get('/v1/usuarios')
def visualizar_usuarios():
    return UserController.visualizar_todos_usuarios()

@app.post("/v1/usuarios/criar")
def criar_usuario(user:Usuario):
    return UserController.criar_novo_usuario(user.nome, user.senha)
