from fastapi import FastApi, HIPExeption
from typing import list
import database
import models
from models import movie, MovieCreate


app = FastAPI()
 @app.get("/")
 def read_root():
     return{"message": "Welcome to Crud"}