from ai_engine import AIEngine

class WeatherService:

    def __init__(self):
        self.ai_engine = AIEngine('.config.ini')

    def summarize_weather(self, weather_data) -> str:
        """
        This method takes in weather data and sends it to an AI engine to be summarized.
        :param weather_data: weather data in text format
        :return: the summarized weather data
        """
        return self.ai_engine.send_message_to_client(weather_data)

