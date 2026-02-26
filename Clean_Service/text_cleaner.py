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
        self.stop_words =set(stopwords.words("english"))


    def cleaner(self, text):
        if not text:
            return  ""
        self.logger.info(text)
        text = text.lower()
        text = text.replace('’', '').replace('‘', '').replace('״', '').replace('׳', '')
        text = re.sub(r'[^a-z0-9\s]', ' ', text)
        word_tokens = word_tokenize(text)
        filtered_text = [w for w in word_tokens if w not in self.stop_words and len(w) > 1]
        cleaned_result = " ".join(filtered_text)
        self.logger.info(cleaned_result)
        return cleaned_result