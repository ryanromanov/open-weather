# main.py
from weather import WeatherController
from weather import WeatherService


def weather_prompt(controller, weather_service):
    print('Please enter a city and state abbreviation, separated by a comma. For example: \'Pittsburgh, PA\'')
    user_input = (input("City and State: ")
                  .split(','))
    city = user_input[0].strip().capitalize()
    state = user_input[1].strip().upper()

    weather_text = controller.get_weather_discussion(city, state)
    summary = weather_service.summarize_weather(weather_text)
    print(summary)


def main():
    controller = WeatherController()
    weather_service = WeatherService()

    should_exit = False
    while should_exit is not True:
        user_input = input()
        match user_input:
            case 'forecast':
                weather_prompt(controller, weather_service)
            case _:
                return 'Not a valid input'


if __name__ == "__main__":
    main()
