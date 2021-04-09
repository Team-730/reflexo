from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
from database import DataBase as DB
db = DB()

tokenizer = RegexTokenizer()
model = FastTextSocialNetworkModel(tokenizer=tokenizer)
tokens = tokenizer.split('всё очень плохо') 
def ready_msg(messages):
    results = model.predict(messages, k=2)
    sentiments = []
    for message, sentiment in zip(messages, results):
        sentiments.append(sentiment)
    return(sentiments)
texts = db.getText()
for i, el in enumerate(texts):
    db.AddRes(i+1, ready_msg([el])) 
