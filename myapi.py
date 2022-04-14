from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Ayu(BaseModel):
    msg:str
    sal:str

@app.get("/")
def home():
    return {"welcome" : "to first page"}

@app.get("/second")
def second():
    return {"welcome": "to second page"}

# @app.get("/{name}")
# def name(name : str):
#     return {"welcome ": name }

@app.get("/{a} {b}")
def sum(a:int , b:int):
    z=int(a)+int(b)
    return {"sum =" : z} 

@app.post("/p/{name1} {sal}")
def po( name1:str , sal:str , a1:Ayu):
    return {"post": name1}