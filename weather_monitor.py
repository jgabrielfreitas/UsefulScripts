import requests
import json
import schedule
import time

# $ pip install schedule
# MY_API_KEY = "3ca33a17f8d231c4ea91bd9dd9b1ecf4"
DEV_API_KEY = "44db6a862fba0b067b1930da0d769e98"

def job():
    city = "rio de janeiro"
    country = "br"
    url = "http://api.openweathermap.org/data/2.5/weather?q={0},{1}&lang=pt&appid={2}".format(city, country, DEV_API_KEY)
    response = requests.request("GET", url)
    data = json.loads(response.text)
    list_of_weathers = data['weather']
    current_weather = list_of_weathers[0]
    main = current_weather['main']
    description = current_weather['description']
    if(main == 'Rain'):
        # notify users
        print main
        print description
    else:
        print "do nothing"
    print '============================='

# schedule.every(1).minutes.do(job)
schedule.every().day.do(job)

while True:
    schedule.run_pending()
    # time.sleep(1)
