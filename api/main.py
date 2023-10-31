from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/sheet")
async def root():
    return {"message": "Sheet"}


@app.get("/pg")
async def root():
    return {"message": "This is my pg"}