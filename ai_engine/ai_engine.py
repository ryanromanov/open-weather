# ai_engine.py
import os
from openai import OpenAI

from helpers import get_ai_attitude_from_file


# possibly should have a "memory" class later
class AIEngine:

    def __init__(self, config_file_name):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.messages = []
        self.client_attitude = {
            "role": "system", "content": get_ai_attitude_from_file(config_file_name) or None
        }

    def set_ai_attitude(self, attitude):
        if attitude is not None:
            self.client_attitude = {
                "role": "system", "content": attitude
            }
            self.messages.append(self.client_attitude)
        else:
            print('Error: no attitude found')

    def send_message_to_client(self, message) -> str:
        """
        Appends the message the messages collection, and then sends the collection to the AI server
        :param message: the message you want to send to the AI server
        :return: the reply to the message
        """
        if message is None:
            raise Exception('message is null')

        self.messages.append(
            {'role': 'user', 'content': str(message)}
        )


        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=self.messages,
            temperature=0.5,
            stream=False,
        )

        print(response)

        reply = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": reply})
        return reply
