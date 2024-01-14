import requests

def getWeather(api_key,location):
    url_base="http://api.openweathermap.org/data/2.5/weather"
    params= {'q':location,'appid':api_key,'units':'metric'}

    try:
        response=requests.get(url_base,params=params)
        data=response.json()
        
        if response.status_code==200:
            return data
        
        else:
            print(f"Error:{data['message']}")
            return None
    
    except Exception as e:
        print(f"Error fetching weather data:{str(e)}")
        return None
    
def display_weather(weather_data):
    if weather_data:
        print("\nCurrent Weather:")
        print(f"City:{weather_data['name']}")
        print(f"Temperature:{weather_data['main']['temp']}")
        print(f"Humidity:{weather_data['main']['humidity']}")
        print(f"Weatheer:{weather_data['weather'][0]['description']}")

    else:
        print("Weather data not available.")

if __name__=="__main__":
    id="061146959bd5667d4f6717d196766a01"
    loc=input("Enter city or ZIP code:")
    weather_data=getWeather(id,loc)

    if weather_data:
        display_weather(weather_data)