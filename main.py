from fastapi import FastAPI

app = FastAPI()


@app.get("/true")
def read_root():
    return {"index1": True,"index2":True}
@app.get("/false")
def read_root():
    return {"index1": False,"index2":False}
