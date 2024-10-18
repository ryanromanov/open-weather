# ai_engine.py
import os
from openai import OpenAI

from helpers import get_ai_attitude_from_file


# possibly should have a "memory" class later
class AIEngine:

    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.messages = []
        self.client_attitude = {
            "role": "system", "content": get_ai_attitude_from_file() or None
        }

    def set_ai_attitude(self, attitude):
        if attitude is not None:
            self.client_attitude = {
                "role": "system", "content": attitude
            }
            self.messages.append(self.client_attitude)

    def send_message_to_client(self, message) -> str:
        """
        Appends the message the messages collection, and then sends the collection to the AI server
        :param message: the message you want to send to the AI server
        :return: the reply to the message
        """
        if message is None:
            raise Exception('message is null')

        self.messages.append(
            {'role': 'user', 'content': message}
        )

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=self.messages,
            temperature=0.5,
            stream=False,
        )

        reply = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": reply})
        return reply
