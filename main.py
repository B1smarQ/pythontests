from fastapi import FastAPI

app = FastAPI()


def add_two(a, b):
    return a + b

@app.get("/")
async def root():
    return {"message":"Hello World"}

@app.get("/hello")
async def hello(a: int, b: int):
    return {"message": add_two(a, b)}

