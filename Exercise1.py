import urequests as requests 
import ujson as json
from machine import Pin, I2C
import ssd1306

url = f"http://dataservice.accuweather.com/forecasts/v1/daily/1day/204108?apikey=dCYDw6mVNmnPhVw8Q3k8e0fGR4IPOQve"

response = requests.get(url).json()["DailyForecasts"][0]

Temperature = str(response["Temperature"]["Minimum"]["Value"]) + response["Temperature"]["Minimum"]["Unit"] + \
                " - " + str(response["Temperature"]["Maximum"]["Value"]) + response["Temperature"]["Maximum"]["Unit"]
Weather = response["Day"]["IconPhrase"]


i2c = I2C(sda=Pin(0), scl=Pin(2))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

display.text(Temperature, 15, 35, 1)
display.text(Weather, 15, 45, 1)

display.show()
# Attached Snap as 'Exercise1.jpeg'
