# main.py
from weather import WeatherController
from weather import WeatherService

def main():
    print('hello')
    controller = WeatherController()
    weather_service = WeatherService()
    city = input("Please enter a city: ")
    state = input("Please enter a state (in a two letter format: ")
    weather_text = controller.get_weather_discussion(city, state)
    summary = weather_service.summarize_weather(weather_text)
    print(summary)



if __name__ == "__main__":
    main()
