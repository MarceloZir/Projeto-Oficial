from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Bia S2"}

@app.get("/teste1")
async def funcaoteste():
    return {"teste": "deu certo"}