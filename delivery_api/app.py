from fastapi import FastAPI
from database import Base, engine
from routers import restaurante_router, avaliacao_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Delivery API")

app.include_router(restaurante_router.router)
app.include_router(avaliacao_router.router)
@app.get("/")
def read_root():
    return {"message": "Welcome to the Delivery API!"}