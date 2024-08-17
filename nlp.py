import spacy

class NLP:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def process_text(self, text):
        doc = self.nlp(text)
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.dep_)
