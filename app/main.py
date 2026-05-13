from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.routes import task

app = FastAPI(title="API de Produtividade")

app.include_router(task.router)

# cria as tabelas
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API rodando 🚀"}