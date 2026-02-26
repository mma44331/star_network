import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')


class TextCleaner:
    def __init__(self, logger):
        self.logger = logger

    @staticmethod
    def stop_words(text):
        stop_words =set(stopwords.words("english"))
        word_tokens = word_tokenize(text)
        filter_text = [w for w in word_tokens if w not in stop_words]
        return " ".join(filter_text)

    def cleaner(self, text):
        self.logger.info(text)
        text = text.lower()
        charts_to_remove = string.punctuation + '״׳•●'
        text = text.translate(str.maketrans('','',charts_to_remove))
        text = self.stop_words(text)
        self.logger.info(text)
        return text