import requests, json

forecastURL = "https://api.openweathermap.org/data/2.5/forecast?"
gweatherURL = "https://api.openweathermap.org/data/2.5/weather?"

#Openweather forecast => 5 days divided in intervals of 3 hours
#

class WeatherWrapper:

    def __init__(self, lat: float, lon: float, location_name: str):
        self.lat = lat
        self.lon = lon
        self.location = location_name
        
    def get_weather(self, key: str):
        print("Calling weather API...")
        base_url = forecastURL + f"lat={self.lat}&lon={self.lon}&appid={key}"

        response = requests.get(base_url).json()

        print(response["list"][0]["dt_txt"])
        #print(json.dumps(response, indent=2))

    def __str__(self, ):
        return True