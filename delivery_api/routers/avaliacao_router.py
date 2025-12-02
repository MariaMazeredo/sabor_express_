from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from modelos.avaliacao import Avaliacao
from schemas.avaliacao import AvaliacaoCreate, AvaliacaoResponse

router = APIRouter(prefix="/avaliacoes")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AvaliacaoResponse)
def criar_avaliacao(av: AvaliacaoCreate, db: Session = Depends(get_db)):
    nova = Avaliacao(
        cliente=av.cliente,
        nota=av.nota,
        restaurante_id=av.restaurante_id
    )
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova
