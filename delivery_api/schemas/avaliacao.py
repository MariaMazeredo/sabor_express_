from pydantic import BaseModel

class AvaliacaoBase(BaseModel):
    cliente: str
    nota: int

class AvaliacaoCreate(AvaliacaoBase):
    restaurante_id: int

class AvaliacaoResponse(AvaliacaoBase):
    id: int

    class Config:
        orm_mode = True
