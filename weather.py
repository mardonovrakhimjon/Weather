import requests 

from config import TOKEN


class OpenWeatherClient:

    def __init__(self) -> None:
        self.base_url = 'https://api.openweathermap.org'
        self.token = TOKEN

    def get_weather(self, city: str) -> dict:
        url = f"{self.base_url}/data/2.5/weather"
        params = {
            'q': city,
            'appid': self.token,
            'units': 'metric'
        }

        response = requests.get(url=url, params=params)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            raise Exception(f"No Weather Data: {response.status_code}")
    

weather_client = OpenWeatherClient()
print(weather_client.get_weather("Samarkand"))
