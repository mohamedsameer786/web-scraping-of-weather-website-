import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://forecast.weather.gov/MapClick.php?lat=34.073600000000056&lon=-118.40045999999995#.X-Wtw1Uzapo'

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")


week = soup.find (id="current-conditions-body")
#print (week)
items = soup.find_all (class_='forecast-tombstone')
print (items[0])

print (items [0].find (class_= 'period-name').get_text())
print (items [0].find (class_= 'short-desc').get_text())
print (items [0].find (class_= 'temp').get_text())
period_names = [item.find(class_= 'period-name').get_text() for item in items ]

short_desc = [item.find(class_= 'short-desc').get_text() for item in items ]

temp = [item.find(class_= 'temp').get_text() for item in items ]
#print (period_names)
#print (short_desc)
#print (temp)

weather_stuff = pd.DataFrame(
  {
     'period':period_names,
     'day weather':short_desc,
     'temp':temp,

  }

)
print (weather_stuff)

weather_stuff.to_csv('weather.csv')