from twilio.rest import Client
from weather import WeatherWrapper

import json
import pandas as pd

def read_secrets(secrets_path: str):
    with open(secrets_path + '/secrets.json') as f:
        data = json.load(f)
        return data

def send_message(client: Client, message_body: str, from_number: str, to_number: str):
    message = client.messages.create(
    body= message_body,
    from_= from_number,
    to= to_number,
    )
    print(message.body)

def main():

    secrets=read_secrets("C:/.dev/weather-app/configs")
    client = Client(secrets["twilioSID"],secrets["twilioAuthToken"])

    lisbon_weather = WeatherWrapper(38.736946,-9.142685,"Lisboa")
    lisbon_weather.get_weather(secrets["openWeatherApiKey"])

    
if __name__ == "__main__":
    main()