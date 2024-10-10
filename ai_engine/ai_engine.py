# ai_engine.py
import os
from openai import OpenAI

# possibly should have a "memory" class later
class AIEngine:

    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.messages = []
        self.client_attitude = {
            "role": "system", "content": "You are a meteorologist explaining weather data to a layperson."
        }

    def set_ai_attitude(self, attitude):
        if attitude is not None:
            self.client_attitude = {
                "role": "system", "content": attitude
            }
            self.messages.append(self.client_attitude)

