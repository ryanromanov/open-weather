# main.py
from weather_controller import WeatherController

def main():
    print('hello')
    controller = WeatherController()
    city = input("Please enter a city: ")
    state = input("Please enter a state (in a two letter format: ")
    weather_text = controller.get_weather_discussion(city, state)



if __name__ == "__main__":
    main()
