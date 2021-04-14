from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
from database import DataBase as DB


class DostN:
    def __init__(self):
        self.db = DB()
        self.tokenizer = RegexTokenizer()
        self.model = FastTextSocialNetworkModel(tokenizer=self.tokenizer)
        self.tokens = self.tokenizer.split('всё очень плохо')

    def ready_msg(self, messages, id):
        results = self.model.predict(messages, k=2)
        sentiments = []
        for message, sentiment in zip(messages, results):
            sentiments.append(sentiment)
        try:
            pos = sentiments[0]['positive']
            self.db.setPos(id, pos)
        except Exception as e:
            pos = 0
            self.db.setPos(id, pos)
        try:
            neg = sentiments[0]['negative']
            self.db.setNegativ(id, neg)
        except Exception as e:
            neg = 0
            self.db.setNegativ(id, neg)
        try:
            ne = sentiments[0]['neutral']
            self.db.setNegativ(id, ne)
        except Exception as e:
            ne = 0
            self.db.setNegativ(id, ne)
        return (sentiments)
