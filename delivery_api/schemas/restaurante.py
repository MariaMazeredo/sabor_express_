from pydantic import BaseModel

class RestauranteBase(BaseModel):
    nome: str
    categoria: str

class RestauranteCreate(RestauranteBase):
    pass

class RestauranteResponse(RestauranteBase):
    id: int
    ativo: bool

    class Config:
        orm_mode = True