from src.database.database_schema import Usuarios, session
from src.views.responses import ResponseOK, ResponseErro

class UserController:
    @classmethod
    def criar_novo_usuario(cls, nome, senha):
        usuario_existente = session.query(Usuarios).filter_by(Nome = nome).first()
        if usuario_existente:
            return ResponseErro.usuario_ja_existe_bd(nome)
        
        session.add(Usuarios(Nome = nome, Senha = senha))
        session.commit()
        return ResponseOK.usuario_cadastrado_sucesso(nome)

    @classmethod
    def visualizar_todos_usuarios(cls):
        return session.query(Usuarios).all()
        
