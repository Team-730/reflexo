from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel

tokenizer = RegexTokenizer()
model = FastTextSocialNetworkModel(tokenizer=tokenizer)
tokens = tokenizer.split('всё очень плохо') 
def ready_msg(messages):
    results = model.predict(messages, k=2)
    sentiments = []
    for message, sentiment in zip(messages, results):
        sentiments.append(sentiment)
    return(sentiments)
ready_msg(['все круто'])