from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Conexão com SQLite
engine = create_engine("sqlite:///database/database.db", echo=True)  # 'echo=True' para ver os logs no terminal
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Usuarios(Base):
    __tablename__ = "USUARIOS"
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Nome = Column(String, nullable=False)
    Senha = Column(String, nullable=False) 

# Criação da tabela no banco de dados
Base.metadata.create_all(engine)