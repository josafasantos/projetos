# Importando as bibliotecas
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np


# Inicializa o FastAPI
app = FastAPI()
model = joblib.load(r'C:\Users\josaf\Documents\Aulas\aulas\Ciencia-dados\35-deploy-modelo-api-ml\app\model.joblib')

class InputDate(BaseModel):
  features: list[float]

@app.post('/predict')
def predict(data: InputDate):
  prediction = model.predict([data.features])
  return {"prediction":int(prediction[0])}