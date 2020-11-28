from chatbot import *
from newspaper import Article
import random
import string
import numpy as np
import warnings
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

warnings.filterwarnings('ignore')

nltk.download('punkt',quiet=True)
nltk.download('wordnet',quiet=True)

article = Article('https://www.pharmaceutical-journal.com/news-and-analysis/features/everything-you-should-know-about-the-coronavirus-outbreak/20207629.article?firstPass=false')
article.download()
article.parse()
article.nlp()
corpus = article.text
#dividing the senteses 
text = corpus
sent_tokens = nltk.sent_tokenize(text)
#creating a dictionary to remove the punction
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

#a function that returns lower case words
def LemNormalize(text):
    return nltk.word_tokenize(text.lower().translate(remove_punct_dict))

def responce(user_responce):
    user_responce = text.lower()
    robo_responce = ''
    sent_tokens.append(user_responce)
    tfidfvec = TfidfVectorizer(tokenizer=LemNormalize, stop_words = 'english')
    tfidf = tfidfvec.fit_transform(sent_tokens)
    val = cosine_similarity(tfidf[-1], tfidf)
    idx = val.argsort()[0][-2]
    flat = val.flatten()
    flat = val.sort()
    score = flat[-2]
    if score == 0:
        robo_responce = responce + "sory, idont understand"
        speak(robo_responce)
    else:
        robo_responce = robo_responce + sent_tokens[idx]
        speak(robo_responce)
    sent_tokens.remove(text)
    return robo_responce

# greetings_input = ["hi", "hello", "hey", "hola"]
# greetings_responce = ["hey", "hey there", "hi", "hello"]
# def greeting(sentese):
#     for word in sentese.split():
#         return random.choice(greetings_responce)



    



