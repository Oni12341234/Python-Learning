import requests

api_key = "1ec6bd0f1d45d7e6affdf66273954280"
endpoint = "https://api.openweathermap.org/data/2.5/onecall"
params = {

"exclude": "current,minutely,daily,alerts",
"lat" : 44.4584,
"lon" : 25.9734,
"appid" : api_key,

}

will_rain = False

response = requests.get(endpoint, params=params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella.")