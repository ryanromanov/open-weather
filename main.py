# main.py
from weather import WeatherController
from weather import WeatherService


def main():
    controller = WeatherController()
    weather_service = WeatherService()
    print('Please enter a city and state abbreviation, separated by a comma. For example: \'Pittsburgh, PA\'')
    user_inputs = (input("City and State: ")
                   .split(','))
    city = user_inputs[0].strip().capitalize()
    state = user_inputs[1].strip().upper()

    weather_text = controller.get_weather_discussion(city, state)
    summary = weather_service.summarize_weather(weather_text)
    print(summary)


if __name__ == "__main__":
    main()
