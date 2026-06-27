from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import SessionLocal, engine, Base
from app.models import Game

Base.metadata.create_all(bind=engine)

app = FastAPI(title="LevelShelf", version="0.1.0")


class GameCreate(BaseModel):
    title: str
    platform: str | None = None
    genre: str | None = None
    release: str | None = None
    rating: float | None = None


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Welcome to LevelShelf: Your personal video game catalog :D"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/games")
def create_game(game: GameCreate, db: Session = Depends(get_db)):
    db_game = Game(**game.model_dump())
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


@app.get("/games")
def list_games(db: Session = Depends(get_db)):
    return db.query(Game).all()


@app.get("/games/{game_id}")
def get_game(game_id: int, db: Session = Depends(get_db)):
    game = db.query(Game).filter(Game.id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game