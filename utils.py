import os
import openai

token = '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'

# NPC 1 character
class npc:
    def __init__(self, bg_content):
        # Setting the API key to use the OpenAI API
        openai.api_key = token
        self.messages = [
            {"role": "system", "content": bg_content},
        ]

    def chat(self, message):
        self.messages.append({"role": "user", "content": message})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        self.messages.append({"role": "assistant", "content": response["choices"][0]["message"].content})
        return response["choices"][0]["message"]["content"]
    
    def conversation(self):
        return self.messages