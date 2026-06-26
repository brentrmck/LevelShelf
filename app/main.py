from fastapi import FastAPI

app = FastAPI(title="LevelShelf", version="0.1.0")


@app.get("/")
def root():
    return {"message": "Welcome to LevelShelf: Your personal video game catalog :D"}


@app.get("/health")
def health():
    return {"status": "ok"}
