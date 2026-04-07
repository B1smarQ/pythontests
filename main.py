from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}


def main():
    pass 

if __name__ == "__main__":
    main()
