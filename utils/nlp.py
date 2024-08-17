import spacy
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class NLP:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))

    def preprocess_text(self, text):
        tokens = word_tokenize(text.lower())
        tokens = [word for word in tokens if word.isalpha() and word not in self.stop_words]
        lemmatized_tokens = [self.lemmatizer.lemmatize(token) for token in tokens]
        return lemmatized_tokens

    def analyze_sentiment(self, text):
        doc = self.nlp(text)
        sentiment = {'positive': doc.cats.get('positive', 0.5), 'negative': doc.cats.get('negative', 0.5)}
        return sentiment
