from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import json


FILE = "weather.json"
app = FastAPI()

weather_lst = []

def read_json_weather_file(file):
    """
        Read json file
        Return:
                List[dict]
    """
    with open(file, "r", encoding="utf-8") as f:
        weather_lst.append(json.load(f))
    return weather_lst

class Item(BaseModel):
    location: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/sevendays_weather")
async def location_item(item: Item):
    """
        Get location from copilot studio
        Mapping location to weather data
        Return:
                Dict[List[Dict]]
    """
    print("Received location from Copilot:", item.location)
    weather_data = read_json_weather_file(FILE)
    input_location = item.location.lower().strip()
    file_location = weather_data[0]["location"]["name"].lower().strip()

    if input_location == file_location:
        forecast = weather_data[0]["forecast"]["forecastday"]
        result = []

        for day in forecast:
            result.append({
                "date": day["date"],
                "condition": day["day"]["condition"]["text"],
                "max_temp": day["day"]["maxtemp_c"],
                "min_temp": day["day"]["mintemp_c"],
                "chance_of_rain": day["day"]["daily_chance_of_rain"],
                "icon": day["day"]["condition"]["icon"]
            })

        return {
            "location": weather_data[0]["location"]["name"],
            "forecast": result
        }
    else:
        return {"message": f"Không tìm thấy dữ liệu cho '{item.location}'"}
        

    


=======
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import json


FILE = "weather.json"
app = FastAPI()

weather_lst = []

def read_json_weather_file(file):
    """
        Read json file
        Return:
                List[dict]
    """
    with open(file, "r", encoding="utf-8") as f:
        weather_lst.append(json.load(f))
    return weather_lst

class Item(BaseModel):
    location: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/sevendays_weather")
async def location_item(item: Item):
    """
        Get location from copilot studio
        Mapping location to weather data
        Return:
                Dict[List[Dict]]
    """
    print("Received location from Copilot:", item.location)
    weather_data = read_json_weather_file(FILE)
    input_location = item.location.lower().strip()
    file_location = weather_data[0]["location"]["name"].lower().strip()

    if input_location == file_location:
        forecast = weather_data[0]["forecast"]["forecastday"]
        result = []

        for day in forecast:
            result.append({
                "date": day["date"],
                "condition": day["day"]["condition"]["text"],
                "max_temp": day["day"]["maxtemp_c"],
                "min_temp": day["day"]["mintemp_c"],
                "chance_of_rain": day["day"]["daily_chance_of_rain"],
                "icon": day["day"]["condition"]["icon"]
            })

        return {
            "location": weather_data[0]["location"]["name"],
            "forecast": result
        }
    else:
        return {"message": f"Không tìm thấy dữ liệu cho '{item.location}'"}
        

    



