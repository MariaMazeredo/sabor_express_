from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Avaliacao(Base):
    __tablename__ = "avaliacoes"

    id = Column(Integer, primary_key=True, index=True)
    cliente = Column(String, nullable=False)
    nota = Column(Integer, nullable=False)

    restaurante_id = Column(Integer, ForeignKey("restaurantes.id"))

    restaurante = relationship("Restaurante", back_populates="avaliacao")
