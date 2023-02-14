import requests
import os
from twilio.rest import Client
API_KEY = "672264e249e911c6c1095e3f8af84ebb"
LAT = 11.186630
LONG = 108.605870
WEATHER_END_POINT = "https://api.openweathermap.org/data/2.5/weather"
parameters = {
    'lat': LAT,
    'lon': LONG,
    'appid': API_KEY,
    'lang': 'vi'
}

response = requests.get(WEATHER_END_POINT, params=parameters)
response.raise_for_status()
data_weather = response.json()

current_weather = data_weather['weather'][0]['description']


def send_sms(current_weather):
    # Set environment variables for your credentials
    # Read more at http://twil.io/secure
    account_sid = "ACfb74dc414ea5930a9855e6877c927666"
    auth_token = "82f33c313e06006a39e59263f611a07a"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"Thời tiết hôm nay : {current_weather}",
        from_="+17752274238",
        to="+84924967332"
    )

    print(message.sid)


send_sms(current_weather)
