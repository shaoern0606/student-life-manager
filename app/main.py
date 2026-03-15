from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Student Life Manager AI running"}

@app.get("/health")
def health():
    return {"status": "ok"}