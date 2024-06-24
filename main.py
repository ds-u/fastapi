from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SensorData(BaseModel):
    temperature:float
    humidity:float
    
@app.post("/postSensorData")
def post_data(data:SensorData):
    print(data)
    return{
        "temperature: ": {data.temperature},
        "humidity: ": {data.humidity}
    }
    