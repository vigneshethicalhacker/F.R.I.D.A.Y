from utils.speech import Speech
from utils.nlp import NLP
import openai

class Jarvis:
    def __init__(self):
        self.speech = Speech()
        self.nlp = NLP()
        openai.api_key = 'YOUR_API_KEY'

    def ask_gpt(self, question):
        response = openai.Completion.create(
            engine="davinci",
            prompt=question,
            max_tokens=150
        )
        return response.choices[0].text.strip()

    def run(self):
        while True:
            text = self.speech.listen()
            if text:
                self.speech.speak(f"You said: {text}")
                self.nlp.process_text(text)
                answer = self.ask_gpt(text)
                self.speech.speak(answer)

if __name__ == "__main__":
    jarvis = Jarvis()
    jarvis.run()
