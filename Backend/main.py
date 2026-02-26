from fastapi import FastAPI

app = FastAPI(title="Company Analysis API", version="1.0.0")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/welcome")
def welcome():
    return {"message": "Welcome to the Company Analysis API!"}
