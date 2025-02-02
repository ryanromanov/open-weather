from ai_engine import AIEngine

class WeatherService:

    def __init__(self):
        self.ai_engine = AIEngine('config.ini')

    def summarize_weather(self, weather_data):
        return self.ai_engine.send_message_to_client(weather_data)

