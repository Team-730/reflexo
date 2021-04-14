from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
from database import DataBase as DB


class DostN:
    def __init__(self):
        self.db = DB()
        self.tokenizer = RegexTokenizer()
        self.model = FastTextSocialNetworkModel(tokenizer=self.tokenizer)
        self.tokens = self.tokenizer.split('всё очень плохо')

    def ready_msg(self, messages, nnID):
        results = self.model.predict(messages, k=2)
        sentiments = []
        for message, sentiment in zip(messages, results):
            sentiments.append(sentiment)
        try:
            pos = sentiments[0]['positive']
            self.db.setPos(nnID, pos)
        except Exception as e:
            print(e, 22)
            pos = 0
            self.db.setPos(nnID, pos)
        try:
            neg = sentiments[0]['negative']
            self.db.setNegative(nnID, neg)
        except Exception as e:
            print(e, 29)
            neg = 0
            self.db.setNegative(nnID, neg)
        try:
            ne = sentiments[0]['neutral']
            self.db.setNegative(nnID, ne)
        except Exception as e:
            print(e, 36)
            ne = 0
            self.db.setNegative(nnID, ne)
        return (sentiments)
