from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/data")
async def get_data():
    return {"data": [1, 2, 3], "data2": [1, 2, 3]}