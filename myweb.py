import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.bbc.com/weather/1275339")
soup = BeautifulSoup(page.content, 'html.parser')
fortheen_day = soup.find(id="wr-forecast")
loc=soup.find(class_="wr-c-location")
print(loc)
doc=fortheen_day.find_all(class_='wr-js-day')
tonight=doc[0]
print(tonight.prettify())
location=loc.find(id="wr-location-name-id").get_text()
period=tonight.find(class_="wr-day__title").get_text()
temp = tonight.find(class_="wr-day__temperature").get_text()
short_desc = tonight.find(class_="wr-day__details__weather-type-description").get_text()

print(location)
print(period)
print(temp)
print(short_desc)

period_tags = fortheen_day.select(".wr-day__title")
periods = [pt.get_text() for pt in period_tags]
periods
temps = [t.get_text() for t in fortheen_day.select(".wr-day__temperature")]
short_descs = [sd.get_text() for sd in fortheen_day.select(".wr-day__details__weather-type-description")]

print(temps)
print(short_descs)

import pandas as pd
weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
     "temp": temps
})

print(weather)

weather.to_csv('myweather1.csv',encoding="utf-8")
