#fast api
from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()

#what is swagger : testing goodbye to postman welcome to swagger

#micro service
#by defualt supports async await
@app.get('/')
async def home():
    return{'msg':'Welcome to Fast API'}
    


class Contact(BaseModel):
    cid:int
    name:str
    username:str
    password:str

@app.post('/contact',description='create a single contact')    
async def create_contact(contact: Contact):
    '''to insert contact in db'''
    return contact


#http://localhost:8000/docs is the swagger
#to run this uvicorn main:app --reload