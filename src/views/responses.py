from fastapi.responses import JSONResponse
from fastapi import status

class ResponseOK:
    @classmethod
    def usuario_cadastrado_sucesso(cls, nome: str):
        return JSONResponse(
            status_code=status.HTTP_201_CREATED, 
            content={"code": 201, "message": f'Usuário {nome}, cadastrado com sucesso! '}
        )

class ResponseErro:
    @classmethod
    def usuario_ja_existe_bd(cls, nome: str):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT, 
            content={"code": 409, "message": f'Usuário {nome}, já existe na base de dados! '}
        )

