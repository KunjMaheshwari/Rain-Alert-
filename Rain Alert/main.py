import requests
import smtplib

my_email = "kunj1766@gmail.com"
password = "12345"

my_api_key = "d944eb09fc0aa936054c05041e3dd297"
my_endpoint = "https://api.openweathermap.org/data/2.5/weather"

paramters = {
    "lat": 51.507351,
    "lon": 0.127758,
    "appid": my_api_key
}

condition = requests.get(my_endpoint, params=paramters)
condition.raise_for_status()

weather_data = condition.json()
weather_slicing = weather_data["hourly"][:12]

will_rain = False

for hours in weather_slicing:
    climate = hours["weather"][0]["id"]
    if int(climate) < 700:
        will_rain = True


if will_rain:
    sending = smtplib.SMTP("smtp.gmail.com")
    sending.starttls()
    sending.login(user=my_email, password=password)
    sending.sendmail(from_addr=my_email, to_addrs="kunj1766@gmail.com",
                     msg="Subject:It's going to rain today\n\nBring an Umbrella")
