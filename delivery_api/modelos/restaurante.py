from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Restaurante(Base):
    __tablename__ = "restaurantes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    ativo = Column(Boolean, default=False)

    avaliacao = relationship(
        "Avaliacao",
        back_populates="restaurante",
        cascade="all, delete"
    )

    
        




