from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from modelos.restaurante import Restaurante
from schemas.restaurante import RestauranteCreate, RestauranteResponse

router = APIRouter(prefix="/restaurantes")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=RestauranteResponse)
def criar_restaurante(restaurante: RestauranteCreate, db: Session = Depends(get_db)):
    novo = Restaurante(
        nome=restaurante.nome.title(),
        categoria=restaurante.categoria.upper()
    )
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/", response_model=list[RestauranteResponse])
def listar_restaurantes(db: Session = Depends(get_db)):
    return db.query(Restaurante).all()

@router.put("/{restaurante_id}/status")
def alterar_status(restaurante_id: int, db: Session = Depends(get_db)):
    restaurante = db.query(Restaurante).filter_by(id=restaurante_id).first()
    restaurante.ativo = not restaurante.ativo
    db.commit()
    return {"mensagem": "Status atualizado!"}
