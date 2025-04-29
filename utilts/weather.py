import requests

def index(request):
    city = "lahore"
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=aff584d9aedae231ab24591531c1e091'
    PARAMS = {'units': 'metric'}
    data = requests.get(url, params=PARAMS).json()
    if 'main' not in data:
        print(request,'Some Thing Wrong')
    try:
        description = data['weather'][0]['description']
        # Extracting weather icon
        icon = data['weather'][0]['icon']
        # Extracting temperature
        temp = data['main']['temp']
        # Extracting humidity
        humidity = data['main']['humidity']
        # Extracting wind speed
        wind_speed = data['wind']['speed']
        # Extracting maximum temperature
        max_temp = data['main']['temp_max']
        # Extracting minimum temperature
        min_temp = data['main']['temp_min']
        # Extracting atmospheric pressure
        pressure = data['main']['pressure']
        # Extracting precipitation (rainfall)
        precipitation = data.get('rain', 0)
        # Extracting cloudiness
        cloudiness = data['clouds']['all']
        # Extracting sunrise time and converting it to datetime
        import datetime
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        # # Extracting sunset time and converting it to datetime
        import datetime
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        # time -----------
        from datetime import datetime
        sunset_time = sunset.time()
        sunrise_time = sunrise.time()
        now = datetime.now()
        current_time = now.time()
        time = current_time.strftime("%H:%M:%S")
        date = datetime.now()
        date = date.date()
        cloud = {
            'description': description,
            'icon': icon,
            'temp': temp,
            'humidity': humidity,
            'wind_speed': wind_speed,
            'max_temp': max_temp,
            'min_temp': min_temp,
            'pressure': pressure,
            'precipitation': precipitation,
            'cloudiness': cloudiness,
            'sunrise': sunrise,
            'sunset': sunset,
            'time':time,
            'date':date,
            'sunrise_time':sunrise_time,    
            'sunset_time':sunset_time,
            'city':city
        }
        print(cloud)
    except:
        # messages.success(request,'Some Thing Wrong')
        print('')

index(requests)    



