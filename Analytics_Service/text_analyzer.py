import json
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')


class TextAnalyzer:
    def __init__(self, logger):
        self.logger = logger
        self.max_10 = {}
        self.list_weapons = self._loader_weapons()

    def top_10(self,text):
        list_text = text.split(" ")
        for txt in list_text:
            if txt in self.max_10:
                self.max_10[txt] += 1
            else:
                self.max_10[txt] = 1
        empty = sorted(self.max_10.items(), key=lambda x: x[1], reverse=True)
        top_10 = [word[0] for word in empty[:10]]
        self.logger.info(f"Top 10 words: {top_10}")
        return top_10

    def _loader_weapons(self):
        with open('data/weapons.txt','r') as f:
            list_weapons = list(set(line.strip() for line in f if line.strip()))
        return list_weapons


    def find_fillings(self,text):
        scores =SentimentIntensityAnalyzer().polarity_scores(text)
        score = scores['compound']
        self.logger.info(f"the score of text '{text}' is {score}")
        if score >= 0.5000 and score <= 1.000:
            return "text_positive"
        elif score <= -0.4999 and score >= -1.000:
            return "text_negative"
        return "text_neutral"

    def get_list_weapons(self,text):
        text = text.lower()
        words_in_text = set(text.split())
        list_of_weapons = [weapon for weapon in self.list_weapons if weapon.lower() in words_in_text]
        self.logger.info(f"List weapons of the text: {list_of_weapons}")
        return list_of_weapons

    def analyze(self, text):
        top_10 = self.top_10(text)
        list_of_weapons = self.get_list_weapons(text)
        score_filling = self.find_fillings(text)
        return {
            'top_10': top_10,
            'list_of_weapons': list_of_weapons,
            'score_filling': score_filling
        }


